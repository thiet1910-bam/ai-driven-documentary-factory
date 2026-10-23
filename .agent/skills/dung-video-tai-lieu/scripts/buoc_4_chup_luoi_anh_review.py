"""
PHA 4 (BƯỚC BẮT BUỘC CHỐNG QUAN LIÊU): ĐẠO DIỄN AI TỰ MỞ BROWSER XEM TOÀN BỘ CÁC CẢNH (100% SCENES)
& LẬP BIÊN BẢN PHẢN HỒI CHO EDITOR ĐIỀU CHỈNH TRƯỚC KHI TRÌNH NGƯỜI DÙNG.

Cơ chế hoạt động:
1. Tự động đọc `storyboard.json` của Phần hiện tại (`phan_XX`).
2. Với MỌI CẢNH (từ `sc_01` đến cảnh cuối cùng, không bỏ sót cảnh nào!), tự động tính toán
   2 mốc thời gian kiểm tra hiểm hóc nhất:
   - Mốc Giữa Cảnh (Nửa đầu): Kiểm tra bố cục Tư liệu chính + Nhịp hiệu ứng đầu tiên.
   - Mốc Cuối Cảnh (Nửa sau): Kiểm tra xem hiệu ứng cũ đã thoát sạch chưa, có bị đè chữ/tạp nham không.
3. Mở trình duyệt Chrome/Edge thực tế chụp toàn bộ khung hình `1920x1080` của tất cả các cảnh + Giao diện 5-Track Timeline.
4. Bắt buộc Đạo diễn AI dùng `read_file` mở xem bằng mắt toàn bộ các ảnh chụp này, lập Biên bản bắt lỗi Editor
   và yêu cầu Editor sửa ngay trên `storyboard.json` trước khi mở Cổng Dừng 4!
"""
import os
import sys
import json
import subprocess

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if os.path.isdir(_PROJECT_ROOT) and os.path.exists(os.path.join(_PROJECT_ROOT, "index.html")):
    os.chdir(_PROJECT_ROOT)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def get_browser_exe():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None


def capture_all_scenes_for_director(part_id="phan_01", port=8088):
    browser = get_browser_exe()
    if not browser:
        print("[!] Không tìm thấy trình duyệt Chrome/Edge để Đạo diễn mở xem video.")
        sys.exit(1)

    sb_path = f"2_KHO_NGUYEN_LIEU/theo_tung_phan/{part_id}/chi_dao_phan_canh.json"
    legacy_sb_path = f"2_KHO_NGUYEN_LIEU/theo_tung_phan/{part_id}/storyboard.json"
    if os.path.exists(sb_path):
        import shutil
        shutil.copyfile(sb_path, legacy_sb_path)
    elif os.path.exists(legacy_sb_path):
        sb_path = legacy_sb_path
    else:
        print(f"[!] Không tìm thấy file chỉ đạo phân cảnh: {sb_path}")
        sys.exit(1)

    with open(sb_path, encoding="utf-8") as f:
        sb = json.load(f)

    # Tự động bật local HTTP server tạm thời nếu cổng chưa mở
    import socket, threading, http.server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    is_open = (sock.connect_ex(("127.0.0.1", port)) == 0)
    sock.close()
    httpd = None
    if not is_open:
        handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(*args, directory=os.getcwd(), **kwargs)
        httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()

    out_dir = os.path.abspath(f"2_KHO_NGUYEN_LIEU/theo_tung_phan/{part_id}/director_review_frames")
    os.makedirs(out_dir, exist_ok=True)

    checkpoints = []
    for sc in sb.get("scenes", []):
        sc_id = sc.get("id", "sc")
        t0 = float(sc.get("t0", 0.0))
        t1 = float(sc.get("t1", 10.0))
        dur = t1 - t0
        t_mid = round(t0 + dur * 0.30, 1)
        t_end = round(t1 - 1.2, 1)
        checkpoints.append((f"director_{sc_id}_A_{str(t_mid).replace('.','s')}.png", f"http://localhost:{port}/index.html?part={part_id}&t={t_mid}&clean=1", f"{sc_id} (Nửa đầu @ {t_mid}s)"))
        checkpoints.append((f"director_{sc_id}_B_{str(t_end).replace('.','s')}.png", f"http://localhost:{port}/index.html?part={part_id}&t={t_end}&clean=1", f"{sc_id} (Cuối cảnh @ {t_end}s)"))

    checkpoints.append(("director_studio_5track_overview.png", f"http://localhost:{port}/index.html?part={part_id}&t=20.5", "Giao diện Bàn dựng 5-Track NLE tổng thể"))

    print("=" * 88)
    print(f"🎬 [ĐẠO DIỄN AI KIỂM DUYỆT BẰNG BROWSER] ĐANG MỞ XEM 100% CÁC CẢNH CỦA {part_id.upper()} ({len(checkpoints)} KHUNG HÌNH)")
    print("=" * 88)

    for fname, url, desc in checkpoints:
        out_path = os.path.join(out_dir, fname)
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1920,1080",
            "--virtual-time-budget=2500",
            f"--screenshot={out_path}",
            url,
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(out_path):
            size_kb = os.path.getsize(out_path) / 1024.0
            print(f"  👁️ [Đã mở Browser chụp {desc}]: {out_path} ({size_kb:.1f} KB)")
        else:
            print(f"  ❌ [Lỗi chụp {desc}]: {fname}")

    print("=" * 88)
    print("🚨 QUY TẮC CHỐNG QUAN LIÊU (ZERO RUBBER-STAMP RULE):")
    print("1. Đạo diễn AI BẮT BUỘC dùng `read_file` mở xem bằng mắt TẤT CẢ các cảnh vừa chụp ở trên.")
    print("2. Đạo diễn AI phải viết [BIÊN BẢN PHẢN HỒI ĐẠO DIỄN -> EDITOR] chỉ rõ các điểm chưa tối ưu.")
    print("3. Editor AI phải sửa ngay trong `storyboard.json` và chụp lại xác nhận trước khi mở CỔNG DỪNG 4!")
    print("=" * 88)


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "phan_01"
    capture_all_scenes_for_director(part)
