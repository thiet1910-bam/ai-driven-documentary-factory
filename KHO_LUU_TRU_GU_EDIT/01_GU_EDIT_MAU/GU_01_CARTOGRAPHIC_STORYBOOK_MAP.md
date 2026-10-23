# 🗺️ GU EDIT 01: CARTOGRAPHIC STORYBOOK & ILLUSTRATED HISTORICAL MAP
*(Phân tích từ Video mẫu: `https://www.youtube.com/watch?v=gP4ihbNXFrY` — "Switzerland Should Be Poor. Here's Why It Isn't" / Kênh: Fortune of Nations Animated)*

> [!NOTE]
> **Bản chất thẩm mỹ (Core Aesthetic):** Kết hợp giữa **Bản đồ địa lý cổ điển (Hand-drawn Parchment Cartography)**, **Bản đồ địa hình vệ tinh 3D tối màu (Satellite Relief Map)** và **Nhân vật minh họa dạng quân cờ/sticker (Illustrated Figurines)** để giải thích các nghịch lý lịch sử, kinh tế và địa chính trị một cách trực quan, dễ hiểu.

---

## 1. BẢNG MÀU & CHẤT LIỆU NỀN (COLOR PALETTE & TEXTURES)

| Thành phần | Mã màu Hex | Mô tả ứng dụng trong khung hình |
| :--- | :--- | :--- |
| **Giấy Da Bản Đồ Cổ (Parchment Base)** | `#E6DCC5` $\rightarrow$ `#CBBBA0` | Nền chính cho các cảnh lịch sử (thế kỷ 16–19), có hiệu ứng bo tối 4 góc (Vignette) và nét vẽ sông ngòi, dãy núi bằng mực nâu. |
| **Nâu Mực Bản Đồ (Cartographic Ink)** | `#4A3525` | Đường biên giới quốc gia, nét vẽ dãy núi Alps, đường bờ biển và chữ in chìm tên vùng đất cổ (`HELVETIA`, `Oceanus Atlanticus`). |
| **Lãnh Thổ Tâm Điểm (Focal Territory)** | `#D88A73` (Cam đất) hoặc `#D91E18` (Đỏ tươi) | Tô nổi bật quốc gia đang được phân tích ở chính giữa bản đồ cùng đường viền trắng dày (`3px - 5px`) phát sáng nhẹ. |
| **Vàng Nhấn Số Liệu (Highlight Gold)** | `#F5C518` | Hộp nền chứa con số tiền tệ/dân số lớn (`$111,000`, `1,450,042`, `1,500,000`), huy hiệu thứ hạng (`#4`) và số thứ tự câu hỏi (`1`, `2`, `3`). |
| **Đỏ Cảnh Báo & Quân Sự (Crimson Alert)** | `#C81E1E` | Con dấu cao su (`NEUTRAL`), chữ `NO` trong thẻ danh sách, mũi tên xuất quân và số phần trăm (`12%`, `15%`). |
| **Nền Địa Hình Vệ Tinh (Satellite Dark Mode)** | `#141A17` / `#1E3518` | Dùng khi đối chiếu với hiện tại (`Today`) hoặc phóng từ quả địa cầu 3D xuống lãnh thổ thực tế. |

---

## 2. HỆ THỐNG TYPOGRAPHY & GHI CHÚ TRÊN BẢN ĐỒ

1. **Nhãn Năm Lịch Sử Cố Định Góc Trái (`Corner Era Timestamp`)**:
   - Vị trí: Góc trên bên trái (`x: 80, y: 65`).
   - Phông chữ: **Serif Cổ Điển có chân dạng khắc đá/in sách cổ** (*IM Fell English / Garamond / Cinzel*), cỡ `42px - 54px`, màu mực đen nâu (`#2B2118`) hoặc trắng ngà (trên nền tối).
   - Ví dụ: `1817`, `1500`, `1515`, `1800s`, `1855`, `Today`.
2. **Ghi Chú Viết Tay Kèm Mũi Tên Cong (`Handwritten Callout + Curved Arrow`)**:
   - Phông chữ: **Script / Handwritten nghiêng tự nhiên** (*Caveat / Kalam / Shadows Into Light*), cỡ `32px - 40px`.
   - Cách xuất hiện: Chữ hiện ra ngay trên đầu nhân vật hoặc vùng địa lý (`eating grass`, `and tree bark`, `paid by two different kings`, `too many people`), đi kèm một mũi tên vẽ tay ngắn chỉ thẳng vào vật thể.
3. **Thẻ Nhãn Dán Nền Kem (`Cream Paper Tag / Banner`)**:
   - Dùng cho các cụm từ giải thích nguyên nhân trên bản đồ (`the harvest failed`, `a wall`).
   - Nền giấy kem sáng (`#F7F1E1`), viền nâu mảnh, đổ bóng nhẹ tách khỏi mặt bản đồ.
