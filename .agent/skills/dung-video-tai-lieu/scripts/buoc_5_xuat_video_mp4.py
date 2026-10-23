"""
PHA 5: BỘ KẾT XUẤT VIDEO .MP4 VẬT LÝ & TRỘN ÂM THANH MASTER (VOICE + SFX) — CHUẨN GU EDIT 10/10
Đọc kịch bản đã chỉnh sửa từ Bàn dựng 5-Track HTML (storyboard.json), trộn giọng đọc (phan_XX_voice.mp3)
cùng các hiệu ứng âm thanh (sfx/*.wav) đúng tới 0.01s, kết xuất khung hình 1920x1080 @ 30fps
hỗ trợ đầy đủ Kho 10 Hiệu Ứng Thị Giác (POLAROID, STICKER, VIDEO_CLIP, HEADLINE, SVG_RED_ARROW,
NUMBER_COUNTER, RED_MAP_PIN, DETECTIVE_TAPE_NOTE, MAGNIFIER_CALLOUT, STAMP) + Phụ đề Song ngữ tùy chọn,
và đóng gói thành file .MP4 hoàn chỉnh tại 3_OUTPUT_VIDEO_HOAN_CHINH/tung_phan_mp4/.
"""
import os
import sys
import json
import math

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)
import wave
import struct
import argparse
import subprocess
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import imageio_ffmpeg

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

WIDTH = 1920
HEIGHT = 1080
FPS = 30
_FONT_CACHE = {}
_VIDEO_FRAME_CACHE = {}


def get_font(size, bold=True, mono=False):
    key = (size, bold, mono)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    if mono:
        candidates = [
            r"C:\Windows\Fonts\courbd.ttf" if bold else r"C:\Windows\Fonts\cour.ttf",
            r"C:\Windows\Fonts\consolab.ttf" if bold else r"C:\Windows\Fonts\consola.ttf",
        ]
    else:
        candidates = [
            r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\tahomabd.ttf" if bold else r"C:\Windows\Fonts\tahoma.ttf",
        ]
    for path in candidates:
        if os.path.exists(path):
            try:
                f = ImageFont.truetype(path, size)
                _FONT_CACHE[key] = f
                return f
            except Exception:
                pass
    f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


def get_video_frames(video_path, target_w, target_h):
    key = (video_path, target_w, target_h)
    if key in _VIDEO_FRAME_CACHE:
        return _VIDEO_FRAME_CACHE[key]
    frames = []
    if not os.path.exists(video_path):
        _VIDEO_FRAME_CACHE[key] = frames
        return frames
    try:
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        cmd = [
            ffmpeg_exe, "-i", video_path,
            "-vf", f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},fps=15",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"
        ]
        raw = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        frame_bytes = target_w * target_h * 3
        n = len(raw) // frame_bytes
        for i in range(n):
            chunk = raw[i * frame_bytes:(i + 1) * frame_bytes]
            frames.append(Image.frombytes("RGB", (target_w, target_h), chunk))
    except Exception:
        pass
    _VIDEO_FRAME_CACHE[key] = frames
    return frames


