"""
PHA 4 (VERSION 2.0 MULTI-WORLD ARCHITECTURE — CHUẨN VĂN THIẾT):
KIỂM TOÁN TOÁN HỌC ĐA THẾ GIỚI THỊ GIÁC (WORLD VARIETY GATE), BẤT ĐỐI XỨNG TỌA ĐỘ (LAYOUT ASYMMETRY GATE),
CHỐNG TÍCH TỤ TẠP NHAM (MAX 3 PHẦN TỬ), CHỐNG ĐÈ CHỮ, CHỐNG KHOẢNG CHẾT & BẢO TOÀN ĐỘNG LƯỢNG VẾT CẮT.
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

IMAGE_HIGHLIGHT_OVERLAYS = {
    "RED_INK_CIRCLE", "FOCUS_FRAME", "HANDWRITTEN_CALLOUT",
    "TORN_PAPER_SPLIT", "MAP_ROUTE", "SPOTLIGHT_XRAY", "RED_STRING_LINK"
}

MOTIF_TO_WORLD = {
    "MOTIF_3_CARTOGRAPHIC_3D_FLYOVER": "WORLD_1_FULL_MAP",
    "MOTIF_2_BROLL_KINETIC_OVERDRIVE": "WORLD_2_CINEMA_FULLBLEED",
    "MOTIF_1_DETECTIVE_CANVAS_PAN": "WORLD_3_DETECTIVE_CANVAS",
    "MOTIF_5_DATA_STORY_PROGRESSION": "WORLD_4_DATA_STAGE",
    "MOTIF_4_EVIDENCE_SPLIT_COLLISION": "WORLD_5_ARCHIVE_XRAY",
    "WORLD_1_FULL_MAP": "WORLD_1_FULL_MAP",
    "WORLD_2_CINEMA_FULLBLEED": "WORLD_2_CINEMA_FULLBLEED",
    "WORLD_3_DETECTIVE_CANVAS": "WORLD_3_DETECTIVE_CANVAS",
    "WORLD_4_DATA_STAGE": "WORLD_4_DATA_STAGE",
    "WORLD_5_ARCHIVE_XRAY": "WORLD_5_ARCHIVE_XRAY",
}


def get_bbox(beat):
    if beat.get("full_bleed"):
        return (0, 0, 1920, 1080)
    x = int(beat.get("x", 100))
    y = int(beat.get("y", 100))
    btype = beat.get("type", "POLAROID")
    default_w, default_h = 520, 380
    if btype == "STAMP":
        default_w, default_h = 380, 100
    elif btype in ("RED_INK_CIRCLE", "FOCUS_FRAME", "HANDWRITTEN_CALLOUT", "SPOTLIGHT_XRAY"):
        default_w, default_h = 320, 180
    elif btype in ("TORN_PAPER_SPLIT",):
        default_w, default_h = 90, 1080
    elif btype in ("MAP_ROUTE", "RED_STRING_LINK"):
        fx = int(beat.get("from_x", x))
        fy = int(beat.get("from_y", y))
        tx = int(beat.get("to_x", x + 400))
        ty = int(beat.get("to_y", y + 200))
        return (min(fx, tx) - 40, min(fy, ty) - 40, max(fx, tx) + 40, max(fy, ty) + 40)
    elif btype in ("WAFFLE_100_ARRAY", "ROUGH_EDGE_BARS", "SVG_LINE_CHART", "TIMELINE_SCROLLER"):
        default_w, default_h = 680, 320
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


def classify_scene_layout(sc):
    world = sc.get("world_type") or MOTIF_TO_WORLD.get(sc.get("scene_motif", ""), "WORLD_3_DETECTIVE_CANVAS")
    if world in ("WORLD_1_FULL_MAP", "WORLD_2_CINEMA_FULLBLEED"):
        return "FULL_BLEED"
    if world == "WORLD_4_DATA_STAGE":
        return "CENTER_DATA_STAGE"
    beats = sc.get("beats", [])
    for b in beats:
        if b.get("full_bleed") or int(b.get("w", 0)) >= 1350:
            return "FULL_BLEED"
        if b.get("type") in ("POLAROID", "VIDEO_CLIP", "STICKER", "TIMELINE_SCROLLER", "SVG_LINE_CHART"):
            bx = int(b.get("x", 100))
            bw = int(b.get("w", 600))
            if bw >= 1150 or (240 <= bx <= 550 and bw >= 820):
                return "CENTER_STAGE"
            if bx >= 720:
                return "RIGHT_ANCHOR"
            return "LEFT_ANCHOR"
    return "CENTER_STAGE"


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
    prev_world = None
    worlds_used = []
    layouts_used = []
    consecutive_left_anchor = 0

    for sc in scenes:
        sc_id = sc.get("id", "sc")
        raw_motif = sc.get("world_type") or sc.get("scene_motif", "")
        sc_world = MOTIF_TO_WORLD.get(raw_motif, raw_motif or "WORLD_3_DETECTIVE_CANVAS")
        worlds_used.append(sc_world)
        if prev_world and sc_world == prev_world:
            errors.append(
                f"[{sc_id}] LẶP THẾ GIỚI CÔNG NGHIỆP (WORLD_VARIETY_GATE): Cảnh '{sc_id}' dùng trùng '{sc_world}' với cảnh liền trước!"
            )
        prev_world = sc_world

        sc_layout = sc.get("layout_mode") or classify_scene_layout(sc)
        layouts_used.append(sc_layout)
        if sc_layout == "LEFT_ANCHOR":
            consecutive_left_anchor += 1
            if consecutive_left_anchor > 2:
                warnings.append(
                    f"[{sc_id}] LẶP BỐ CỤC GÓC TRÁI (LAYOUT_ASYMMETRY_GATE): Đã có {consecutive_left_anchor} cảnh liên tiếp đặt tư liệu ở góc trái (LEFT_ANCHOR). Hãy đổi sang FULL_BLEED, CENTER_STAGE hoặc RIGHT_ANCHOR!"
                )
        else:
            consecutive_left_anchor = 0

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
            is_fb = bool(b.get("full_bleed")) or btype in ("TORN_PAPER_SPLIT", "MAP_ROUTE", "RED_STRING_LINK")
            if not is_fb and (box[0] < 0 or box[1] < 0 or box[2] > 1920 or box[3] > 1080):
                errors.append(f"[{sc_id} | {stt_id}] TRÀN KHUNG 1920x1080: bbox={box}")

            bboxes.append((stt_id, b, box))

        # Kiểm tra đè chồng giữa các phần tử cùng xuất hiện (trừ lớp nền full_bleed hoặc lớp phủ highlight)
        for i in range(len(bboxes)):
            for j in range(i + 1, len(bboxes)):
                idA, bA, boxA = bboxes[i]
                idB, bB, boxB = bboxes[j]
                if not time_overlaps(bA, bB):
                    continue
                if bA.get("full_bleed") or bB.get("full_bleed"):
                    continue
                types_pair = {bA.get("type"), bB.get("type")}
                if types_pair & IMAGE_HIGHLIGHT_OVERLAYS:
                    continue
                ratio = overlap_ratio(boxA, boxB)
                if ratio > 0.08:
                    errors.append(f"[{sc_id}] ĐÈ BỐ CỤC ({int(ratio*100)}%): '{idA}' ({bA.get('type')}) đè lên '{idB}' ({bB.get('type')})")

        # Kiểm tra số phần tử tối đa xuất hiện cùng lúc (<= 3)
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

    unique_worlds = len(set(worlds_used))
    if len(scenes) >= 5 and unique_worlds < 4:
        warnings.append(
            f"[WORLD_VARIETY_GATE] Phần này chỉ dùng {unique_worlds}/5 Thế Giới Thị Giác ({set(worlds_used)}). Chuẩn v2.0 yêu cầu tối thiểu 4/5 Thế giới!"
        )

    dynamic_types = {
        "VIDEO_CLIP", "STICKER", "WAFFLE_100_ARRAY", "ROUGH_EDGE_BARS",
        "TORN_PAPER_SPLIT", "HANDWRITTEN_CALLOUT", "NUMBER_COUNTER",
        "RED_INK_CIRCLE", "STAMP", "MAP_ROUTE", "SPOTLIGHT_XRAY",
        "TIMELINE_SCROLLER", "SVG_LINE_CHART", "RED_STRING_LINK"
    }
    dynamic_count = sum(cnt for t, cnt in type_counts.items() if t in dynamic_types)
    dynamic_ratio = (dynamic_count / float(max(1, total_beats))) * 100.0

    print("=" * 88)
    print(f"[PHA 4 - DIRECTOR QA V2.0 MULTI-WORLD] BÁO CÁO KIỂM TOÁN ĐA THẾ GIỚI ({sb.get('part_id', '')})")
    print("=" * 88)
    print(f"• Tổng số Cảnh lớn (Scenes)                  : {len(scenes)} cảnh ({unique_worlds}/5 Thế Giới Thị Giác)")
    print(f"• Tổng số Nhịp (Enter-Hold-Exit Beats)       : {total_beats} nhịp ({round(duration/max(1,total_beats), 2)}s / nhịp)")
    print(f"• Khoảng giữ nhịp dài nhất (Max Hold Stretch): {max_dead_stretch_global:.2f}s (Chuẩn <= 4.50s)")
    print(f"• Tỷ lệ Chất liệu Động & Tương tác Vật lý    : {dynamic_ratio:.1f}% ({dynamic_count}/{total_beats} nhịp)")
    if worlds_used:
        print(f"• Chuỗi Thế Giới Thị Giác (5 Visual Worlds)  : {' -> '.join(worlds_used)}")
    if layouts_used:
        print(f"• Chuỗi Bố Cục Tọa Độ (Layout Modes)         : {' -> '.join(layouts_used)}")
    print(f"• Số phần tử tối đa trên màn hình cùng lúc   : {max_concurrent} phần tử (Chuẩn <= 3 — 0% tạp nham)")
    print(f"• Track 1 (V1 - Media STT)                   : {verified_stt_files} tư liệu chính")
    print(f"• Track 2 (FX1 - Đồ họa Vào/Ra Tuần tự)      : {total_beats - verified_stt_files} khối ({dict(type_counts)})")
    print(f"• Track 3 (SUB1 - Phụ đề Song ngữ EN/VI)     : {len(subtitles)} cặp câu phụ đề")
    print(f"• Track 4 (A1 - Giọng đọc + BGM 3 Tầng)      : {sb.get('voice_path', '')} ({duration:.1f}s)")
    print(f"• Track 5 (A2 - Tiếng động Foley Tự nhiên)   : {sfx_count} điểm nhấn âm thanh .WAV")
    print(f"• Số lỗi P0 (Đè chữ / Tràn khung / Lặp World): {len(errors)} lỗi | Cảnh báo P1 (Nhịp/Bố cục): {len(warnings)}")
    if warnings:
        for w in warnings:
            print("  ⚠️ [P1 - CẢNH BÁO]:", w)
    if errors:
        for e in errors:
            print("  ❌", e)
        print("=" * 88)
        sys.exit(1)
    else:
        print("✅ [ĐẠT CHUẨN TOÁN HỌC V2.0 100% — 0 LỖI]: Tiếp tục chạy bước tiếp theo!")
        print("=" * 88)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python buoc_3_kiem_toan_nhip_va_vet_cat.py <storyboard_json> [--blueprint]")
        sys.exit(1)
    blueprint_mode = "--blueprint" in sys.argv
    run_qa_pha_4(sys.argv[1], blueprint_only=blueprint_mode)
