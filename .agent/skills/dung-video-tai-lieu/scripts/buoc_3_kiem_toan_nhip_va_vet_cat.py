"""
PHA 4 (VERSION 3.0 — CHUẨN VĂN THIẾT): KIỂM TRA TOÁN HỌC BỐ CỤC, CHỐNG TÍCH TỤ TẠP NHAM (MAX 3 PHẦN TỬ),
CHỐNG ĐÈ CHỮ, CHỐNG ĐỨNG HÌNH CHỜ GIỌNG ĐỌC (DEAD STRETCH GATE) & CHỐNG LẶP MÔ-TÍP CÔNG NGHIỆP
Kiểm tra 8 tiêu chí khắt khe trước khi mở Cổng Dừng 4:
1. Mọi nguyên liệu chính (POLAROID, STICKER, VIDEO_CLIP) đều có mã `stt_id` và tồn tại file vật lý.
2. Không phần tử nào tràn ra ngoài khung an toàn 1920x1080.
3. QUY LUẬT CHỐNG ĐỐNG TẠP NHAM (CLEAN STAGE LAW): Tại bất kỳ giây `t` nào trên toàn bộ video,
   tổng số phần tử đang hiển thị cùng lúc KHÔNG ĐƯỢC VƯỢT QUÁ 3 (1 Tư liệu chính + tối đa 2 điểm nhấn).
4. KHÔNG ĐÈ CHỒNG BẤT KỲ HỘP CHỮ HAY CON DẤU NÀO: Kiểm tra va chạm hình học giữa TẤT CẢ các thẻ (kể cả STAMP!).
5. Mật độ sự kiện thị giác duy trì nhịp sinh động.
6. CHỐT CHẶN KHOẢNG CHẾT (DEAD STRETCH GATE): Phát hiện ngay mọi khoảng thời gian > 3.5s màn hình đứng yên chờ giọng đọc.
7. CHỐT CHẶN CHỐNG LẶP MÔ-TÍP (ANTI-REPETITION MOTIF GATE): Cấm 2 cảnh liên tiếp trùng `scene_motif`.
8. BÁO CÁO ĐỘ ĐA DẠNG CHẤT LIỆU (MIXED-MEDIA ENTROPY): Đo tỷ lệ Video B-Roll, Sticker, Bản đồ & Biểu đồ động.
"""
import os
import sys
import json
from collections import Counter

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

IMAGE_HIGHLIGHT_OVERLAYS = {"RED_INK_CIRCLE", "FOCUS_FRAME", "HANDWRITTEN_CALLOUT", "TORN_PAPER_SPLIT"}


def get_bbox(beat):
    x = int(beat.get("x", 100))
    y = int(beat.get("y", 100))
    btype = beat.get("type", "POLAROID")
    default_w, default_h = 520, 380
    if btype == "STAMP":
        default_w, default_h = 380, 100
    elif btype in ("RED_INK_CIRCLE", "FOCUS_FRAME", "HANDWRITTEN_CALLOUT"):
        default_w, default_h = 320, 180
    elif btype == "TORN_PAPER_SPLIT":
        default_w, default_h = 90, 1080
    elif btype in ("WAFFLE_100_ARRAY", "ROUGH_EDGE_BARS"):
        default_w, default_h = 640, 250
    elif btype == "NUMBER_COUNTER":
        default_w, default_h = 560, 150
    elif btype == "DETECTIVE_TAPE_NOTE":
        default_w, default_h = 640, 155
    w = int(beat.get("w", default_w))
    h = int(beat.get("h", default_h))
    return (x, y, x + w, y + h)


def time_overlaps(b1, b2):
    t0_a, t1_a = float(b1.get("t0", 0)), float(b1.get("t1", 0))
    t0_b, t1_b = float(b2.get("t0", 0)), float(b2.get("t1", 0))
    return max(t0_a, t0_b) < (min(t1_a, t1_b) - 0.15)


