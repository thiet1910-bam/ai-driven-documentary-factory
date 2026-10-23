# BIÊN BẢN ĐẠO DIỄN KIỂM TOÁN & HẬU KIỂM (`REVIEW.md` — KIẾN TRÚC ĐA THẾ GIỚI V2.0)

- **Mã phần dự án:** `phan_03` (`00:04:41.5 -> 00:07:12.2`, thời lượng `150.73s`)
- **Phiên bản kiến trúc:** `AI-Driven Documentary Factory v2.0` (*Multi-World Long-Form Documentary Architecture*)
- **Kết quả chạy `buoc_3_kiem_toan_nhip_va_vet_cat.py` (v2.0):**
  - Số lỗi P0 (Đè chữ / Tràn khung / Lặp Thế Giới / Thiếu file): `0` lỗi `[📊]`
  - Số cảnh báo P1 (Nhịp điệu / Bố cục bất đối xứng): `0` cảnh báo `[📊]`
  - Tổng số cảnh lớn (`Scenes`): `8` cảnh (`sc_01` -> `sc_08`) trải qua **5/5 Thế Giới Thị Giác (`WORLD_1` -> `WORLD_5`)** `[📊]`
  - Chuỗi Thế Giới Thị Giác (`world_type`): `WORLD_1_FULL_MAP -> WORLD_2_CINEMA_FULLBLEED -> WORLD_3_DETECTIVE_CANVAS -> WORLD_1_FULL_MAP -> WORLD_4_DATA_STAGE -> WORLD_2_CINEMA_FULLBLEED -> WORLD_5_ARCHIVE_XRAY -> WORLD_4_DATA_STAGE` (`0` lần lặp liên tiếp) `[📊]`
  - Chuỗi Bố Cục Tọa Độ (`layout_mode`): `FULL_BLEED -> FULL_BLEED -> RIGHT_ANCHOR -> FULL_BLEED -> CENTER_DATA_STAGE -> FULL_BLEED -> CENTER_STAGE -> FULL_BLEED` (`0%` lặp bố cục 2 cột trái-phải công nghiệp) `[📊]`
  - Tổng số nhịp (`Enter-Hold-Exit Beats`): `47` nhịp (`3.21s / nhịp`) `[📊]`
  - Khoảng giữ nhịp dài nhất (`Max Hold Stretch`): `4.00s` (Chuẩn `<= 4.50s`) `[📊]`
  - Tỷ lệ Chất liệu Động & Tương tác Vật lý (`Mixed-Media Entropy`): `55.3%` (`26/47` nhịp) `[📊]`
  - Trần phần tử đồng thời (`Max Concurrent`): `<= 3` phần tử (`3` phần tử tối đa — `0%` tạp nham) `[✅]`

## 1. Danh Sách Lỗi Phát Hiện Trên Lưới Ảnh Browser V2.0 & Trạng Thái Xử Lý (`P0 / P1 / P2`)

| Mức độ | Định vị (`t=... · cảnh · vị trí`) | Vấn đề phát hiện khi soi bằng mắt (`read_file`) | Thay đổi chính xác đã thực hiện | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **🟡 P1** | `t=44.7s · sc_03_A · Dây chỉ đỏ thám tử & HUD góc phải trên` | Dây chỉ đỏ `03.1` (`RED_STRING_LINK`) thoát ở `44.2s` trước mốc chụp `44.7s`, và nhãn `#hud-price-tag` `"SHOVEL & SALOON OWNERS"` quá dài (22 ký tự) khiến chữ `"OWNERS"` rớt xuống dòng 2 sát mép giấy xé. | Đã tinh gọn `hud_ticker.value` thành `"SHOVEL SELLERS"` nằm gọn trên 1 dòng và điều chỉnh nhịp dây chỉ đỏ `03.1` (`t0=43.5s -> t1=50.2s`), nối trực tiếp từ biểu đồ người bán xẻng sang chân dung Wyatt Earp tại `44.7s`. | `[✅ ĐÃ SỬA]` |
| **🟡 P1** | `t=101.8s · sc_05_B · Tiêu đề biểu đồ SVG_LINE_CHART` | Tiêu đề `"1925 SERUM RUN: DISTANCE COVERED PER LEAD DOG"` và nhãn đỉnh `"TOGO: 260+ MILES (5X BALTO!)"` hơi dài nên bị rớt chữ `"DOG"` và `"BALTO!)"` xuống dòng thứ 2. | Đã biên tập cô đọng thành `"1925 SERUM RUN: DISTANCE BY LEAD DOG"` và `"TOGO: 260+ MI (5X BALTO)"`, giúp thanh Header của `SVG_LINE_CHART` hiển thị trên 1 dòng sắc nét. | `[✅ ĐÃ SỬA]` |
| **🟡 P1** | `t=129.7s · sc_07_A · Thế giới WORLD_5_ARCHIVE_XRAY` | Cảnh `sc_07` được gán `WORLD_5_ARCHIVE_XRAY` nhưng `07.1` chưa bật `full_bleed: true` và `07.2` vẫn giữ kiểu `TORN_PAPER_SPLIT` cũ. | Đã nâng cấp `07.1` thành tư liệu tràn viền (`full_bleed: true`) và chuyển `07.2` sang kính lúp soi tia X (`SPOTLIGHT_XRAY`: `"34,000 TROOPS LAND • 0 JAPANESE FOUND!"`, `128.4s -> 133.4s`), đúng chất đại cảnh soi hồ sơ mật `WORLD_5_ARCHIVE_XRAY`. | `[✅ ĐÃ SỬA]` |
| **🔴 P0 (Lịch sử v1)** | `t=141.7s & 149.5s · sc_08 · Phụ đề #17` | Câu phụ đề tiếng Việt số `#17` ở bản nháp đầu có lẫn từ ngoại lai đã được sửa triệt để thành `"sự mong manh và dễ tổn thương"`. | Duy trì chuẩn 100% tiếng Việt tự nhiên trong cả `chi_dao_phan_canh.json` và `storyboard.json`. | `[✅ ĐÃ SỬA]` |

