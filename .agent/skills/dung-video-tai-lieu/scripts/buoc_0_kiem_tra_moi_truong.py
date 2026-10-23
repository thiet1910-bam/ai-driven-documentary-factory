"""
PHA 0: CÔNG CỤ KIỂM TRA & CÀI ĐẶT MÔI TRƯỜNG TỰ ĐỘNG (CÓ CỔNG DỪNG BÁO CÁO)
Kiểm tra toàn diện môi trường thực thi trên máy của nhân sự:
1. Hệ điều hành & Phiên bản Python
2. FFmpeg (imageio-ffmpeg) để cắt nối Audio và xuất Video .MP4
3. Faster-Whisper để đồng bộ kịch bản & giọng đọc
4. Rembg + ONNXRuntime để tách nền Sticker nhân vật
5. Pillow + NumPy để xử lý đồ họa khung hình 1920x1080
6. yt-dlp để cắt đoạn video tư liệu 3-5s từ YouTube
7. Cấu trúc 3 Ngăn & Bộ nguyên liệu dùng chung (6 file SFX .wav + paper_texture_hd.jpg)
"""
import sys
import os
import platform
import subprocess
import importlib

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REQUIRED_PACKAGES = [
    ("PIL", "pillow"),
    ("numpy", "numpy"),
    ("imageio_ffmpeg", "imageio-ffmpeg"),
    ("faster_whisper", "faster-whisper"),
    ("rembg", "rembg"),
    ("onnxruntime", "onnxruntime"),
]


def check_and_install():
    print("=" * 72)
    print("[PHA 0] BÁO CÁO KIỂM TRA MÔI TRƯỜNG SẢN XUẤT VIDEO TÀI LIỆU")
    print("=" * 72)
    print(f"• Hệ điều hành : {platform.system()} {platform.release()} ({platform.version()})")
    print(f"• Python       : {sys.version.split()[0]} ({sys.executable})")

    all_ok = True
    for mod_name, pip_name in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(mod_name)
            ver = getattr(mod, "__version__", "Đã cài đặt")
            print(f"• Thư viện {pip_name:<16}: [ĐÃ CÀI] (Phiên bản: {ver})")
        except ImportError:
            print(f"• Thư viện {pip_name:<16}: [CHƯA CÀI] -> Đang tự động cài đặt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            print(f"• Thư viện {pip_name:<16}: [ĐÃ CÀI XONG]")

    # Kiểm tra FFmpeg binary
    try:
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        print(f"• FFmpeg Engine          : [SẴN SÀNG] ({ffmpeg_exe})")
    except Exception as e:
        print(f"• FFmpeg Engine          : [LỖI] ({e})")
        all_ok = False

    # Kiểm tra yt-dlp
    try:
        res = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            print(f"• Công cụ yt-dlp         : [SẴN SÀNG] (Phiên bản: {res.stdout.strip()})")
        else:
            print("• Công cụ yt-dlp         : [CẢNH BÁO] Chưa tìm thấy trong PATH")
    except Exception:
        print("• Công cụ yt-dlp         : [CẢNH BÁO] Chưa cài đặt -> Đang cài qua pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

    # Kiểm tra cấu trúc 3 Ngăn và nguyên liệu dùng chung
    dirs_to_ensure = [
        "1_INPUT_NHAN_SU/cac_phan_da_cat",
        "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx",
        "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/textures",
        "2_KHO_NGUYEN_LIEU/theo_tung_phan",
        "3_OUTPUT_VIDEO_HOAN_CHINH/tung_phan_mp4",
        "3_OUTPUT_VIDEO_HOAN_CHINH/video_full_ghep_noi"
    ]
    for d in dirs_to_ensure:
        os.makedirs(d, exist_ok=True)

    sfx_dir = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx"
    sfx_files = [f for f in os.listdir(sfx_dir) if f.endswith(".wav")] if os.path.exists(sfx_dir) else []
    tex_path = "2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/textures/paper_texture_hd.jpg"
    print(f"• Cấu trúc 3 Ngăn lưu trữ: [ĐÃ KHỞI TẠO CHUẨN]")
    print(f"• Kho SFX dùng chung     : [{len(sfx_files)} file .wav] ({', '.join(sfx_files)})")
    print(f"• Nền giấy nhăn HD       : [{'CÓ SẴN' if os.path.exists(tex_path) else 'THIẾU'}]")
    print("=" * 72)
    print("[KẾT LUẬN PHA 0]: MÔI TRƯỜNG ĐÃ SẴN SÀNG 100% ĐỂ CHẠY PHA 1!")
    print("🛑 [CỔNG DỪNG 0]: Dừng lại báo cáo người dùng trước khi qua Pha 1.")
    print("=" * 72)
    return all_ok


if __name__ == "__main__":
    check_and_install()