def build_sfx_overlay_wav(storyboard, duration_sec, sfx_dir, out_wav_path):
    """Tạo đường âm thanh SFX 44100Hz khớp chính xác từng mốc t0 của 57+ Beat."""
    sample_rate = 44100
    total_samples = int(math.ceil((duration_sec + 1.0) * sample_rate))
    mix_buffer = [0.0] * total_samples

    sfx_cache = {}
    for sc in storyboard.get("scenes", []):
        for b in sc.get("beats", []):
            sfx_name = b.get("sfx")
            if not sfx_name:
                continue
            sfx_path = os.path.join(sfx_dir, sfx_name)
            if not os.path.exists(sfx_path):
                alt_path = os.path.join(".agent", "skills", "dung-video-tai-lieu", "assets", "sfx", sfx_name)
                if os.path.exists(alt_path):
                    sfx_path = alt_path
                else:
                    continue

            if sfx_path not in sfx_cache:
                try:
                    with wave.open(sfx_path, "rb") as wf:
                        n_frames = wf.getnframes()
                        raw = wf.readframes(n_frames)
                        ch = wf.getnchannels()
                        sw = wf.getsampwidth()
                        if sw == 2:
                            samples = struct.unpack(f"<{n_frames * ch}h", raw)
                            if ch > 1:
                                samples = samples[::ch]
                            sfx_cache[sfx_path] = [s / 32768.0 for s in samples]
                        else:
                            sfx_cache[sfx_path] = []
                except Exception:
                    sfx_cache[sfx_path] = []

            samples = sfx_cache.get(sfx_path, [])
            start_idx = int(float(b.get("t0", 0.0)) * sample_rate)
            for i, s in enumerate(samples):
                idx = start_idx + i
                if 0 <= idx < total_samples:
                    mix_buffer[idx] += s * 0.42

    os.makedirs(os.path.dirname(os.path.abspath(out_wav_path)), exist_ok=True)
    with wave.open(out_wav_path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        clamped = [max(-32767, min(32767, int(v * 32767))) for v in mix_buffer]
        wf.writeframes(struct.pack(f"<{len(clamped)}h", *clamped))
    return out_wav_path


def mix_voice_and_sfx(ffmpeg_exe, voice_path, sfx_wav_path, out_aac_path, duration_sec):
    """Trộn giọng đọc chính (phan_XX_voice.mp3) và đường tiếng động (sfx_track.wav) bằng FFmpeg."""
    if voice_path and os.path.exists(voice_path):
        cmd = [
            ffmpeg_exe, "-y",
            "-i", voice_path,
            "-i", sfx_wav_path,
            "-filter_complex", "[0:a]volume=1.0[v];[1:a]volume=0.80[s];[v][s]amix=inputs=2:duration=first:dropout_transition=2[aout]",
            "-map", "[aout]",
            "-t", str(duration_sec),
            "-c:a", "aac", "-b:a", "192k",
            out_aac_path
        ]
    else:
        cmd = [
            ffmpeg_exe, "-y",
            "-i", sfx_wav_path,
            "-t", str(duration_sec),
            "-c:a", "aac", "-b:a", "192k",
            out_aac_path
        ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out_aac_path


def render_polaroid_card(beat, img_cache, elapsed=0.0):
    w, h = int(beat.get("w", 520)), int(beat.get("h", 420))
    card = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([16, 18, w + 28, h + 30], radius=5, fill=(0, 0, 0, 95))
    draw.rounded_rectangle([8, 8, w + 18, h + 18], radius=4, fill=(250, 246, 235, 255), outline=(184, 174, 153, 255), width=2)

    src = beat.get("src", "")
    img_h = max(100, h - 68)
    img_w = max(100, w - 24)
    if src.lower().endswith(".mp4"):
        vframes = get_video_frames(src, img_w, img_h)
        if vframes:
            fidx = int(elapsed * 15) % len(vframes)
            card.paste(vframes[fidx], (20, 20))
        else:
            draw.rectangle([20, 20, 20 + img_w, 20 + img_h], fill=(35, 32, 28, 255))
    else:
        cache_key = (src, img_w, img_h)
        if cache_key not in img_cache:
            if os.path.exists(src):
                try:
                    im = Image.open(src).convert("RGB")
                    im = ImageOps.fit(im, (img_w, img_h), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
                    img_cache[cache_key] = im
                except Exception:
                    img_cache[cache_key] = None
            else:
                img_cache[cache_key] = None

        if img_cache.get(cache_key) is not None:
            card.paste(img_cache[cache_key], (20, 20))
        else:
            draw.rectangle([20, 20, 20 + img_w, 20 + img_h], fill=(35, 32, 28, 255))

    draw.rectangle([20, 20, 20 + img_w, 20 + img_h], outline=(210, 200, 178, 255), width=1)
    pin_x = (w + 26) // 2
    draw.ellipse([pin_x - 11, 0, pin_x + 11, 22], fill=(215, 38, 26, 255), outline=(74, 8, 4, 255), width=2)

    caption = beat.get("caption", "")
    if caption:
        font_cap = get_font(18, bold=True, mono=True)
        bbox = draw.textbbox((0, 0), caption[:62], font=font_cap)
        tw = bbox[2] - bbox[0]
        tx = max(22, (w + 26 - tw) // 2)
        draw.text((tx, 28 + img_h), caption[:62], fill=(31, 29, 26, 255), font=font_cap)

    rot = float(beat.get("rot", 0.0))
    if abs(rot) > 0.1:
        card = card.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)
    return card


def render_sticker_card(beat, img_cache):
    w, h = int(beat.get("w", 380)), int(beat.get("h", 440))
    canvas = Image.new("RGBA", (w + 40, h + 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    src = beat.get("src", "")
    cache_key = ("STICKER", src, w, h)
    if cache_key not in img_cache:
        if os.path.exists(src):
            try:
                im = Image.open(src).convert("RGBA")
                im.thumbnail((w - 16, h - 56), Image.Resampling.LANCZOS)
                # Tạo viền trắng + bóng đổ kiểu Sticker cắt rời
                alpha = im.split()[3]
                outline_mask = alpha.filter(ImageFilter.MaxFilter(9))
                shadow_mask = outline_mask.filter(ImageFilter.GaussianBlur(6))
                layered = Image.new("RGBA", (im.width + 24, im.height + 24), (0, 0, 0, 0))
                sh_img = Image.new("RGBA", im.size, (0, 0, 0, 140))
                layered.paste(sh_img, (12, 16), shadow_mask)
                wh_img = Image.new("RGBA", im.size, (255, 255, 255, 255))
                layered.paste(wh_img, (12, 12), outline_mask)
                layered.paste(im, (12, 12), im)
                img_cache[cache_key] = layered
            except Exception:
                img_cache[cache_key] = None
        else:
            img_cache[cache_key] = None

    im = img_cache.get(cache_key)
    if im is not None:
        ox = (w + 40 - im.width) // 2
        oy = max(4, (h - 36 - im.height) // 2)
        canvas.paste(im, (ox, oy), im)

    label = beat.get("label") or beat.get("caption") or ""
    if label:
        lbl_str = label[:68]
        font_lbl = get_font(18, bold=True)
        for sz in (18, 17, 16, 15, 14):
            f_try = get_font(sz, bold=True)
            bb_try = draw.textbbox((0, 0), lbl_str, font=f_try)
            if (bb_try[2] - bb_try[0]) + 32 <= w + 24:
                font_lbl = f_try
                break
        bbox = draw.textbbox((0, 0), lbl_str, font=font_lbl)
        tw = bbox[2] - bbox[0]
        pad_x = 16
        box_w = min(w + 28, tw + pad_x * 2)
        bx0 = max(4, (w + 40 - box_w) // 2)
        by0 = h - 22
        draw.rounded_rectangle([bx0 + 4, by0 + 5, bx0 + box_w + 4, by0 + 43], radius=4, fill=(0, 0, 0, 95))
        draw.rounded_rectangle([bx0, by0, bx0 + box_w, by0 + 38], radius=4, fill=(245, 197, 24, 255), outline=(20, 20, 20, 255), width=3)
        draw.text((bx0 + (box_w - tw) // 2, by0 + 8), lbl_str, fill=(20, 20, 20, 255), font=font_lbl)

    rot = float(beat.get("rot", 0.0))
    if abs(rot) > 0.1:
        canvas = canvas.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)
    return canvas


def render_headline_card(beat, progress, dark_mode=False):
    w, h = int(beat.get("w", 680)), int(beat.get("h", 225))
    card = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([10, 12, w + 14, h + 16], radius=5, fill=(0, 0, 0, 105))
    bg_col = (20, 22, 28, 248) if dark_mode else (252, 249, 240, 252)
    bd_col = (65, 72, 90, 255) if dark_mode else (30, 30, 30, 255)
    left_bar = (245, 197, 24, 255) if dark_mode else (184, 29, 19, 255)
    draw.rounded_rectangle([4, 4, w + 8, h + 8], radius=5, fill=bg_col, outline=bd_col, width=3)
    draw.rectangle([4, 4, 16, h + 8], fill=left_bar)

    prefix = beat.get("prefix", beat.get("text", ""))
    strikethrough = beat.get("strikethrough", "")
    highlight = beat.get("highlight", "")
    sub = beat.get("sub", "")

    font_pre = get_font(22, bold=True)
    font_hl = get_font(40, bold=True)
    font_sub = get_font(17, bold=True, mono=True)

    pre_col = (225, 228, 235, 255) if dark_mode else (74, 69, 61, 255)
    draw.text((34, 24 if strikethrough else 34), prefix[:52], fill=pre_col, font=font_pre)

    hl_y = 72
    if strikethrough:
        font_st = get_font(32, bold=True)
        draw.text((34, 54), strikethrough[:34], fill=(120, 115, 108, 255), font=font_st)
        st_bb = draw.textbbox((34, 54), strikethrough[:34], font=font_st)
        mid_y = (st_bb[1] + st_bb[3]) // 2
        draw.line([(30, mid_y + 2), (st_bb[2] + 6, mid_y - 2)], fill=(217, 35, 24, 255), width=5)
        hl_y = 96

    hl_str = highlight[:48]
    font_hl = get_font(38, bold=True)
    for sz in (38, 35, 32, 29, 26):
        f_try = get_font(sz, bold=True)
        bb_try = draw.textbbox((0, 0), hl_str, font=f_try)
        if (bb_try[2] - bb_try[0]) + 32 <= w - 44:
            font_hl = f_try
            break
    hl_bbox = draw.textbbox((0, 0), hl_str, font=font_hl)
    full_hl_w = min(w - 38, max(120, (hl_bbox[2] - hl_bbox[0]) + 28))
    hl_w = int(full_hl_w * min(1.0, max(0.22, progress)))
    draw.rounded_rectangle([32, hl_y, 32 + hl_w, hl_y + 56], radius=4, fill=(245, 197, 24, 255))
    draw.text((44, hl_y + 8), hl_str, fill=(18, 18, 18, 255), font=font_hl)
    if sub:
        sub_col = (205, 210, 220, 255) if dark_mode else (44, 40, 35, 255)
        draw.text((34, hl_y + 72), sub[:64], fill=sub_col, font=font_sub)
    return card


def render_waffle_array(beat, progress=1.0):
    w, h = int(beat.get("w", 640)), int(beat.get("h", 260))
    raw_pct = beat.get("percent", beat.get("highlight_count", 40))
    pct = max(1, min(100, int(raw_pct)))
    cur_pct = int(round(pct * min(1.0, progress * 1.6)))
    card = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([10, 12, w + 14, h + 16], radius=5, fill=(0, 0, 0, 95))
    draw.rounded_rectangle([4, 4, w + 8, h + 8], radius=5, fill=(252, 249, 240, 252), outline=(35, 32, 28, 255), width=3)

    font_t = get_font(20, bold=True)
    font_p = get_font(36, bold=True)
    font_s = get_font(14, bold=True, mono=True)
    draw.text((28, 22), beat.get("title", "POPULATION IMPACT")[:48], fill=(31, 29, 26, 255), font=font_t)
    badge_txt = str(beat.get("badge_text", f"{pct}%"))[:14]
    b_bb = draw.textbbox((0, 0), badge_txt, font=font_p)
    b_tw = b_bb[2] - b_bb[0]
    draw.text((w - 22 - b_tw, 16), badge_txt, fill=(217, 35, 24, 255), font=font_p)

    cols, rows = 20, 5
    gx0, gy0 = 28, 72
    cell_w = (w - 52) // cols
    cell_h = 22
    for idx in range(100):
        r = idx // cols
        c = idx % cols
        cx = gx0 + c * cell_w
        cy = gy0 + r * (cell_h + 6)
        col = (217, 35, 24, 255) if (idx + 1) <= cur_pct else (214, 207, 194, 255)
        draw.rounded_rectangle([cx, cy, cx + cell_w - 5, cy + cell_h], radius=3, fill=col)

    sub_txt = beat.get("sub", beat.get("caption", "EACH BLOCK REPRESENTS 1% OF TOTAL"))
    draw.text((28, h - 32), str(sub_txt)[:78], fill=(60, 55, 48, 255), font=font_s)
    return card


def render_rough_bars(beat, progress=1.0):
    w, h = int(beat.get("w", 640)), int(beat.get("h", 250))
    card = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([10, 12, w + 14, h + 16], radius=5, fill=(0, 0, 0, 95))
    draw.rounded_rectangle([4, 4, w + 8, h + 8], radius=5, fill=(252, 249, 240, 252), outline=(35, 32, 28, 255), width=3)

    font_t = get_font(20, bold=True)
    font_l = get_font(14, bold=True, mono=True)
    draw.text((28, 20), beat.get("title", "COMPARISON")[:48], fill=(31, 29, 26, 255), font=font_t)

    bars = beat.get("bars", [
        {"label": "1867 PURCHASE PRICE", "value_text": "$7.2M", "ratio": 0.14},
        {"label": "RESOURCE VALUE TODAY", "value_text": "$500B+", "ratio": 1.0}
    ])
    cy = 62
    for i, b in enumerate(bars[:3]):
        lbl = b.get("label", "")
        vtxt = b.get("value_text", "")
        r_raw = b.get("ratio", float(b.get("pct", 50)) / 100.0)
        ratio = float(r_raw) * min(1.0, progress * 1.8)
        draw.text((28, cy), f"{lbl}  •  {vtxt}", fill=(35, 32, 28, 255), font=font_l)
        draw.rounded_rectangle([28, cy + 22, w - 24, cy + 50], radius=3, fill=(230, 223, 209, 255))
        bw = max(22, int((w - 52) * ratio))
        bcol = (217, 35, 24, 255) if i == len(bars) - 1 else (74, 107, 130, 255)
        draw.rounded_rectangle([28, cy + 22, 28 + bw, cy + 50], radius=3, fill=bcol)
        cy += 62
    if beat.get("sub"):
        draw.text((28, h - 30), str(beat.get("sub"))[:78], fill=(80, 75, 68, 255), font=font_l)
    return card


def render_handwritten_callout(beat, dark_mode=False):
    w, h = int(beat.get("w", 340)), int(beat.get("h", 110))
    card = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    font_hw = get_font(25, bold=True)
    txt = beat.get("text", beat.get("label", ""))[:58]
    col = (245, 197, 24, 255) if dark_mode else (31, 27, 22, 255)
    draw.text((16, 12), txt, fill=col, font=font_hw)
    draw.line([(w // 2, 52), (w // 2 - 28, 88)], fill=(217, 35, 24, 255), width=4)
    draw.line([(w // 2 - 28, 88), (w // 2 - 14, 84)], fill=(217, 35, 24, 255), width=4)
    draw.line([(w // 2 - 28, 88), (w // 2 - 24, 74)], fill=(217, 35, 24, 255), width=4)
    return card


def render_number_counter(beat, elapsed):
    w, h = int(beat.get("w", 520)), int(beat.get("h", 190))
    card = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([10, 12, w + 14, h + 16], radius=6, fill=(0, 0, 0, 110))
    draw.rounded_rectangle([4, 4, w + 8, h + 8], radius=6, fill=(24, 22, 20, 252), outline=(245, 197, 24, 255), width=3)

    if "target_number" in beat:
        target = float(beat.get("target_number", 100))
        prog = min(1.0, elapsed / 0.85)
        cur_val = int(round(target * (1.0 - math.pow(1.0 - prog, 3))))
        num_str = f"{beat.get('prefix', '')}{cur_val:,}{beat.get('suffix', '')}"
    else:
        num_str = str(beat.get("target_text", "100"))

    font_num = get_font(50, bold=True)
    font_cap = get_font(16, bold=True, mono=True)
    draw.text((28, 38), num_str[:28], fill=(245, 197, 24, 255), font=font_num)
    cap_txt = beat.get("caption") or beat.get("label") or ""
    draw.text((28, 112), cap_txt[:54], fill=(229, 224, 213, 255), font=font_cap)
    rot = float(beat.get("rot", 0.0))
    if abs(rot) > 0.1:
        card = card.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)
    return card


def render_detective_note(beat):
    w, h = int(beat.get("w", 660)), int(beat.get("h", 175))
    card = Image.new("RGBA", (w + 24, h + 28), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([10, 16, w + 14, h + 20], radius=4, fill=(0, 0, 0, 90))
    draw.rounded_rectangle([4, 10, w + 8, h + 14], radius=4, fill=(254, 243, 190, 252), outline=(203, 182, 107, 255), width=2)
    draw.rectangle([w // 2 - 68, 0, w // 2 + 68, 22], fill=(238, 231, 206, 225), outline=(195, 184, 155, 190))

    font_t = get_font(18, bold=True)
    font_b = get_font(17, bold=True, mono=True)
    draw.polygon([(26, 36), (38, 36), (32, 50)], fill=(184, 29, 19, 255))
    draw.ellipse([27, 32, 37, 42], fill=(215, 38, 26, 255))
    draw.text((46, 32), f"{beat.get('title', 'DETECTIVE NOTE')[:48]}", fill=(184, 29, 19, 255), font=font_t)
    lines = textwrap.wrap(beat.get("text", ""), width=54)[:3]
    for idx, ln in enumerate(lines):
        draw.text((26, 68 + idx * 25), ln, fill=(34, 31, 27, 255), font=font_b)
    rot = float(beat.get("rot", 0.0))
    if abs(rot) > 0.1:
        card = card.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)
    return card


def render_svg_arrow(beat):
    w, h = int(beat.get("w", 170)), int(beat.get("h", 85))
    card = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    direction = beat.get("direction", "LEFT_TO_RIGHT")
    y_mid = h // 2 + 10
    draw.line([(16, y_mid), (w - 16, y_mid)], fill=(217, 35, 24, 255), width=6)
    if direction == "RIGHT_TO_LEFT":
        draw.polygon([(12, y_mid), (32, y_mid - 12), (32, y_mid + 12)], fill=(217, 35, 24, 255))
    else:
        draw.polygon([(w - 12, y_mid), (w - 32, y_mid - 12), (w - 32, y_mid + 12)], fill=(217, 35, 24, 255))
    lbl = beat.get("label", "")
    if lbl:
        font_l = get_font(14, bold=True)
        draw.rounded_rectangle([18, 6, w - 10, 32], radius=3, fill=(217, 35, 24, 255))
        draw.text((26, 9), lbl[:22], fill=(255, 255, 255, 255), font=font_l)
    return card


def render_map_pin(beat):
    w, h = int(beat.get("w", 260)), int(beat.get("h", 80))
    card = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.ellipse([8, 18, 44, 54], fill=(217, 35, 24, 90), outline=(217, 35, 24, 255), width=3)
    draw.ellipse([18, 28, 34, 44], fill=(217, 35, 24, 255))
    draw.rounded_rectangle([50, 18, w + 8, 56], radius=4, fill=(20, 20, 20, 240), outline=(245, 197, 24, 255), width=2)
    font_p = get_font(15, bold=True)
    draw.text((60, 27), beat.get("label", "LOCATION")[:28], fill=(245, 197, 24, 255), font=font_p)
    return card


def render_magnifier(beat):
    w, h = int(beat.get("w", 250)), int(beat.get("h", 130))
    card = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.ellipse([10, 10, 96, 96], outline=(245, 197, 24, 255), width=5)
    draw.ellipse([16, 16, 90, 90], outline=(217, 35, 24, 255), width=2)
    draw.rounded_rectangle([85, 34, w + 10, 74], radius=4, fill=(217, 35, 24, 245))
    font_m = get_font(14, bold=True)
    draw.text((95, 45), beat.get("label", "DETAIL")[:24], fill=(255, 255, 255, 255), font=font_m)
    return card


def render_stamp(beat):
    text = beat.get("text", "CONFIRMED")
    font_st = get_font(34, bold=True)
    tmp_im = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    tmp_dr = ImageDraw.Draw(tmp_im)
    bbox = tmp_dr.textbbox((0, 0), text[:32], font=font_st)
    tw = bbox[2] - bbox[0]
    bw = max(int(beat.get("w", 360)), tw + 56)
    bh = max(int(beat.get("h", 96)), 94)
    card = Image.new("RGBA", (bw + 36, bh + 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    if beat.get("radar_ring"):
        draw.rounded_rectangle([3, 3, bw + 25, bh + 25], radius=10, outline=(217, 35, 24, 185), width=3)
    draw.rounded_rectangle([18, 20, bw + 20, bh + 22], radius=6, fill=(0, 0, 0, 75))
    draw.rounded_rectangle([14, 14, bw + 14, bh + 14], radius=6, fill=(250, 246, 235, 238), outline=(184, 29, 19, 245), width=6)
    draw.rounded_rectangle([22, 22, bw + 6, bh + 6], radius=3, outline=(184, 29, 19, 195), width=2)
    tx = 14 + (bw - tw) // 2
    ty = 14 + (bh - (bbox[3] - bbox[1])) // 2 - 4
    draw.text((tx, ty), text[:32], fill=(184, 29, 19, 248), font=font_st)
    rot = float(beat.get("rot", -6.0))
    return card.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)


def render_red_ink_overlay(beat, img_cache):
    w, h = int(beat.get("w", 320)), int(beat.get("h", 170))
    ov_src = beat.get("src", "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/red_ink_circle.png")
    lbl = beat.get("label", "")
    cache_key = ("RED_INK", ov_src, w, h, lbl)
    if cache_key in img_cache:
        return img_cache[cache_key]
    card = Image.new("RGBA", (w + 24, h + 44), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    if os.path.exists(ov_src):
        ov_im = Image.open(ov_src).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
        card.paste(ov_im, (12, 8), ov_im)
    else:
        draw.ellipse([12, 8, 12 + w, 8 + h], outline=(217, 35, 24, 255), width=6)
    if lbl:
        font_l = get_font(15, bold=True)
        bbox = draw.textbbox((0, 0), lbl[:32], font=font_l)
        tw = bbox[2] - bbox[0]
        tag_w = tw + 26
        tx0 = 12 + (w - tag_w) // 2
        ty0 = h - 10
        draw.rounded_rectangle([tx0 + 2, ty0 + 3, tx0 + tag_w + 2, ty0 + 33], radius=3, fill=(0, 0, 0, 110))
        draw.rounded_rectangle([tx0, ty0, tx0 + tag_w, ty0 + 30], radius=3, fill=(184, 29, 19, 255), outline=(255, 255, 255, 255), width=2)
        draw.text((tx0 + 13, ty0 + 5), lbl[:32], fill=(255, 255, 255, 255), font=font_l)
    rot = float(beat.get("rot", 0.0))
    if abs(rot) > 0.1:
        card = card.rotate(-rot, expand=True, resample=Image.Resampling.BICUBIC)
    img_cache[cache_key] = card
    return card


def render_part_mp4(storyboard_path, voice_path, out_mp4_path, max_seconds=None):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    with open(storyboard_path, encoding="utf-8") as f:
        sb = json.load(f)

    duration = float(sb.get("duration", 145.2))
    if max_seconds is not None and max_seconds > 0:
        duration = min(duration, float(max_seconds))

    if not voice_path:
        voice_path = sb.get("voice_path", "1_INPUT_NHAN_SU/cac_phan_da_cat/phan_01/phan_01_voice.mp3")

    sfx_dir = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx"
    os.makedirs(os.path.dirname(os.path.abspath(out_mp4_path)), exist_ok=True)

    print(f"[Pha 5 - MP4 Exporter] Đang trộn âm thanh Master (Voice + SFX) cho {duration:.1f}s...")
    temp_sfx_wav = out_mp4_path + ".sfx_temp.wav"
    temp_master_aac = out_mp4_path + ".master_temp.aac"
    build_sfx_overlay_wav(sb, duration, sfx_dir, temp_sfx_wav)
    mix_voice_and_sfx(ffmpeg_exe, voice_path, temp_sfx_wav, temp_master_aac, duration)

    bg_path = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/textures/paper_texture_hd.jpg"
    if os.path.exists(bg_path):
        base_bg = Image.open(bg_path).convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    else:
        base_bg = Image.new("RGB", (WIDTH, HEIGHT), (234, 226, 208))

    bg_draw = ImageDraw.Draw(base_bg)
    for gx in range(0, WIDTH, 80):
        bg_draw.line([(gx, 0), (gx, HEIGHT)], fill=(215, 206, 188), width=1)
    for gy in range(0, HEIGHT, 80):
        bg_draw.line([(0, gy), (WIDTH, gy)], fill=(215, 206, 188), width=1)

    compass_path = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/compass_rose_vintage.png"
    if os.path.exists(compass_path):
        try:
            comp = Image.open(compass_path).convert("RGBA").resize((240, 240), Image.Resampling.LANCZOS)
            r, g, b, a = comp.split()
            a = a.point(lambda p: int(p * 0.14))
            comp = Image.merge("RGBA", (r, g, b, a))
            base_bg_rgba = base_bg.convert("RGBA")
            base_bg_rgba.paste(comp, (WIDTH - 75 - 240, HEIGHT - 130 - 240), comp)
            base_bg = base_bg_rgba.convert("RGB")
        except Exception:
            pass

    total_frames = int(duration * FPS)
    print(f"[Pha 5 - MP4 Exporter] Đang kết xuất {total_frames} khung hình (1920x1080 @ {FPS}fps) -> {out_mp4_path}")

    cmd = [
        ffmpeg_exe, "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", temp_master_aac,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_mp4_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    img_cache = {}
    font_sub_en = get_font(25, bold=True)
    font_sub_vi = get_font(20, bold=True)
    font_era = get_font(24, bold=True)
    font_src = get_font(13, bold=False, mono=True)
    font_hud_lbl = get_font(11, bold=True, mono=True)
    font_hud_val = get_font(28, bold=True)
    scenes = sb.get("scenes", [])
    subtitles = sb.get("subtitles", [])
    show_subs = bool(sb.get("show_subtitles_on_export", True))

    dark_bg = Image.new("RGB", (WIDTH, HEIGHT), (12, 13, 17))
    dark_draw = ImageDraw.Draw(dark_bg)
    for gx in range(0, WIDTH, 80):
        dark_draw.line([(gx, 0), (gx, HEIGHT)], fill=(26, 29, 38), width=1)
    for gy in range(0, HEIGHT, 80):
        dark_draw.line([(0, gy), (WIDTH, gy)], fill=(26, 29, 38), width=1)

    hud_card_path = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/vox_torn_hud_ticker_card.png"
    hud_card_im = Image.open(hud_card_path).convert("RGBA").resize((310, 86), Image.Resampling.LANCZOS) if os.path.exists(hud_card_path) else None
    torn_div_path = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/vox_torn_paper_vertical_divider.png"
    torn_div_im = Image.open(torn_div_path).convert("RGBA") if os.path.exists(torn_div_path) else None

    for frame_idx in range(total_frames):
        t = frame_idx / float(FPS)

        active_scene = None
        for sc in scenes:
            if float(sc.get("t0", 0)) <= t <= float(sc.get("t1", 9999)):
                active_scene = sc
                break
        if active_scene is None and scenes:
            active_scene = scenes[-1]

        is_dark = False
        if active_scene:
            is_dark = (active_scene.get("bg_mode") == "DARK_CLIMAX") or (
                active_scene.get("dark_climax_from") and t >= float(active_scene.get("dark_climax_from"))
            )

        frame = (dark_bg if is_dark else base_bg).copy().convert("RGBA")
        draw = ImageDraw.Draw(frame)

        if active_scene:
            # 1. Top-Left Era Anchor (Gu 1)
            era_lbl = active_scene.get("era_label")
            if era_lbl:
                ebb = draw.textbbox((0, 0), era_lbl[:64], font=font_era)
                ew = (ebb[2] - ebb[0]) + 32
                ebg = (24, 26, 34, 230) if is_dark else (250, 246, 235, 225)
                ecol = (245, 197, 24, 255) if is_dark else (43, 35, 27, 255)
                draw.rounded_rectangle([56, 34, 56 + ew, 80], radius=3, fill=ebg)
                draw.rectangle([56, 34, 62, 80], fill=(245, 197, 24, 255) if is_dark else (217, 35, 24, 255))
                draw.text((74, 43), era_lbl[:64], fill=ecol, font=font_era)

            # 2. Top-Right Torn-Paper HUD Ticker (Gu 2)
            hud_t = active_scene.get("hud_ticker")
            if isinstance(hud_t, dict) and (hud_t.get("value") or hud_t.get("to") is not None):
                hx, hy = WIDTH - 362, 28
                if hud_card_im is not None:
                    frame.paste(hud_card_im, (hx, hy), hud_card_im)
                else:
                    draw.rounded_rectangle([hx, hy, hx + 310, hy + 86], radius=4, fill=(252, 249, 241, 245))
                val_str = str(hud_t.get("value", ""))
                if not val_str and hud_t.get("to") is not None:
                    sc_t0 = float(active_scene.get("t0", 0.0))
                    sc_t1 = float(active_scene.get("t1", duration))
                    sc_p = max(0.0, min(1.0, ((t - sc_t0) / max(0.1, sc_t1 - sc_t0)) * 1.35))
                    f_val = float(hud_t.get("from", 0))
                    t_val = float(hud_t.get("to", 100))
                    cur_num = int(round(f_val + (t_val - f_val) * (1.0 - math.pow(1.0 - sc_p, 3))))
                    is_year = ("YEAR" in str(hud_t.get("prefix", "")).upper()) or ("YEAR" in str(hud_t.get("label", "")).upper())
                    num_str = str(cur_num) if is_year else f"{cur_num:,}"
                    val_str = f"{hud_t.get('prefix', '')}{num_str}{hud_t.get('suffix', '')}"
                draw.text((hx + 24, hy + 16), str(hud_t.get("label", "KEY METRIC"))[:28], fill=(90, 83, 72, 255), font=font_hud_lbl)
                draw.text((hx + 24, hy + 36), val_str[:22], fill=(20, 20, 20, 255), font=font_hud_val)

            # 3. Bottom-Left Archival Source Footnote (Gu 2)
            src_fn = active_scene.get("source_footnote")
            if src_fn:
                scol = (156, 163, 175, 230) if is_dark else (87, 80, 70, 230)
                draw.text((56, HEIGHT - 28), str(src_fn)[:95], fill=scol, font=font_src)

            for beat in active_scene.get("beats", []):
                bt0 = float(beat.get("t0", 0.0))
                bt1 = float(beat.get("t1", active_scene.get("t1", duration)))
                if t < bt0 or t > bt1:
                    continue

                elapsed = t - bt0
                pop_prog = min(1.0, elapsed / 0.25)
                btype = beat.get("type", "POLAROID")
                bx, by = int(beat.get("x", 100)), int(beat.get("y", 120))
                y_offset = int((1.0 - pop_prog) * 24)

                if btype in ("POLAROID", "VIDEO_CLIP"):
                    card = render_polaroid_card(beat, img_cache, elapsed)
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype == "STICKER":
                    card = render_sticker_card(beat, img_cache)
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype in ("HEADLINE", "KINETIC_TEXT"):
                    card = render_headline_card(beat, min(1.0, elapsed / 0.45), dark_mode=is_dark)
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype == "NUMBER_COUNTER":
                    card = render_number_counter(beat, elapsed)
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype == "DETECTIVE_TAPE_NOTE":
                    card = render_detective_note(beat)
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype in ("RED_INK_CIRCLE", "FOCUS_FRAME"):
                    card = render_red_ink_overlay(beat, img_cache)
                    frame.paste(card, (bx, by), card)
                elif btype == "TORN_PAPER_SPLIT" and torn_div_im is not None:
                    tw_d, th_d = int(beat.get("w", 90)), int(beat.get("h", 1080))
                    dv = torn_div_im.resize((tw_d, th_d), Image.Resampling.LANCZOS)
                    frame.paste(dv, (bx, by), dv)
                    l_tag = beat.get("left_tag", "")
                    r_tag = beat.get("right_tag", "")
                    font_tg = get_font(15, bold=True)
                    if l_tag:
                        lbb = draw.textbbox((0, 0), l_tag[:18], font=font_tg)
                        ltw = (lbb[2] - lbb[0]) + 22
                        draw.rounded_rectangle([bx - ltw - 6, by + 20, bx - 6, by + 50], radius=3, fill=(24, 22, 20, 238), outline=(245, 197, 24, 255), width=2)
                        draw.text((bx - ltw + 5, by + 26), l_tag[:18], fill=(245, 197, 24, 255), font=font_tg)
                    if r_tag:
                        rbb = draw.textbbox((0, 0), r_tag[:18], font=font_tg)
                        rtw = (rbb[2] - rbb[0]) + 22
                        draw.rounded_rectangle([bx + tw_d - 20, by + th_d - 24, bx + tw_d - 20 + rtw, by + th_d + 6], radius=3, fill=(184, 29, 19, 242), outline=(255, 255, 255, 255), width=2)
                        draw.text((bx + tw_d - 9, by + th_d - 18), r_tag[:18], fill=(255, 255, 255, 255), font=font_tg)
                elif btype == "WAFFLE_100_ARRAY":
                    card = render_waffle_array(beat, elapsed / max(0.5, bt1 - bt0))
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype == "ROUGH_EDGE_BARS":
                    card = render_rough_bars(beat, elapsed / max(0.5, bt1 - bt0))
                    frame.paste(card, (bx, by + y_offset), card)
                elif btype == "HANDWRITTEN_CALLOUT":
                    card = render_handwritten_callout(beat, dark_mode=is_dark)
                    frame.paste(card, (bx, by), card)
                elif btype == "SVG_RED_ARROW":
                    card = render_svg_arrow(beat)
                    frame.paste(card, (bx, by), card)
                elif btype == "RED_MAP_PIN":
                    card = render_map_pin(beat)
                    frame.paste(card, (bx, by), card)
                elif btype == "MAGNIFIER_CALLOUT":
                    card = render_magnifier(beat)
                    frame.paste(card, (bx, by), card)
                elif btype == "STAMP":
                    card = render_stamp(beat)
                    frame.paste(card, (bx, by), card)

        if show_subs:
            active_sub = None
            for s in subtitles:
                if float(s.get("t0", 0)) <= t <= float(s.get("t1", 0)):
                    active_sub = s
                    break
            if active_sub:
                en_lines = textwrap.wrap(active_sub.get("en", ""), width=88)[:2]
                vi_lines = textwrap.wrap(active_sub.get("vi", ""), width=102)[:2]
                box_h = 26 + len(en_lines) * 32 + len(vi_lines) * 26
                by0 = HEIGHT - 36 - box_h
                by1 = HEIGHT - 36
                bx0, bx1 = 200, WIDTH - 200
                draw.rounded_rectangle([bx0 + 4, by0 + 6, bx1 + 4, by1 + 6], radius=10, fill=(0, 0, 0, 145))
                draw.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=(12, 14, 18, 232), outline=(245, 197, 24, 190), width=2)
                cy = by0 + 13
                for ln in en_lines:
                    bb = draw.textbbox((0, 0), ln, font=font_sub_en)
                    tw = bb[2] - bb[0]
                    draw.text(((WIDTH - tw) // 2, cy), ln, fill=(255, 255, 255, 255), font=font_sub_en)
                    cy += 32
                cy += 3
                for ln in vi_lines:
                    bb = draw.textbbox((0, 0), ln, font=font_sub_vi)
                    tw = bb[2] - bb[0]
                    draw.text(((WIDTH - tw) // 2, cy), ln, fill=(245, 197, 24, 255), font=font_sub_vi)
                    cy += 26

        prog_w = int((t / max(0.1, duration)) * WIDTH)
        draw.rectangle([0, HEIGHT - 6, WIDTH, HEIGHT], fill=(0, 0, 0, 90))
        draw.rectangle([0, HEIGHT - 6, prog_w, HEIGHT], fill=(184, 29, 19, 255))

        proc.stdin.write(frame.convert("RGB").tobytes())

    proc.stdin.close()
    proc.wait()

    for tmp in (temp_sfx_wav, temp_master_aac):
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass

    print(f"[Hoàn tất Xuất MP4] Video đã lưu tại: {out_mp4_path} ({os.path.getsize(out_mp4_path) / (1024*1024):.2f} MB)")
    return out_mp4_path


def concat_all_parts(parts_dir, full_out_mp4):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    mp4_files = sorted([
        os.path.join(parts_dir, f)
        for f in os.listdir(parts_dir)
        if f.lower().endswith(".mp4")
    ])
    if not mp4_files:
        print("[Cảnh báo] Không tìm thấy file MP4 phần nào trong:", parts_dir)
        return None

    os.makedirs(os.path.dirname(os.path.abspath(full_out_mp4)), exist_ok=True)
    list_txt = full_out_mp4 + ".concat_list.txt"
    with open(list_txt, "w", encoding="utf-8") as f:
        for p in mp4_files:
            abs_p = os.path.abspath(p).replace("\\", "/")
            f.write(f"file '{abs_p}'\n")

    cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", list_txt,
        "-c", "copy",
        full_out_mp4
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(list_txt):
        os.remove(list_txt)
    print(f"[Hoàn tất Ghép nối Toàn tập] Đã nối {len(mp4_files)} phần thành: {full_out_mp4}")
    return full_out_mp4


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pha 5: Kết xuất Bàn dựng 5-Track ra file Video .MP4")
    parser.add_argument("--part", default="phan_01", help="Tên thư mục phần (mặc định: phan_01)")
    parser.add_argument("--chapter", default=None, help="Alias tương thích ngược cho --part")
    parser.add_argument("--storyboard", default=None, help="Đường dẫn file storyboard.json")
    parser.add_argument("--voice", default=None, help="Đường dẫn file voice.mp3")
    parser.add_argument("--output", default=None, help="Đường dẫn file .mp4 đầu ra")
    parser.add_argument("--max-seconds", type=float, default=None, help="Giới hạn số giây xuất thử (tùy chọn)")
    parser.add_argument("--concat-all", action="store_true", help="Ghép nối toàn bộ các phần thành FULL_VIDEO_HOAN_CHINH.mp4")
    args = parser.parse_args()

    part_id = args.chapter or args.part
    if args.concat_all:
        concat_all_parts(
            "3_OUTPUT_VIDEO_HOAN_CHINH/tung_phan_mp4",
            "3_OUTPUT_VIDEO_HOAN_CHINH/video_full_ghep_noi/FULL_VIDEO_HOAN_CHINH.mp4"
        )
    else:
        default_sb = f"2_KHO_NGUYEN_LIEU/theo_tung_phan/{part_id}/chi_dao_phan_canh.json"
        if not os.path.exists(default_sb):
            default_sb = f"2_KHO_NGUYEN_LIEU/theo_tung_phan/{part_id}/storyboard.json"
        sb_path = args.storyboard or default_sb
        out_path = args.output or f"3_OUTPUT_VIDEO_HOAN_CHINH/tung_phan_mp4/{part_id}_final.mp4"
        render_part_mp4(sb_path, args.voice, out_path, max_seconds=args.max_seconds)