## 2. Minh Bạch Triệt Để (Theo Chuẩn Ray Dalio & HeyGen `review.md`)

- **Các quyết định sáng tạo đã chọn (và các hướng đã loại bỏ) để giải bài toán phim dài 5–30+ phút:**
  - **Đã chọn:** Phá bỏ hoàn toàn khuôn mẫu "bàn giấy 2 cột tĩnh" của v1.0 bằng **Kiến trúc 5 Thế Giới Thị Giác (`Multi-World Architecture v2.0`)**:
    1. `WORLD_1_FULL_MAP` (`sc_01`, `sc_04`): Bản đồ cổ 1897 và bản đồ đường chạy huyết thanh 1925 bung tràn 100% màn hình (`full_bleed: true`) kết hợp đường bay вектор đứt nét tự vẽ `MAP_ROUTE`.
    2. `WORLD_2_CINEMA_FULLBLEED` (`sc_02`, `sc_06`): Phim tư liệu đèo băng Chilkoot và chiến dịch quần đảo Aleutian WWII tràn 100% màn hình kèm dải đen điện ảnh `2.35:1` (`cinema-bar`) và kính lúp `SPOTLIGHT_XRAY`.
    3. `WORLD_3_DETECTIVE_CANVAS` (`sc_03`): Bàn điều tra bất đối xứng (`RIGHT_ANCHOR` — nhân vật Wyatt Earp bên phải, biểu đồ bên trái) nối bằng sợi chỉ đỏ `RED_STRING_LINK`.
    4. `WORLD_4_DATA_STAGE` (`sc_05`, `sc_08`): Sân khấu dữ liệu tối giản kiểu Vox với biểu đồ đường chiếu sáng `SVG_LINE_CHART` (*Togo 260 dặm vs Balto 55 dặm*) và thước trượt niên đại `TIMELINE_SCROLLER` (*1867 -> 1896 -> 1925 -> 1942 -> 1959*).
    5. `WORLD_5_ARCHIVE_XRAY` (`sc_07`): Hồ sơ chiến dịch Kiska 1943 phóng tràn màn hình được soi sáng cục bộ bằng `SPOTLIGHT_XRAY`.
  - **Đã loại bỏ:** Loại bỏ bố cục lặp đi lặp lại `LEFT_ANCHOR` quá 2 cảnh liên tiếp; loại bỏ nền giấy kem tĩnh đơn điệu kéo dài suốt nhiều phút.
- **Cảnh ấn tượng nhất và cảnh được gia cố mạnh nhất trong bản `v2.0`:**
  - **Cảnh ấn tượng nhất:** `sc_01_B` (`16.6s`, bản đồ Klondike tràn màn hình với đường bay `MAP_ROUTE` nối từ Seattle/San Francisco thẳng lên Klondike), `sc_05_B` (`101.8s`, biểu đồ đường `SVG_LINE_CHART` vạch trần khoảng cách 260+ dặm của Togo so với 55 dặm của Balto), và `sc_08_A` (`141.7s`, thước trượt niên đại `TIMELINE_SCROLLER` trên nền công binh Mỹ xây cầu Alaska Highway).
  - **Cảnh được gia cố mạnh nhất:** `sc_07` (`126.2s -> 137.8s`), được nâng cấp từ bố cục xé giấy 2 cột cũ sang `WORLD_5_ARCHIVE_XRAY` tràn viền kết hợp kính lúp `SPOTLIGHT_XRAY` soi thẳng vào bãi đổ bộ Kiska trống không.
- **Những gì đã đo bằng số và những gì đã kiểm tra bằng mắt:**
  - **Đo bằng số (`[📊]`):** Kiểm toán tự động bằng `buoc_3_kiem_toan_nhip_va_vet_cat.py` xác nhận `0` lỗi P0, `0` cảnh báo P1, độ phủ `5/5` Thế Giới Thị Giác, `0` lần lặp World liên tiếp, `47` nhịp (`3.21s/nhịp`), `Max Hold Stretch = 4.00s <= 4.50s`, `Mixed-Media Entropy = 55.3% >= 50%`.
  - **Kiểm tra bằng mắt (`[👁️]`):** Đã mở xem trực tiếp bằng `read_file` toàn bộ 17/17 khung hình trình duyệt v2.0 (`director_sc_01_A_5s3.png` -> `director_sc_08_B_149s5.png` + `director_studio_5track_overview.png`), tinh chỉnh từng chi tiết nhỏ nhất (nhãn HUD góc phải, dòng tiêu đề `SVG_LINE_CHART`, dây chỉ đỏ `RED_STRING_LINK`, và kính lúp `SPOTLIGHT_XRAY` ở `sc_07`).
