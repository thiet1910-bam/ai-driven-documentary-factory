# 🖼️ QUY CHUẨN XỬ LÝ HÌNH ẢNH, STICKER TÁCH NỀN, BIỂU ĐỒ VẬT LÝ & BỐ CỤC (VISUAL ASSETS & LAYOUTS)

> [!IMPORTANT]
> Trong phong cách Vox Editorial (Gu 2) và Cartographic Storybook (Gu 1), hình ảnh không bao giờ bị quăng lên màn hình dưới dạng một bức ảnh chữ nhật thô kệch. Mọi bức ảnh hoặc phải nằm trong **Khung tư liệu vật lý (Polaroid / Torn Paper Card)**, hoặc phải được **Tách nền sạch tuyệt đối kèm viền trắng & bóng đổ sâu (Cutout Sticker / Figurine)**.

---

## 1. 6 ĐỊNH DẠNG HÌNH ẢNH & ĐỒ HỌA DỮ LIỆU TRONG KHO

### 1.1. `VIBRANT_DIE_CUT_STICKER` (Ảnh Tách Nền Viền Trắng Sắc Nét — Gu 1 & Gu 2)
- **Yêu cầu kỹ thuật**:
  1. Tách sạch 100% phông nền bằng `rembg` kết hợp thuật toán **Khử đảo rác ở 4 góc (`Connected-Components Alpha Island Cleanup`)** — giữ lại duy nhất cụm đối tượng trung tâm lớn nhất, xóa sạch mọi mảng đen/trắng thừa ở rìa ảnh.
  2. Tăng nhẹ độ tương phản (`Contrast +8%`) và độ bão hòa màu (`Saturation +12%` cho đối tượng hiện đại/thiên nhiên, hoặc chuyển `Sepia Contrast` cho chân dung lịch sử cổ).
  3. Tạo lớp viền trắng đều (`4px – 6px` quanh kênh Alpha) và bóng đổ mềm (`GaussianBlur radius 8px, offset Y +10px`).

### 1.2. `ARCHIVAL_POLAROID_LANDSCAPE_FIT` (Khung Ảnh Lưu Trữ Ghim Đinh Đỏ — Không Bao Giờ Cắt Lẹm Đầu)
- **Quy tắc chống cắt lẹm (Anti-Cropping Rule)**:
  - Mọi bức ảnh dọc (`w / h < 1.35`, ví dụ chân dung đứng hoặc bản đồ dọc) trước khi đưa vào khung Polaroid ngang (`16:10`) bắt buộc phải chạy hàm **`reframe_to_landscape()`**: tạo lớp nền mờ tối lấy từ chính bức ảnh gốc (`GaussianBlur radius 28px, Brightness 42%`) rồi đặt bức ảnh gốc sắc nét vào chính giữa để hiển thị trọn vẹn 100% đầu người và chú thích bản đồ.

### 1.3. `TORN_PAPER_RECEIPT_AND_DIVIDER` (Thẻ Giấy Xé Răng Cưa & Vách Ngăn Chia Đôi Màn Hình — Gu 2)
- **Ứng dụng**:
  - **Vách ngăn dọc (`Vertical Torn Divider`)**: Đặt tại `x = 960` để chia đôi màn hình so sánh `QUÁ KHỨ` (Trái) $\leftrightarrow$ `HIỆN TẠI` (Phải).
  - **Thẻ hóa đơn / bảng kê (`Torn Budget Card`)**: Tờ giấy trắng/kem có cạnh dưới xé răng cưa, liệt kê 3–4 hạng mục, trong đó hạng mục quan trọng nhất được quét bút dạ vàng nổi bật.
  - **Thẻ HUD góc trên phải (`Corner Torn Ticker`)**: Mảnh giấy xé nhỏ ghim góc phải trên chứa con số đếm liên tục.

