# BIÊN BẢN ĐẠO DIỄN KIỂM TOÁN & HẬU KIỂM (`REVIEW.md`)

- **Mã phần dự án:** `phan_03` (`00:04:41.5 -> 00:07:12.2`, thời lượng `150.73s`)
- **Kết quả chạy `buoc_3_kiem_toan_nhip_va_vet_cat.py`:**
  - Số lỗi P0 (Đè chữ / Tràn khung / Lặp Mô-típ / Thiếu file): `0` lỗi `[📊]`
  - Số cảnh báo P1 (Nhịp điệu): `0` cảnh báo `[📊]`
  - Tổng số cảnh lớn (`Scenes`): `8` cảnh (`sc_01` -> `sc_08`) `[📊]`
  - Tổng số nhịp (`Enter-Hold-Exit Beats`): `47` nhịp (`3.21s / nhịp`) `[📊]`
  - Khoảng giữ nhịp dài nhất (`Max Hold Stretch`): `4.00s` (Chuẩn `<= 4.50s`) `[📊]`
  - Tỷ lệ Chất liệu Động (`Mixed-Media Entropy`): `53.2%` (`25/47` nhịp) `[📊]`
  - Trần phần tử đồng thời (`Max Concurrent`): `<= 3` phần tử (`3` phần tử tối đa — `0%` tạp nham) `[✅]`

## 1. Danh Sách Lỗi Phát Hiện Trên Lưới Ảnh Browser & Trạng Thái Xử Lý (`P0 / P1 / P2`)

| Mức độ | Định vị (`t=... · cảnh · vị trí`) | Vấn đề phát hiện khi soi bằng mắt (`read_file`) | Thay đổi chính xác đã thực hiện | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **🔴 P0** | `t=141.7s & 149.5s · sc_08 · Phụ đề #17` | Câu phụ đề tiếng Việt số `#17` bị lẫn từ tiếng Thái (`"sựเปราะบาง"`) khi dịch chữ `"exposed"` (trong câu *"Suddenly, Washington understood how exposed Alaska was"*). | Đã sửa chính xác thành `"sự mong manh và dễ tổn thương"` trong `chi_dao_phan_canh.json` và `storyboard.json`, chụp lại `director_sc_08_A_141s7.png` & `director_sc_08_B_149s5.png` và xác nhận bằng mắt 100% tiếng Việt chuẩn xác. | `[✅ ĐÃ SỬA]` |
| **🟡 P1** | `t=16.6s (sc_01_B) & t=129.7s (sc_07_A) · Khung Polaroid trái` | Tư liệu gốc `01.4_00m07s_polaroid_klondike_gold_pan_1896.jpg` và `07.1_02m06s_polaroid_kiska_landing_34k.jpg` có kích thước ảnh tiền cảnh nhỏ hơn khung `960x720`, khiến ảnh sắc nét nằm lọt thỏm ở giữa với viền mờ tối bao quanh cả 4 phía. | Đã dùng thuật toán Lanczos phóng to phần ảnh sắc nét (`fg`) lấp kín 100% chiều cao `720px` của khung Polaroid (`776x720` cho `01.4` và `873x720` cho `07.1`), chỉ giữ viền mờ nhẹ 2 bên hông. Đã chụp lại và kiểm tra bằng mắt. | `[✅ ĐÃ SỬA]` |
| **🟡 P1** | `t=36.3s (sc_02_B), t=125.0s (sc_06_B), t=141.7s (sc_08_A) · Đinh ghim đỏ Polaroid` | Các khối tư liệu góc trái có tọa độ `y=120..130` khiến đầu đinh ghim đỏ (`top: -11px`) hơi chạm nhẹ vào mép dưới của thanh nhãn niên đại `#hud-era-anchor`. | Đã dời tọa độ `y` của các tư liệu `02.4`, `06.1`, `06.4`, `06.6`, `08.1`, `08.3` xuống `y=140`, tạo khoảng thở an toàn và cân đối hoàn hảo với thanh niên đại. | `[✅ ĐÃ SỬA]` |
| **🟡 P1** | `t=129.7s · sc_07_A · Nửa phải màn hình` | Tại thời điểm `129.7s`, dải giấy xé `07.2_02m09s_torn_split_34k_vs_0_japanese` đã xuất hiện ở giữa nhưng khối Headline `07.3_02m11s_headline_nobody_there` tới `131.5s` mới vào, làm nửa phải màn hình trống trải trong 2.5 giây và tạo cảnh báo giữ nhịp `5.0s`. | Đã điều chỉnh `07.2` (`128.4s -> 132.4s`) và đẩy `07.3` vào sớm từ `129.4s -> 137.7s`, giúp nửa phải khung hình tại `129.7s` hiện đầy đủ khối Headline gạch đỏ `"FIERCE JAPANESE GARRISON"` + tô vàng `"NOBODY THERE • SLIPPED AWAY IN THE FOG"`, đồng thời kéo `Max Hold Stretch` toàn phần xuống `4.00s`. | `[✅ ĐÃ SỬA]` |

