# Bước 1: Đọc Vị Nguyên Liệu, Cắt Nhỏ Theo Mạch Ý Nghĩa & Xuất `BRIEF.md` / `STORYLINES.md`

> **Đọc file này khi:** Bắt đầu dự án mới hoặc bắt đầu một Phần mới chưa có `BRIEF.md`.

## 1. Cắt Kịch Bản & Voice Dài (10–45 Phút) Theo Mạch Ý Nghĩa
- Không bao giờ xử lý một cục kịch bản dài 10–45 phút trong 1 lượt.
- Chạy `python .agent/skills/dung-video-tai-lieu/scripts/buoc_1_cat_kich_ban_va_brief.py <voice> <script> <out_dir>` để:
  1. Đồng bộ mặt chữ với giọng đọc bằng `Faster-Whisper` (`word_timestamps=True`).
  2. Tìm điểm ngắt đoạn văn tự nhiên (`1.5 – 3.0 phút/phần`) kèm khoảng lặng âm thanh (`>= 0.35s`) để không bao giờ cắt ngang chữ.
  3. Lưu từng phần vào `1_INPUT_NHAN_SU/cac_phan_da_cat/phan_01/`, `phan_02/`...

## 2. Xác Định "Xương Sống Câu Chuyện" (The One Thing — Học từ `story.md` của HeyGen)
Trước khi lên phân cảnh cho `phan_XX`, bắt buộc trả lời 3 câu hỏi gốc rễ vào `BRIEF.md`:
1. **Một luận điểm duy nhất cần nhớ (The One Thing):** Khán giả xem xong 2 phút của phần này sẽ nhớ câu nói hay sự thật chấn động nào?
2. **Vật dẫn đường xuyên suốt (The Spine / Carrier):** Con số hay vật thể thực tế nào (VD: *Tờ ngân phiếu $7.2M*, *Thùng dầu Standard Oil*, *Bản đồ eo biển Bering*) sẽ đi xuyên từ câu mở đầu (Hook) tới cú chốt (Payoff)?
3. **3 Phương Án Tuyến Truyện (`STORYLINES.md`):** Phác thảo ngắn gọn 3 hướng dàn dựng khác hẳn nhau về **Thế giới thị giác (World)** và **Hình thái máy quay (Form)**:
   - *Phương án A (Bàn Điều Tra Lịch Sử & Hồ Sơ Mật)*
   - *Phương án B (Báo Chí Dữ Liệu Vox & Đồ Họa Tương Phản Cao)*
   - *Phương án C (Sa Bàn Bản Đồ Địa Chính Trị 2.5D & Băng Tư Liệu Thật)*
   - Đề xuất phương án tối ưu nhất lên đầu và ghi vào `2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/BRIEF.md` theo khuôn mẫu `templates/mau_01_brief_va_storylines.md`.

## 3. Quy Tắc "Định Tuyến 1 Lần Rồi Rút Lui" (Route Once, Then Leave)
- Sau khi người dùng duyệt **CỔNG DỪNG 1** và chốt `BRIEF.md`, ở mọi lượt làm việc tiếp theo, AI chỉ đọc `BRIEF.md` mà không bao giờ mở lại bước phỏng vấn này nữa.
