"""
PHA 1: BÓC TÁCH & CHIA NHỎ KỊCH BẢN + VOICE DÀI (10-45 PHÚT) THEO MẠCH Ý NGHĨA
- Không cắt cứng ở 3 phút hay 5 phút.
- Lấy các đoạn văn có ý nghĩa trọn vẹn trong Kịch bản gốc (Paragraphs) làm tham chiếu.
- Gom các đoạn văn liên tiếp sao cho mỗi Phần (phan_01, phan_02...) có độ dài khoảng 2.0 - 3.0 phút (120s - 190s)
  và điểm cắt nằm chính xác tại khoảng nghỉ giữa câu kết thúc đoạn trước và câu mở đầu đoạn sau.
- Xuất ra cho mỗi phần:
  1. File chữ: 1_INPUT_NHAN_SU/cac_phan_da_cat/phan_XX/phan_XX_kich_ban.txt
  2. File âm thanh: 1_INPUT_NHAN_SU/cac_phan_da_cat/phan_XX/phan_XX_voice.mp3
  3. File mốc thời gian (đã quy đổi về 0.00s của phần đó): phan_XX_timestamps.json
  4. Báo cáo tổng hợp: 1_INPUT_NHAN_SU/cac_phan_da_cat/bao_cao_chia_phan_pha_1.json
"""
import sys
import os
import json

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)
import re
import subprocess
import numpy as np
from difflib import SequenceMatcher
import imageio_ffmpeg

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
os.environ["PATH"] = os.path.dirname(FFMPEG_EXE) + os.pathsep + os.environ.get("PATH", "")


def load_audio_16k(audio_path):
    cmd = [
        FFMPEG_EXE, "-nostdin", "-threads", "0",
        "-i", audio_path,
        "-f", "s16le", "-ac", "1", "-acodec", "pcm_s16le", "-ar", "16000", "-"
    ]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0


def detect_script_language(text):
    if not text:
        return None
    vn_chars = re.findall(r"[ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", text.lower())
    return "vi" if len(vn_chars) > 10 else "en"


def norm_word(w):
    return re.sub(r"[^\w]", "", w).lower()


def slice_audio_mp3(src_audio, start_sec, end_sec, out_mp3):
    os.makedirs(os.path.dirname(os.path.abspath(out_mp3)), exist_ok=True)
    dur = max(0.5, end_sec - start_sec)
    cmd = [
        FFMPEG_EXE, "-y",
        "-ss", f"{start_sec:.2f}",
        "-i", src_audio,
        "-t", f"{dur:.2f}",
        "-c:a", "libmp3lame", "-q:a", "2",
        out_mp3
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)