## 2. Minh Bạch Triệt Để (Theo Chuẩn Ray Dalio & HeyGen `review.md`)

- **Các quyết định sáng tạo đã chọn (và các hướng đã loại bỏ):**
  - **Đã chọn:** Kết hợp luân phiên 5 mô-típ chuyển động (`MOTIF_1_DETECTIVE_CANVAS_PAN` -> `MOTIF_2_BROLL_KINETIC_OVERDRIVE` -> `MOTIF_4_EVIDENCE_SPLIT_COLLISION` -> `MOTIF_3_CARTOGRAPHIC_3D_FLYOVER` -> `MOTIF_5_DATA_STORY_PROGRESSION`), dùng tư liệu video lịch sử thật từ Prelinger Archives / U.S. National Archives cho 4 cao trào động: đoàn người leo đèo băng Chilkoot (`02.4`), chó kéo xe vượt bão tuyết Nome (`04.6`), pháo kích chiến dịch Aleutian WWII (`06.1`), và công binh Mỹ mở đường cao tốc Alaska (`08.1`).
  - **Đã loại bỏ:** Loại bỏ hoàn toàn ảnh minh họa chung chung hoặc lặp lại tư liệu giữa các cảnh; loại bỏ cách xếp chồng quá 3 phần tử cùng lúc để giữ khoảng thở thẩm mỹ tối thiểu 35% diện tích bàn dựng.
- **Cảnh yếu nhất trong phần này là cảnh nào, và đã được gia cố ra sao?**
  - **Cảnh yếu nhất ban đầu:** `sc_07` (*Chiến dịch Kiska — 34.000 quân Đồng minh đổ bộ lên hòn đảo trống không, `126.3s -> 137.7s`*), vì ở bản chụp đầu tiên tại `t=129.7s`, nhịp Headline vào trễ khiến nửa phải bàn dựng bị trống sau đường rách giấy `TORN_PAPER_SPLIT`, đồng thời ảnh đổ bộ Kiska (`07.1`) bị viền mờ 4 cạnh.
  - **Cách gia cố:** Đã phóng to ảnh tư liệu đổ bộ Kiska (`07.1`) tràn 100% chiều cao khung Polaroid, đồng bộ thời điểm vào của đường giấy xé (`128.4s`) và bảng Headline gạch bút đỏ (`129.4s`) kèm mộc đỏ `"ESCAPED IN THE FOG"` (`134.5s`), biến `sc_07` thành một trong những cảnh đối lập thị giác sắc bén nhất của `phan_03`.
- **Những gì đã đo bằng số và những gì đã kiểm tra bằng mắt:**
  - **Đo bằng số (`[📊]`):** Kiểm toán tự động bằng `buoc_3_kiem_toan_nhip_va_vet_cat.py` xác nhận `0` lỗi P0, `0` cảnh báo P1, `47` nhịp (`3.21s/nhịp`), `Max Hold Stretch = 4.00s <= 4.50s`, `Mixed-Media Entropy = 53.2% >= 50%`, `19/19` file nguyên liệu vật lý tồn tại 100% và không trùng lặp.
  - **Kiểm tra bằng mắt (`[👁️]`):** Đã mở xem trực tiếp bằng `read_file` toàn bộ 19/19 tư liệu gốc cùng 17/17 khung hình trình duyệt (`director_sc_01_A_5s3.png` -> `director_sc_08_B_149s5.png` + `director_studio_5track_overview.png`), phát hiện và sửa dứt điểm lỗi từ tiếng Thái trong phụ đề `#17`, lỗi khung ảnh Polaroid `01.4` & `07.1`, khoảng cách đinh ghim đỏ và nhịp vào của `sc_07`.
