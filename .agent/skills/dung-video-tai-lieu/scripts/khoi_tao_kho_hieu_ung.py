"""
TẢI & KHỞI TẠO KHO HIỆU ỨNG ĐỒ HỌA PNG/SVG TRONG SUỐT & BỘ ÂM THANH FOLEY ĐIỆN ẢNH
Lưu vĩnh viễn vào:
1. 2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/
2. 2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx/
3. Đồng bộ bản sao vào .agent/skills/dung-video-tai-lieu/assets/
"""
import os
import sys
import math

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)
import wave
import struct
import random
import shutil
import urllib.request
from PIL import Image, ImageDraw, ImageFilter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FX_DIR = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays"
SFX_DIR = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx"
SKILL_ASSETS_DIR = ".agent/skills/dung-video-tai-lieu/assets"

os.makedirs(FX_DIR, exist_ok=True)
os.makedirs(SFX_DIR, exist_ok=True)
os.makedirs(os.path.join(SKILL_ASSETS_DIR, "fx_overlays"), exist_ok=True)
os.makedirs(os.path.join(SKILL_ASSETS_DIR, "sfx"), exist_ok=True)

USER_AGENT = "SuDeHieuDocumentaryBot/1.0 (https://sudehieu.vn; contact@sudehieu.vn) Python/3.12"