def fmt_mmss(sec):
    m = int(sec // 60)
    s = int(round(sec % 60))
    return f"{m:02d}:{s:02d}"


def split_input_by_semantic_meaning(audio_path, script_path, out_base_dir, target_part_sec=145.0):
    with open(script_path, encoding="utf-8") as f:
        raw_script = f.read().strip()

    # Tách kịch bản thành các đoạn văn (Paragraphs) có ý nghĩa
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n+", raw_script) if p.strip()]
    if len(paragraphs) <= 1:
        # Nếu người dùng không xuống dòng đôi, tách theo cụm 3-4 câu
        sentences = re.split(r"(?<=[.!?])\s+", raw_script)
        paragraphs = [" ".join(sentences[i:i+4]) for i in range(0, len(sentences), 4)]

    # Kiểm tra xem đã có bản cache timestamps tổng chưa để tiết kiệm thời gian nếu chạy lại
    cache_ts_path = os.path.join(out_base_dir, "full_master_timestamps.json")
    if os.path.exists(cache_ts_path):
        with open(cache_ts_path, encoding="utf-8") as f:
            master_data = json.load(f)
        whisper_words = master_data["aligned_words"]
        total_duration = master_data["duration"]
        similarity_pct = master_data["verification"]["similarity_score_pct"]
        print(f"[Pha 1] Đã nạp bảng mốc thời gian gốc từ bộ nhớ đệm ({total_duration}s, {len(whisper_words)} từ).")
    else:
        from faster_whisper import WhisperModel
        lang = detect_script_language(raw_script)
        print(f"[Pha 1] Đang đồng bộ Giọng đọc & Kịch bản gốc ({lang})...")
        audio_np = load_audio_16k(audio_path)
        total_duration = round(len(audio_np) / 16000.0, 2)
        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(
            audio_np,
            language=lang,
            word_timestamps=True,
            vad_filter=True,
            initial_prompt=raw_script[:800]
        )
        whisper_words = []
        for seg in segments:
            if seg.words:
                for w in seg.words:
                    whisper_words.append({
                        "whisper_word": w.word.strip(),
                        "start": round(w.start, 2),
                        "end": round(w.end, 2),
                        "probability": round(w.probability, 2)
                    })

        all_script_tokens = [w for w in re.split(r"\s+", raw_script) if w]
        w_norm = [norm_word(w["whisper_word"]) for w in whisper_words]
        s_norm = [norm_word(t) for t in all_script_tokens]
        matcher = SequenceMatcher(None, w_norm, s_norm)
        similarity_pct = round(matcher.ratio() * 100, 1)

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    whisper_words[i1 + k]["locked_word"] = all_script_tokens[j1 + k]
            elif tag == "replace":
                w_slice = whisper_words[i1:i2]
                s_slice = all_script_tokens[j1:j2]
                for idx, w_obj in enumerate(w_slice):
                    w_obj["locked_word"] = s_slice[min(idx, len(s_slice) - 1)] if s_slice else w_obj["whisper_word"]
        for w in whisper_words:
            if "locked_word" not in w:
                w["locked_word"] = w["whisper_word"]

        os.makedirs(out_base_dir, exist_ok=True)
        with open(cache_ts_path, "w", encoding="utf-8") as f:
            json.dump({
                "audio_file": audio_path,
                "script_file": script_path,
                "duration": total_duration,
                "verification": {"similarity_score_pct": similarity_pct},
                "aligned_words": whisper_words
            }, f, ensure_ascii=False, indent=2)

    # Ánh xạ từng đoạn văn (Paragraph) vào dải từ trong whisper_words
    para_word_counts = [len([w for w in re.split(r"\s+", p) if w]) for p in paragraphs]
    total_script_words = max(1, sum(para_word_counts))
    total_w_words = len(whisper_words)

    para_infos = []
    w_cursor = 0
    for idx, p_text in enumerate(paragraphs):
        p_wc = para_word_counts[idx]
        est_len = int(round((p_wc / total_script_words) * total_w_words))
        w_start_idx = min(w_cursor, total_w_words - 1)
        if idx == len(paragraphs) - 1:
            w_end_idx = total_w_words - 1
        else:
            raw_end = min(total_w_words - 1, w_start_idx + max(1, est_len) - 1)
            # Tinh chỉnh điểm kết thúc đoạn văn trùng với dấu chấm câu hoặc khoảng nghỉ (Silence gap)
            best_end = raw_end
            best_gap = -1.0
            search_lo = max(w_start_idx + 1, raw_end - 8)
            search_hi = min(total_w_words - 2, raw_end + 8)
            for cand_i in range(search_lo, search_hi + 1):
                gap = whisper_words[cand_i + 1]["start"] - whisper_words[cand_i]["end"]
                word_str = whisper_words[cand_i].get("locked_word", "")
                bonus = 0.25 if word_str.endswith((".", "!", "?")) else 0.0
                if gap + bonus > best_gap:
                    best_gap = gap + bonus
                    best_end = cand_i
            w_end_idx = best_end

        t0 = 0.0 if idx == 0 else round((whisper_words[w_start_idx - 1]["end"] + whisper_words[w_start_idx]["start"]) / 2.0, 2)
        t1 = total_duration if idx == len(paragraphs) - 1 else round((whisper_words[w_end_idx]["end"] + whisper_words[min(total_w_words - 1, w_end_idx + 1)]["start"]) / 2.0, 2)

        para_infos.append({
            "para_index": idx + 1,
            "text": p_text,
            "w_start_idx": w_start_idx,
            "w_end_idx": w_end_idx,
            "t0": t0,
            "t1": t1
        })
        w_cursor = w_end_idx + 1

    # Gom các đoạn văn theo mạch ý nghĩa sao cho mỗi Phần dài khoảng target_part_sec (120s - 190s)
    parts = []
    cur_paras = []
    for p_info in para_infos:
        cur_paras.append(p_info)
        cur_dur = cur_paras[-1]["t1"] - cur_paras[0]["t0"]
        if cur_dur >= target_part_sec:
            parts.append(cur_paras)
            cur_paras = []
    if cur_paras:
        # Nếu phần dư cuối quá ngắn (< 45s) thì gộp vào phần trước đó
        if parts and (cur_paras[-1]["t1"] - cur_paras[0]["t0"] < 45.0):
            parts[-1].extend(cur_paras)
        else:
            parts.append(cur_paras)

    report_parts = []
    print("=" * 78)
    print(f"[PHA 1] BÁO CÁO BÓC TÁCH & CHIA NHỎ KỊCH BẢN + VOICE THEO Ý NGHĨA ({len(parts)} PHẦN)")
    print("=" * 78)

    for p_idx, p_group in enumerate(parts, start=1):
        part_id = f"phan_{p_idx:02d}"
        part_dir = os.path.join(out_base_dir, part_id)
        os.makedirs(part_dir, exist_ok=True)

        p_t0 = p_group[0]["t0"]
        p_t1 = p_group[-1]["t1"]
        p_dur = round(p_t1 - p_t0, 2)
        p_text = "\n\n".join(x["text"] for x in p_group)

        # Cắt từ và quy đổi mốc thời gian về 0.00s của phần đó
        w_lo = p_group[0]["w_start_idx"]
        w_hi = p_group[-1]["w_end_idx"]
        part_words = []
        for w in whisper_words[w_lo:w_hi + 1]:
            part_words.append({
                "word": w.get("locked_word", w["whisper_word"]),
                "start": round(max(0.0, w["start"] - p_t0), 2),
                "end": round(max(0.05, w["end"] - p_t0), 2),
                "global_start": w["start"],
                "global_end": w["end"]
            })

        txt_out = os.path.join(part_dir, f"{part_id}_kich_ban.txt")
        mp3_out = os.path.join(part_dir, f"{part_id}_voice.mp3")
        ts_out = os.path.join(part_dir, f"{part_id}_timestamps.json")

        with open(txt_out, "w", encoding="utf-8") as f:
            f.write(p_text + "\n")

        slice_audio_mp3(audio_path, p_t0, p_t1, mp3_out)

        with open(ts_out, "w", encoding="utf-8") as f:
            json.dump({
                "part_id": part_id,
                "global_t0": p_t0,
                "global_t1": p_t1,
                "duration": p_dur,
                "word_count": len(part_words),
                "words": part_words
            }, f, ensure_ascii=False, indent=2)

        # Tạo thư mục nguyên liệu tương ứng trong Ngăn 2
        os.makedirs(os.path.join("2_KHO_NGUYEN_LIEU", "theo_tung_phan", part_id, "images_polaroid"), exist_ok=True)
        os.makedirs(os.path.join("2_KHO_NGUYEN_LIEU", "theo_tung_phan", part_id, "stickers_cutout"), exist_ok=True)
        os.makedirs(os.path.join("2_KHO_NGUYEN_LIEU", "theo_tung_phan", part_id, "video_footage"), exist_ok=True)

        first_words = " ".join(p_text.split()[:9]) + "..."
        last_words = "..." + " ".join(p_text.split()[-9:])
        info_item = {
            "part_id": part_id,
            "time_range_mmss": f"{fmt_mmss(p_t0)} -> {fmt_mmss(p_t1)}",
            "global_t0": p_t0,
            "global_t1": p_t1,
            "duration_sec": p_dur,
            "word_count": len(part_words),
            "paragraph_count": len(p_group),
            "opening_phrase": first_words,
            "closing_phrase": last_words,
            "text_file": txt_out.replace("\\", "/"),
            "voice_file": mp3_out.replace("\\", "/"),
            "timestamps_file": ts_out.replace("\\", "/")
        }
        report_parts.append(info_item)
        print(f"• {part_id.upper()} [{info_item['time_range_mmss']} | {p_dur:5.1f}s | {len(part_words):3d} từ]")
        print(f"  - Mở đầu : \"{first_words}\"")
        print(f"  - Kết thúc: \"{last_words}\"")
        print(f"  - Text    : {info_item['text_file']}")
        print(f"  - Voice   : {info_item['voice_file']}")

    summary_path = os.path.join(out_base_dir, "bao_cao_chia_phan_pha_1.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "source_audio": audio_path,
            "source_script": script_path,
            "total_duration_sec": total_duration,
            "similarity_score_pct": similarity_pct,
            "total_parts": len(report_parts),
            "parts": report_parts
        }, f, ensure_ascii=False, indent=2)

    print("=" * 78)
    print(f"🛑 [CỔNG DỪNG 1]: Đã chia nhỏ xong {len(report_parts)} phần (Text + Voice). Dừng chờ người dùng duyệt!")
    print("=" * 78)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Cách dùng: python pha-1-chia-nho-input.py <voice_mp3> <script_txt_md> [out_base_dir]")
        sys.exit(1)
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "1_INPUT_NHAN_SU/cac_phan_da_cat"
    split_input_by_semantic_meaning(sys.argv[1], sys.argv[2], out_dir)