4. **Con Số Khổng Lồ Đóng Khung Vàng (`Gold Box Stat`)**:
   - Phông chữ: **Condensed Sans-Serif Đậm** (*Bebas Neue / Oswald Bold*), chữ đen `#111111` đặt trong hộp chữ nhật vàng `#F5C518` bo góc nhẹ (`$111,000`, `1,450,042`).

---

## 3. 8 KỸ THUẬT DÀN DỰNG & ĐỒ HỌA ĐẶC TRƯNG (SIGNATURE VISUAL MECHANICS)

1. **`PERSISTENT_AGENDA_TRACKER` (Bảng Câu Hỏi Định Hướng Ghim Góc Trên Phải)**:
   - Mở đầu video: Bảng `three questions` xuất hiện chính giữa màn hình trên nền tối với 3 thanh ngang đánh số `1`, `2`, `3` trong vòng tròn vàng.
   - Khi vào nội dung: Toàn bộ bảng thu nhỏ lại và **ghim cố định ở góc trên bên phải màn hình** (`x: 1420, y: 40, w: 450`), làm sáng câu hỏi đang được giải đáp và làm mờ 2 câu còn lại. Giúp khán giả luôn biết mình đang ở phần nào của lập luận.
2. **`GLOBE_TO_TERRITORY_ZOOM` (Thu Phóng Từ Quả Địa Cầu 3D Xuống Bản Đồ)**:
   - Khi nói về sự kiện toàn cầu ảnh hưởng đến khu vực (ví dụ núi lửa `Mount Tambora April 1815` ở Indonesia gây mất mùa tại châu Âu), camera quay từ quả địa cầu 3D ngoài không gian trước khi cắt về bản đồ khu vực.
3. **`ILLUSTRATED_FIGURINE_CUTOUTS` (Nhân Vật Minh Họa Có Đế Đứng Trên Bản Đồ)**:
   - Các nhân vật lịch sử (nông dân, lính đánh thuê, vua Pháp, Giáo hoàng, Napoleon, nhà ngoại giao 1815) được vẽ theo phong cách minh họa 2D chi tiết, **có đế gỗ tròn bên dưới giống quân cờ** hoặc viền cắt sticker, trượt êm ái dọc theo các đường chấm đứt (`dotted trajectory`) trên bản đồ.
4. **`RADIAL_EXODUS_ARROWS` (Mũi Tên Phóng Tỏa Tròn Từ Lãnh Thổ)**:
   - Khi diễn tả sự lan tỏa, xuất khẩu hoặc di cư (`1,500,000 Swiss men in foreign armies`), 6–8 mũi tên đỏ thẳng phóng đồng loạt từ ranh giới quốc gia hướng ra các nước láng giềng theo mọi hướng.
5. **`WAFFLE_PEOPLE_ARRAY_CHART` (Biểu Đồ Ma Trận Hình Người 100 Ô)**:
   - Thay vì dùng biểu đồ cột nhàm chán, để biểu diễn tỷ lệ dân số (`12%`, `a quarter... to 40%`), hệ thống vẽ một **lưới gồm 100 biểu tượng hình người nhỏ (silhouettes)**. Phần trăm được nhắc đến sẽ chuyển sang màu Đỏ (`#C81E1E`) hoặc Đen đậm theo hiệu ứng quét từng người một kèm tiếng *tick-tick*.
6. **`STAMP_INSIDE_DASHED_RADAR` (Con Dấu Đỏ Giữa Vòng Tròn Nét Đứt Xoay)**:
   - Khi chốt một trạng thái địa chính trị kéo dài hàng thế kỷ (`for three centuries... NEUTRAL`), con dấu đỏ `NEUTRAL` đập mạnh vào giữa quốc gia, bao quanh bởi một vòng tròn nét đứt màu nâu đen xoay chậm như vùng bất khả xâm phạm.
7. **`PROTECTIVE_BUBBLE_AMID_FIRE` (Ẩn Dụ Thị Giác: Quả Cầu Thủy Tinh Giữa Biển Lửa)**:
   - Khi châu Âu xung quanh chìm trong chiến tranh (các ngọn lửa hoạt hình bật lên khắp Pháp, Đức, Áo, Ý), lãnh thổ ở giữa được bọc trong một **quả cầu thủy tinh trong suốt (`Glass Shield Bubble`)**, truyền tải tức thì khái niệm "ốc đảo an toàn".
8. **`DOCUMENT_SIGNING_POPUP` (Tờ Hiệp Ước Lịch Sử Đóng Dấu Sáp Đỏ)**:
   - Một tờ giấy da lớn (`Guarantee: Switzerland will stay NEUTRAL`) trượt lên giữa màn hình, chữ ký mực đen tự vẽ ra, con dấu đỏ đóng xuống và gắn huy hiệu quốc gia tròn ở góc phải tờ giấy.