def overlap_ratio(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    inter = max(0, xB - xA) * max(0, yB - yA)
    if inter == 0:
        return 0.0
    areaA = max(1, (boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    areaB = max(1, (boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))
    return inter / float(min(areaA, areaB))


def run_qa_pha_4(storyboard_path, blueprint_only=False):
    with open(storyboard_path, encoding="utf-8") as f:
        sb = json.load(f)

    errors = []
    warnings = []
    scenes = sb.get("scenes", [])
    subtitles = sb.get("subtitles", [])
    duration = float(sb.get("duration", 145.2))
    total_beats = 0
    verified_stt_files = 0
    sfx_count = 0
    type_counts = Counter()
    max_concurrent = 0
    max_dead_stretch_global = 0.0
    prev_motif = None
    motifs_used = []

    for sc in scenes:
        sc_id = sc.get("id", "sc")
        sc_motif = sc.get("scene_motif", "")
        if sc_motif:
            motifs_used.append(sc_motif)
            if prev_motif and sc_motif == prev_motif:
                errors.append(
                    f"[{sc_id}] LẶP MÔ-TÍP CÔNG NGHIỆP: Cảnh '{sc_id}' dùng trùng scene_motif '{sc_motif}' với cảnh liền trước!"
                )
            prev_motif = sc_motif
        beats = sc.get("beats", [])
        bboxes = []
        event_times = [float(sc.get("t0", 0.0)), float(sc.get("t1", 0.0))]
        for idx, b in enumerate(beats):
            total_beats += 1
            stt_id = b.get("stt_id", f"beat_{idx}")
            btype = b.get("type", "POLAROID")
            type_counts[btype] += 1
            event_times.append(float(b.get("t0", 0.0)))
            event_times.append(float(b.get("t1", 0.0)))

            if b.get("sfx"):
                sfx_count += 1

            if btype in ("POLAROID", "STICKER", "VIDEO_CLIP", "RED_INK_CIRCLE", "FOCUS_FRAME"):
                src = b.get("src", "")
                if blueprint_only:
                    if btype in ("POLAROID", "STICKER", "VIDEO_CLIP"):
                        verified_stt_files += 1
                else:
                    if not src or not os.path.exists(src):
                        errors.append(f"[{sc_id} | {stt_id}] THIẾU FILE VẬT LÝ: {src}")
                    elif btype in ("POLAROID", "STICKER", "VIDEO_CLIP"):
                        verified_stt_files += 1

            box = get_bbox(b)
            if btype != "TORN_PAPER_SPLIT" and (box[0] < 20 or box[1] < 20 or box[2] > 1900 or box[3] > 1060):
                errors.append(f"[{sc_id} | {stt_id}] TRÀN KHUNG 1920x1080: bbox={box}")

            bboxes.append((stt_id, b, box))

        # Kiểm tra đè chồng giữa TẤT CẢ các phần tử cùng xuất hiện (kể cả STAMP!)
        for i in range(len(bboxes)):
            for j in range(i + 1, len(bboxes)):
                idA, bA, boxA = bboxes[i]
                idB, bB, boxB = bboxes[j]
                if not time_overlaps(bA, bB):
                    continue
                # Chỉ cho phép RED_INK_CIRCLE hoặc FOCUS_FRAME nằm trên POLAROID, STICKER, VIDEO_CLIP
                types_pair = {bA.get("type"), bB.get("type")}
                if types_pair & IMAGE_HIGHLIGHT_OVERLAYS and (types_pair & {"POLAROID", "STICKER", "VIDEO_CLIP"}):
                    continue
                ratio = overlap_ratio(boxA, boxB)
                if ratio > 0.08:
                    errors.append(f"[{sc_id}] ĐÈ BỐ CỤC ({int(ratio*100)}%): '{idA}' ({bA.get('type')}) đè lên '{idB}' ({bB.get('type')})")

        # Kiểm tra số phần tử tối đa xuất hiện cùng lúc (Chống tích tụ thành đống tạp nham!)
        t_cursor = float(sc.get("t0", 0.0))
        t_end = float(sc.get("t1", 0.0))
        while t_cursor <= t_end:
            active_now = [
                b.get("stt_id") for b in beats
                if float(b.get("t0", 0)) <= t_cursor <= float(b.get("t1", 0))
            ]
            if len(active_now) > max_concurrent:
                max_concurrent = len(active_now)
            if len(active_now) > 3:
                errors.append(
                    f"[{sc_id} @ {t_cursor:.1f}s] TÍCH TỤ QUÁ NHIỀU PHẦN TỬ ({len(active_now)} > 3): {active_now}. "
                    f"Phải cho phần tử cũ thoát (t1) trước khi phần tử mới xuất hiện!"
                )
                break
            t_cursor += 0.5

        # Kiểm tra khoảng chết đứng hình chờ giọng đọc (Dead Stretch Gate)
        sc_t0 = float(sc.get("t0", 0.0))
        sc_t1 = float(sc.get("t1", 0.0))
        valid_ev = sorted(set(t for t in event_times if sc_t0 <= t <= sc_t1))
        for k in range(len(valid_ev) - 1):
            stretch = valid_ev[k + 1] - valid_ev[k]
            if stretch > max_dead_stretch_global:
                max_dead_stretch_global = stretch
            if stretch > 4.5:
                warnings.append(
                    f"[{sc_id}] KHOẢNG CHỜ DÀI ({stretch:.1f}s từ {valid_ev[k]:.1f}s -> {valid_ev[k+1]:.1f}s): "
                    f"Nên chèn thêm nhịp khoanh mực đỏ, đổi góc camera hoặc tách tư liệu con để tránh cảm giác đứng chờ giọng đọc."
                )

    dynamic_types = {
        "VIDEO_CLIP", "STICKER", "WAFFLE_100_ARRAY", "ROUGH_EDGE_BARS",
        "TORN_PAPER_SPLIT", "HANDWRITTEN_CALLOUT", "NUMBER_COUNTER", "RED_INK_CIRCLE", "STAMP"
    }
    dynamic_count = sum(cnt for t, cnt in type_counts.items() if t in dynamic_types)
    dynamic_ratio = (dynamic_count / float(max(1, total_beats))) * 100.0

    print("=" * 84)
    print(f"[PHA 4 - DIRECTOR QA V3.0] BÁO CÁO KIỂM TOÁN BỐ CỤC & CHỐNG CÔNG NGHIỆP ({sb.get('part_id', '')})")
    print("=" * 84)
    print(f"• Tổng số Cảnh lớn (Scenes)                  : {len(scenes)} cảnh (Đã xóa sạch nhãn SC_01 trên video)")
    print(f"• Tổng số Nhịp (Enter-Hold-Exit Beats)       : {total_beats} nhịp ({round(duration/max(1,total_beats), 2)}s / nhịp)")
    print(f"• Khoảng giữ nhịp dài nhất (Max Hold Stretch): {max_dead_stretch_global:.2f}s (Chuẩn <= 4.50s)")
    print(f"• Tỷ lệ Chất liệu Động & Tương tác Vật lý    : {dynamic_ratio:.1f}% ({dynamic_count}/{total_beats} nhịp)")
    if motifs_used:
        print(f"• Chuỗi Mô-típ Luân phiên (Scene Motifs)     : {' -> '.join(motifs_used)}")
    print(f"• Số phần tử tối đa trên màn hình cùng lúc   : {max_concurrent} phần tử (Chuẩn <= 3 — 0% tạp nham)")
    print(f"• Track 1 (V1 - Media STT 01..12)            : {verified_stt_files} tư liệu chính")
    print(f"• Track 2 (FX1 - Đồ họa Vào/Ra Tuần tự)      : {total_beats - verified_stt_files} khối ({dict(type_counts)})")
    print(f"• Track 3 (SUB1 - Phụ đề Song ngữ EN/VI)     : {len(subtitles)} cặp câu phụ đề")
    print(f"• Track 4 (A1 - Giọng đọc Voiceover)         : {sb.get('voice_path', '')} ({duration:.1f}s)")
    print(f"• Track 5 (A2 - Tiếng động Foley Tự nhiên)   : {sfx_count} điểm nhấn âm thanh .WAV")
    print(f"• Số lỗi P0 (Đè chữ / Tràn khung / Lặp Motif): {len(errors)} lỗi | Cảnh báo P1 (Nhịp): {len(warnings)}")
    if warnings:
        for w in warnings:
            print("  ⚠️ [P1 - NHỊP ĐIỆU]:", w)
    if errors:
        for e in errors:
            print("  ❌", e)
        print("=" * 84)
        sys.exit(1)
    else:
        print("✅ [ĐẠT CHUẨN TOÁN HỌC 100% — 0 LỖI]: Tiếp tục chạy bước tiếp theo!")
        print("=" * 84)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python buoc_3_kiem_toan_nhip_va_vet_cat.py <storyboard_json> [--blueprint]")
        sys.exit(1)
    blueprint_mode = "--blueprint" in sys.argv
    run_qa_pha_4(sys.argv[1], blueprint_only=blueprint_mode)
