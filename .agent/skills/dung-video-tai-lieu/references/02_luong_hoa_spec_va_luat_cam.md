# Bước 2: Lượng Hóa Tính Từ Thành Con Số (`SPEC.md`) & Danh Sách CẤM Mặc Định (`BANNED`)

> **Chân lý gốc rễ (`spec.md` — HeyGen):** *"Tính từ chính là nơi trú ngụ của vẻ ngoài công nghiệp. Khi bạn viết 'hãy làm cho sinh động, hiện đại, chuyên nghiệp', AI sẽ tự lấp chỗ trống bằng thói quen mặc định của nó — và lần nào kết quả cũng giống hệt nhau. Mỗi tính từ bạn ép thành CON SỐ là một quyết định bạn giành lại từ sự máy móc đó."*

## 1. Bảng Quy Đổi Tính Từ $\rightarrow$ Con Số Bắt Buộc Trong `SPEC.md`

Trước khi thiết kế bất kỳ phân cảnh nào, bắt buộc tạo file `2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/SPEC.md` (theo mẫu `templates/mau_02_spec_thong_so.md`) quy định rõ các con số:

| Tính từ cảm tính (CẤM viết suông) | Phải quy đổi thành Con Số Cụ Thể trong `SPEC.md` |
| :--- | :--- |
| *"Nhịp độ nhanh, sinh động"* | `max_dead_stretch <= 2.8s` (cứ mỗi `2.0s – 2.8s` giọng đọc phải có 1 tư liệu mới Vào/Thoát, bút dạ gạch chữ, hoặc máy quay đổi góc). |
| *"Bố cục rõ ràng, thoáng đãng"* | `max_concurrent <= 3` (tối đa 3 phần tử cùng lúc trên khung `1920x1080`); `hero_fill >= 40%` (vật thể chính chiếm ít nhất 40% chiều rộng hoặc cao). |
| *"Chuyển động mượt mà, có lực"* | Vào cảnh dùng hàm giảm tốc đuôi dài `expo.out` (`0.45s`), thoát cảnh nhanh gọn bằng `70%` thời gian vào (`power3.in`, `0.3s`), lò xo `damping: 0.75`. |
| *"Chuyển cảnh cuốn hút"* | Cắt ngay tại đỉnh vận tốc (`Cut-the-Curve`), kèm độ nhòe chuyển động `motion_blur: 10px` (chữ) và `18px` (khung cảnh lớn). |
| *"Đa dạng, không nhàm chán"* | `mixed_media_ratio >= 40%` (ít nhất 40% tổng số nhịp là `VIDEO_CLIP` quay thật, `STICKER` tách nền, Bản đồ hoặc Biểu đồ động); 2 cảnh liền kề cấm trùng `scene_motif`. |
| *"Chữ dễ đọc trên cả điện thoại"* | Cỡ chữ tối thiểu `>= 28px` (2.6% cạnh ngắn màn hình), tối đa `6–8 từ/dòng`, thời gian giữ chữ trên màn hình `= 0.5s + 0.3s × số_từ`. |

## 2. Danh Sách CẤM Mặc Định (`BANNED BY DEFAULT` — Tư duy ngược Charlie Munger)

Mọi file `SPEC.md` đều phải liệt kê và khóa cứng 8 lệnh cấm sau để triệt tiêu "vẻ ngoài do AI tạo":
1. **CẤM Đồng phục Bố cục Trái – Phải:** Cấm đặt Ảnh Polaroid bên trái + Hộp chữ bên phải lặp lại ở 2 cảnh liên tiếp.
2. **CẤM Đứng hình chờ giọng đọc (`dead_stretch > 2.8s`):** Hiệu ứng chạy xong ở giây thứ 2 mà câu thoại dài 12 giây thì bắt buộc phải chia thành 4 nhịp tư liệu con (`XX.1`, `XX.2`, `XX.3`, `XX.4`).
3. **CẤM Mọi phần tử cùng mờ dần và trượt lên (`Fade + Slide-Up Cliché`):** Phải đa dạng hóa cách xuất hiện (bút dạ quét ngang, máy chữ gõ ký tự, con dấu đập từ trên xuống, vết giấy xé mở khung, máy quay lia tới).
4. **CẤM Lắc lư giả tạo tại chỗ (`Idle Sine Wobble`):** Khi ảnh/chữ đã đáp xuống mặt bàn là phải đứng đầm chắc; cấm cho nhấp nhô lên xuống để câu giờ.
5. **CẤM Cắt cảnh chết đà (`Dead Cut / Crossfade`):** Không bao giờ dùng mờ dần (crossfade) giữa 2 cảnh hoặc đợi cảnh cũ đứng im rồi mới cắt.
6. **CẤM Hộp nhỏ trôi giữa nền trống:** Không bao giờ đặt 1 bức ảnh nhỏ xíu chiếm `< 25%` diện tích giữa màn hình trống.
7. **CẤM Nhãn kỹ thuật trên màn hình phim:** Tuyệt đối không in `[SC_01]`, `[STT_01]` lên khung hình `1920x1080`.
8. **CẤM Tích tụ thành đống tạp nham cuối cảnh:** Phần tử của vế câu trước phải thoát (`t1 < t0_moi`) trước khi phần tử của vế câu sau xuất hiện ở cùng vùng bố cục.
