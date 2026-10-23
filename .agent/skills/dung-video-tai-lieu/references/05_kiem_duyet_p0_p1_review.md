# Bước 5: Kiểm Toán Tự Động, Chụp Lưới Ảnh Browser & Lập Biên Bản `REVIEW.md` (P0 / P1 / P2)

> **Tư duy Đạo diễn Khắt khe (Ray Dalio & `review.md` của HeyGen):** *"Bạn là người viết ra timeline nên bạn biết chuyện gì xảy ra; nhưng người xem chỉ nhìn thấy nó 1 lần ở tốc độ thực. Hãy soi bộ phim như một Đạo diễn khó tính đi bắt lỗi, không phải một tác giả tự hào. Không bao giờ tự chấm điểm 10/10 — điểm số không giúp tìm ra lỗi để sửa."*

## 1. Đo Bằng Số Trước, Nhìn Bằng Mắt Sau (Measure, Then Look)
1. **Chạy Máy Kiểm Toán Số Học & Chống Công Nghiệp:**
   ```bash
   python .agent/skills/dung-video-tai-lieu/scripts/buoc_3_kiem_toan_nhip_va_vet_cat.py <chi_dao_phan_canh_json>
   ```
   - Máy tự động kiểm tra 8 chốt chặn: tồn tại file vật lý theo mã `STT`, tràn khung `1920x1080`, đè chồng bố cục (`> 8%`), trần `max_concurrent <= 3`, **lặp mô-típ liên tiếp (`no_motif_repeat`)**, **khoảng chết đứng hình (`dead_stretch > 4.8s`)**, **độ đa dạng chất liệu động (`mixed_media_ratio`)**, và tính hợp lệ của `ledger.json`.
   - Mọi lỗi **P0** do máy báo phải được sửa về `0` trước khi chụp ảnh.

2. **Chạy Máy Chụp Lưới Ảnh Thật Từ Trình Duyệt (Browser Snapshot):**
   ```bash
   python .agent/skills/dung-video-tai-lieu/scripts/buoc_4_chup_luoi_anh_review.py <phan_XX>
   ```
   - Mở trình duyệt Chrome thật (`1920x1080`) chụp toàn bộ các phân cảnh ở **Nửa đầu (`_A_`)** và **Nửa cuối (`_B_`)** cùng ảnh tổng thể **Bàn dựng 5-Track (`director_studio_5track_overview.png`)**.
   - Dùng `read_file` mở xem trực tiếp từng bức ảnh vừa chụp.

## 2. Bảng 6 Câu Hỏi Bắt Lỗi Thị Giác (Khi Soi Bằng `read_file`)

| Câu hỏi soi lỗi | Lỗi cần bắt sống |
| :--- | :--- |
| **1. Có nhìn ra ngay vật thể là gì không?** | Ảnh bị cắt mất đầu nhân vật lịch sử, Sticker tách nền còn dính mảng rác đen/trắng ở góc, chữ đè lên mặt nhân vật. |
| **2. Chủ thể có tách biệt khỏi nền không?** | Hai hộp chữ tranh chấp tiêu điểm, hoặc vật thể chính quá nhỏ (`< 40%` khung hình) trôi lạc lõng. |
| **3. Bố cục giữa `_A_` (Đầu cảnh) và `_B_` (Cuối cảnh) có biến đổi thật không?** | Nếu ảnh `_A_` và ảnh `_B_` giống hệt nhau $\rightarrow$ Vi phạm lỗi đứng hình chờ giọng đọc (`Dead Hold`). |
| **4. Cuối cảnh (`_B_`) có bị đọng rác không?** | Các thẻ của vế câu đầu chưa thoát đi làm chồng đống lên thẻ của vế câu cuối. |
| **5. Có dấu hiệu "Video do AI tạo" (AI Tells) không?** | Lặp lại kiểu đặt Ảnh bên trái + Chữ bên phải ở nhiều cảnh liên tiếp; xuất hiện nhãn kỹ thuật `[SC_01]` trên màn hình phim. |
| **6. Tắt tiếng chỉ nhìn hình có hiểu câu chuyện không?** | Nhìn chuỗi ảnh từ `sc_01 -> sc_XX` mà không đọc phụ đề, người lạ có hiểu diễn biến nhân quả không? |

## 3. Ghi Biên Bản `REVIEW.md` Theo Chuẩn P0 / P1 / P2
Mỗi lỗi phát hiện được phải ghi thành 1 dòng định vị chính xác tới từng giây trong file `2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/REVIEW.md` (theo mẫu `templates/mau_04_bien_ban_kiem_duyet_review.md`):
- `t=34.8s · sc_02 · [Mô tả lỗi] → [Cách sửa chính xác] · [Trạng thái: ĐÃ SỬA]`
- Phân hạng:
  - **🔴 P0 (Lỗi Chí Tử):** Đè chữ, mất mặt nhân vật, thiếu file, lặp mô-típ công nghiệp, lọt mã kỹ thuật lên màn hình $\rightarrow$ **Bắt buộc sửa sạch 100% và chụp lại xác minh trước khi mở Cổng Dừng.**
  - **🟡 P1 (Lỗi Làm Yếu Phim):** Khoảng chờ hơi dài (`> 3.5s`), điểm cắt chưa đủ mượt, thiếu điểm nhấn khoanh mực đỏ $\rightarrow$ **Sửa ngay những điểm quan trọng.**
  - **🟢 P2 (Tinh chỉnh nhỏ):** Căn chỉnh thẩm mỹ phụ.
- Bắt buộc chỉ rõ: **"Phân cảnh nào hiện tại đang là cảnh yếu nhất trong toàn bộ phần này, và đã được gia cố như thế nào?"**

## 4. Kết Xuất `.MP4` & Hậu Kiểm Sau Render (`buoc_5_xuat_video_mp4.py`)
Khi người dùng đã duyệt Bàn dựng HTML (`http://localhost:8088/index.html`) và `REVIEW.md`:
1. Chạy `python .agent/skills/dung-video-tai-lieu/scripts/buoc_5_xuat_video_mp4.py --part <phan_XX>` để xuất file `3_OUTPUT_VIDEO_HOAN_CHINH/tung_phan_mp4/<phan_XX>_final.mp4`.
2. Trích xuất 4–6 khung hình thực tế từ chính file `.mp4` vừa xuất và mở xem bằng `read_file` để xác nhận khớp 100% với Bàn dựng HTML.