### 1.4. `PHYSICAL_OBJECT_BAR_CHART` (Biểu Đồ Cột Kết Hợp Vật Thể Thật Trên Đỉnh — Gu 2)
- **Mẫu chuẩn từ Gu 2 (`DEFENSE` vs `INTEREST`)**:
  - Hai cột biểu đồ mọc từ dưới lên (`#141414` Đen và `#D92318` Đỏ) với mép trên có độ nhám giấy xé.
  - Trên đỉnh cột `DEFENSE` đặt một **hình cắt rời chiếc tiêm kích chiến đấu (`Fighter Jet Cutout`)**.
  - Trên đỉnh cột `INTEREST` đặt **các cọc tiền đô la cắt rời (`Cash Stack Cutouts`)** chất cao hơn cả máy bay chiến đấu.

### 1.5. `WAFFLE_100_SILHOUETTES_GRID` (Biểu Đồ Lưới 100 Hình Người / Đơn Vị — Gu 1 & Gu 2)
- **Mẫu chuẩn**:
  - Từ Gu 1: Lưới `20 cột x 5 hàng = 100 hình người` (hoặc `25 x 4`) để biểu diễn tỷ lệ `12%` hay `40%` dân số.
  - Từ Gu 2: Hai chiếc lọ thủy tinh (`Glass Jars`) chứa các chấm tròn đen/đỏ đại diện cho `280 PPM` vs `420+ PPM` khí CO2.

### 1.6. `CARTOGRAPHIC_SHIELD_AND_ARROWS` (Khiên Huy Hiệu, Mũi Tên Bản Đồ & Quả Cầu Bảo Vệ — Gu 1)
- **Thành phần**:
  - **Khiên Quốc Huy (`Vector Shield Badge`)**: Đặt chính giữa lãnh thổ khi nói về chủ quyền/phòng thủ.
  - **Mũi Tên Tỏa Tròn (`Radial Map Arrows`)**: Phóng từ trung tâm lãnh thổ ra các hướng.
  - **Vòng Tròn Nét Đứt Xoay (`Rotating Dashed Perimeter`)**: Bao quanh con dấu `NEUTRAL` hoặc vùng cấm.

---

## 2. 4 MẪU BỐ CỤC KHUNG HÌNH CHUẨN 1920x1080 (4 MASTER COMPOSITIONS)

1. **Bố cục A — Đối xứng Trái / Phải (`Asymmetric 50/50 Split Desk`)**:
   - Trái (`x: 90..910`): Ảnh Polaroid / Bản đồ / Tờ hóa đơn giấy xé.
   - Phải (`x: 980..1800`): Nhân vật Sticker tách nền / Bảng chữ Headline / Biểu đồ cột.
2. **Bố cục B — Chia Đôi Giấy Xé (`Torn-Paper Dual Comparison`)**:
   - Nửa trái (`x: 0..950`): Bối cảnh A (`200 YEARS AGO` / `1867`).
   - Chính giữa (`x: 945..975`): Dải giấy xé dọc có bóng đổ.
   - Nửa phải (`x: 970..1920`): Bối cảnh B (`TODAY` / `MODERN ERA`).
3. **Bố cục C — Bản Đồ Trung Tâm Toàn Cảnh (`Full-Bleed Cartographic Stage`)**:
   - Toàn màn hình (`1920x1080`): Bản đồ địa lý cổ hoặc vệ tinh.
   - Góc trên trái (`x: 80, y: 60`): Số năm lịch sử (`1815`).
   - Góc trên phải (`x: 1420, y: 45`): Bảng theo dõi câu hỏi (`Agenda Tracker`) hoặc Bộ đếm (`HUD Ticker`).
   - Giữa bản đồ: Lãnh thổ tô đỏ/cam + Mũi tên + Nhân vật Figurine.
4. **Bố cục D — Đảo Nền Đen Cao Trào (`Climax Dark-Mode Statement`)**:
   - Toàn màn hình nền đen `#0A0A0A`.
   - Trái (`x: 140..1050`): Cặp chữ tương phản `~~TỪ CŨ~~` $\rightarrow$ `TỪ MỚI` tô vàng + Con số đỏ.
   - Phải (`x: 1180..1760`): 1 Vật thể ẩn dụ tách nền sắc nét (Đồng hồ cát, Quả địa cầu, Cán cân công lý).