def download_wikimedia_overlay(url, out_path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(out_path, "wb") as f:
            f.write(data)
        return True
    except Exception as e:
        print(f"  [!] Không tải được {url}: {e}")
        return False


def build_high_res_fx_overlays():
    """Tạo & tải bộ 8 lớp phủ đồ họa PNG Alpha trong suốt độ phân giải cao cho Documentary."""
    # 1. Tải La bàn hàng hải cổ (Vintage Compass Rose PNG từ Wikimedia Commons)
    compass_path = os.path.join(FX_DIR, "compass_rose_vintage.png")
    if not os.path.exists(compass_path):
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Compass_rose_pale.svg/512px-Compass_rose_pale.svg.png"
        if not download_wikimedia_overlay(url, compass_path):
            # Fallback vẽ la bàn cổ chất lượng cao
            im = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
            d = ImageDraw.Draw(im)
            d.ellipse([20, 20, 380, 380], outline=(90, 70, 45, 160), width=4)
            d.ellipse([40, 40, 360, 360], outline=(90, 70, 45, 110), width=2)
            d.polygon([(200, 15), (225, 175), (200, 155), (175, 175)], fill=(184, 29, 19, 190))
            d.polygon([(200, 385), (220, 225), (180, 225)], fill=(70, 55, 40, 170))
            im.save(compass_path)

    # 2. Vòng khoanh bút lông đỏ vẽ tay (Hand-Drawn Red Ink Circle PNG)
    circle_path = os.path.join(FX_DIR, "red_ink_circle.png")
    im = Image.new("RGBA", (500, 320), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pts = []
    cx, cy, rx, ry = 250, 160, 210, 115
    for deg in range(0, 395, 4):
        rad = math.radians(deg)
        wobble_r = math.sin(rad * 3.0) * 6.0 + math.cos(rad * 5.0) * 4.0
        spiral = (deg / 395.0) * 10.0
        x = cx + (rx + wobble_r - spiral) * math.cos(rad)
        y = cy + (ry + wobble_r * 0.6 - spiral * 0.5) * math.sin(rad)
        pts.append((x, y))
    d.line(pts, fill=(210, 28, 20, 240), width=8, joint="curve")
    d.line([(x + 1, y + 2) for (x, y) in pts[:70]], fill=(160, 15, 10, 180), width=5)
    im.save(circle_path)

    # 3. Vệt cọ gạch chân mực đỏ (Red Brush Underline PNG)
    underline_path = os.path.join(FX_DIR, "red_brush_underline.png")
    im = Image.new("RGBA", (600, 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pts = []
    for x in range(20, 580, 8):
        y = 32 + math.sin(x / 90.0) * 5.0
        pts.append((x, y))
    d.line(pts, fill=(212, 30, 22, 245), width=10)
    d.line([(x, y + 7) for (x, y) in pts[5:-15]], fill=(212, 30, 22, 165), width=4)
    im.save(underline_path)

    # 4. Băng dính giấy hồ sơ thật (Realistic Torn Masking Tape PNG)
    tape_path = os.path.join(FX_DIR, "masking_tape_strip.png")
    im = Image.new("RGBA", (280, 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    poly = [(14, 12), (266, 10), (262, 24), (268, 36), (260, 48), (265, 58),
            (16, 60), (20, 46), (12, 34), (19, 22)]
    d.polygon(poly, fill=(238, 229, 198, 215), outline=(195, 182, 145, 180))
    im.save(tape_path)

    # 5. Con dấu sáp đỏ Hoàng gia (Imperial Wax Seal PNG)
    seal_path = os.path.join(FX_DIR, "imperial_wax_seal.png")
    im = Image.new("RGBA", (220, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([16, 18, 206, 208], fill=(0, 0, 0, 90))
    d.ellipse([12, 12, 200, 200], fill=(165, 22, 18, 250), outline=(110, 12, 10, 255), width=5)
    d.ellipse([28, 28, 184, 184], fill=(185, 28, 22, 255), outline=(235, 185, 90, 200), width=3)
    d.ellipse([42, 42, 170, 170], outline=(120, 15, 12, 220), width=2)
    im.save(seal_path)

    # 6. Khung ngắm ống nhòm / tiêu điểm cổ điển (Archival Viewfinder Crosshair PNG)
    reticle_path = os.path.join(FX_DIR, "archival_focus_frame.png")
    im = Image.new("RGBA", (500, 360), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = (245, 197, 24, 235)
    w_len = 48
    # 4 góc chữ L
    d.line([(12, 60), (12, 12), (60, 12)], fill=c, width=6)
    d.line([(440, 12), (488, 12), (488, 60)], fill=c, width=6)
    d.line([(12, 300), (12, 348), (60, 348)], fill=c, width=6)
    d.line([(440, 348), (488, 348), (488, 300)], fill=c, width=6)
    im.save(reticle_path)

    print(f"✅ Đã tạo & tải xong bộ 6 lớp phủ đồ họa PNG Alpha tại: {FX_DIR}")


def save_wav(path, samples, sr=44100):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        clamped = [max(-32767, min(32767, int(s * 32767))) for s in samples]
        wf.writeframes(struct.pack(f"<{len(clamped)}h", *clamped))


def build_natural_foley_sfx():
    """Tạo bộ 8 âm thanh Foley điện ảnh ấm, trầm, tự nhiên (không chói tai, không ồn)."""
    sr = 44100
    random.seed(42)

    # 1. paper_slide.wav — Tiếng đặt hồ sơ giấy êm và ấm (Filtered Low-Pass Velvet Rustle)
    dur = 0.28
    n = int(sr * dur)
    samples = []
    prev = 0.0
    for i in range(n):
        t = i / sr
        env = math.sin(math.pi * (t / dur)) ** 1.8
        raw = random.uniform(-1, 1)
        filt = prev * 0.88 + raw * 0.12
        prev = filt
        thud = math.exp(-t * 32) * math.sin(2 * math.pi * 85 * t) * 0.35
        samples.append((filt * env * 0.45 + thud) * 0.7)
    save_wav(os.path.join(SFX_DIR, "paper_slide.wav"), samples, sr)

    # 2. marker_swipe.wav — Tiếng bút lông lướt nhẹ trên giấy
    dur = 0.22
    n = int(sr * dur)
    samples = []
    prev = 0.0
    for i in range(n):
        t = i / sr
        env = math.sin(math.pi * (t / dur)) ** 1.5
        raw = random.uniform(-1, 1)
        filt = prev * 0.78 + raw * 0.22
        prev = filt
        samples.append(filt * env * 0.28)
    save_wav(os.path.join(SFX_DIR, "marker_swipe.wav"), samples, sr)

    # 3. rubber_stamp.wav — Tiếng đóng dấu gỗ trầm chắc
    dur = 0.26
    n = int(sr * dur)
    samples = []
    for i in range(n):
        t = i / sr
        env = math.exp(-t * 24)
        body = math.sin(2 * math.pi * 68 * t) * 0.65 + math.sin(2 * math.pi * 135 * t) * 0.25
        click = (random.uniform(-1, 1) * math.exp(-t * 90)) * 0.25
        samples.append((body + click) * env * 0.75)
    save_wav(os.path.join(SFX_DIR, "rubber_stamp.wav"), samples, sr)

    # 4. map_whoosh.wav — Tiếng chuyển cảnh gió trầm điện ảnh (Deep Warm Cinematic Whoosh)
    dur = 0.42
    n = int(sr * dur)
    samples = []
    prev = 0.0
    for i in range(n):
        t = i / sr
        env = math.sin(math.pi * (t / dur)) ** 2.2
        raw = random.uniform(-1, 1)
        filt = prev * 0.93 + raw * 0.07
        prev = filt
        sub = math.sin(2 * math.pi * (55 + 40 * math.sin(math.pi * t / dur)) * t) * 0.25
        samples.append((filt * 0.6 + sub) * env * 0.7)
    save_wav(os.path.join(SFX_DIR, "map_whoosh.wav"), samples, sr)

    # 5. typewriter.wav — Tiếng nhảy số / tích tắc cơ học nhẹ nhàng
    dur = 0.18
    n = int(sr * dur)
    samples = []
    for i in range(n):
        t = i / sr
        pulse1 = math.exp(-t * 85) * math.sin(2 * math.pi * 420 * t) * 0.4
        pulse2 = math.exp(-max(0, t - 0.07) * 85) * math.sin(2 * math.pi * 520 * max(0, t - 0.07)) * 0.35 if t > 0.07 else 0.0
        samples.append((pulse1 + pulse2) * 0.65)
    save_wav(os.path.join(SFX_DIR, "typewriter.wav"), samples, sr)

    # 6. low_boom.wav — Tiếng trống trầm lịch sử (Cinematic Sub Impact)
    dur = 0.75
    n = int(sr * dur)
    samples = []
    for i in range(n):
        t = i / sr
        env = math.exp(-t * 5.5)
        freq = 58.0 * math.exp(-t * 1.2) + 32.0
        val = math.sin(2 * math.pi * freq * t) * env * 0.75
        samples.append(val)
    save_wav(os.path.join(SFX_DIR, "low_boom.wav"), samples, sr)

    print(f"✅ Đã nâng cấp bộ 6 âm thanh Foley điện ảnh trầm ấm tại: {SFX_DIR}")


if __name__ == "__main__":
    build_high_res_fx_overlays()
    build_natural_foley_sfx()
    # Đồng bộ sang thư mục Skill
    for f in os.listdir(FX_DIR):
        shutil.copy2(os.path.join(FX_DIR, f), os.path.join(SKILL_ASSETS_DIR, "fx_overlays", f))
    for f in os.listdir(SFX_DIR):
        shutil.copy2(os.path.join(SFX_DIR, f), os.path.join(SKILL_ASSETS_DIR, "sfx", f))
    print("✅ Đã đồng bộ toàn bộ Kho Hiệu Ứng vào .agent/skills/dung-video-tai-lieu/assets/")
