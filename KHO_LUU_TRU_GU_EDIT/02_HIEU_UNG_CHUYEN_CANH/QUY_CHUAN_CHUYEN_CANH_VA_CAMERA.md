# 🎞️ QUY CHUẨN HIỆU ỨNG CHUYỂN CẢNH, CAMERA & NHỊP ĐIỆU CHUYỂN ĐỘNG (TRANSITIONS & MOTION EASING)

> [!IMPORTANT]
> Điểm khác biệt lớn nhất giữa một video "AI làm hàng loạt rẻ tiền" và "Motion Graphics chuẩn Vox / Fortune of Nations" nằm ở **Đường cong gia tốc (Easing Curves)** và **Sự kết nối không gian giữa hai cảnh (Spatial Continuity)**. Tuyệt đối không dùng chuyển động tuyến tính (`linear`) cứng nhắc.

---

## 1. BẢNG ĐƯỜNG CONG GIA TỐC CHUẨN (STANDARD EASING CURVES)

| Mã Easing | Công thức Cubic-Bezier / Toán học | Thời lượng chuẩn | Ứng dụng cụ thể |
| :--- | :--- | :--- | :--- |
| **`EXPO_OUT_SNAP`** | `cubic-bezier(0.16, 1, 0.3, 1)`<br>hoặc `1 - pow(1 - t, 4)` | `0.35s – 0.45s` | Khi đặt ảnh Polaroid, thẻ hóa đơn giấy xé (`Torn Receipt`), hoặc thanh biểu đồ phóng ra: lao vào cực nhanh rồi phanh êm ái ở những pixel cuối cùng. |
| **`SPRING_OVERSHOOT`** | `cubic-bezier(0.34, 1.56, 0.64, 1)` | `0.40s – 0.50s` | Khi bật nhân vật Sticker/Figurine (`POP_UP`), huy hiệu quốc huy (`Shield`), hoặc lọ thủy tinh CO2: phóng vọt lên `108%` kích thước rồi đàn hồi về `100%`. |
| **`STAMP_IMPACT_SLAM`** | Rơi nhanh từ `scale(2.2)` xuống `scale(1.0)` trong `0.14s` + Rung khung hình (`Camera Shake ±4px` trong `0.12s`) | `0.26s` | Khi đóng dấu mộc đỏ (`SOLD FOR $7`, `NEUTRAL`, `2048 [PROJECTED]`). |
| **`MARKER_SWIPE_EASE`** | `cubic-bezier(0.65, 0, 0.35, 1)` (`scaleX: 0 -> 1`) | `0.30s – 0.40s` | Khi quét vệt bút dạ vàng (`#F5C518`) hoặc xanh (`#1D4ED8`) từ trái sang phải dưới từ khóa trọng tâm. |
| **`CAMERA_MAP_GLIDE`** | `cubic-bezier(0.45, 0, 0.15, 1)` (Smooth S-Curve) | `0.80s – 1.40s` | Khi camera lướt từ vùng này sang vùng khác trên bản đồ lớn (Gu 1) hoặc thu nhỏ từ toàn cảnh về góc bàn. |

---

## 2. 6 HIỆU ỨNG CHUYỂN CẢNH ĐẶC TRƯNG (SIGNATURE SCENE TRANSITIONS)

### 2.1. `HUD_SHRINK_TO_CORNER` (Thu Nhỏ Từ Giữa Màn Hình Về Góc Ghim Cố Định)
- **Nguồn gốc**: Cả Gu 1 (`three questions`) và Gu 2 (`$53,973 BORROWED SINCE YOU HIT PLAY`).
- **Cơ chế hoạt động**:
  1. Ở câu mở đầu (Hook), phần tử chủ đạo (Bảng 3 câu hỏi hoặc Bộ đếm tiền) xuất hiện **toàn màn hình ở chính giữa (`scale: 1.0, x: center, y: center`)**.
  2. Ngay khi chuyển sang cảnh giải thích chi tiết, phần tử này **không biến mất** mà trượt chéo và thu nhỏ (`scale: 0.38`) về góc trên bên phải màn hình (`x: 1580, y: 45`), nhường không gian chính giữa cho biểu đồ/bản đồ mới.

### 2.2. `TORN_PAPER_SPLIT_WIPE` (Xé Đôi Màn Hình So Sánh Trước / Sau)
- **Nguồn gốc**: Gu 2 (`200 YEARS AGO` vs `TODAY`).
- **Cơ chế hoạt động**:
  1. Nửa bên trái xuất hiện trước với bối cảnh quá khứ (`200 YEARS AGO`).
  2. Khi giọng đọc chuyển sang từ `"but today..."`, một dải giấy xé răng cưa dọc có bóng đổ sâu quét từ trên xuống ở chính giữa màn hình (`x = 960`), mở ra nửa bên phải (`TODAY`) để đối chiếu trực diện 1:1.

### 2.3. `HARD_DARK_MODE_INVERT` (Đảo Ngược Nền Đen Tuyền Ở Cao Trào)
- **Nguồn gốc**: Gu 2 (`We're not paying for the FUTURE. We're paying for the PAST`).
- **Cơ chế hoạt động**:
  1. Suốt các cảnh trước, mắt khán giả đã quen với nền giấy kem sáng (`#F2EEE4`).
  2. Đúng giây đọc câu kết luận đắt giá nhất, nền màn hình cắt cứng (`Hard Cut 0.05s` kèm tiếng *Low Sub-Bass Boom*) sang màu **Đen Tuyền (`#0A0A0A`)**, toàn bộ chữ chuyển sang trắng/vàng/đỏ tương phản cực đại.

### 2.4. `MAP_TRAJECTORY_CAMERA_FOLLOW` (Camera Đuổi Theo Đường Chấm Đứt Trên Bản Đồ)
- **Nguồn gốc**: Gu 1 (`gP4ihbNXFrY`).
- **Cơ chế hoạt động**:
  1. Đường chấm đứt (`dotted line`) hoặc mũi tên đỏ phóng đi từ điểm A sang điểm B trên bản đồ cổ.
  2. Camera dịch chuyển tâm (`pan X, Y`) bám theo đầu mũi tên hoặc nhân vật Figurine đang trượt đi, tạo cảm giác liền mạch không cần cắt cảnh.

### 2.5. `STAGGERED_UNIT_CASCADE` (Hiệu Ứng Domino Xếp Chồng Theo Nhịp)
- **Nguồn gốc**: Gu 1 (Lưới 100 hình người `12%`) & Gu 2 (8 cọc tiền đô la xếp ngang).
- **Cơ chế hoạt động**:
  - Các phần tử con không hiện ra cùng một lúc mà trễ nhau `0.04s – 0.06s` (`stagger delay`), tạo thành làn sóng từ trái sang phải hoặc từ dưới lên trên.

### 2.6. `VISUAL_RELAY_ENTER_HOLD_EXIT` (Tiếp Sức Thị Giác — Tối Đa 3 Phần Tử Cùng Lúc)
- **Quy luật bất di bất dịch**:
  - Mỗi phân cảnh dài `12s – 25s` phải chia thành **2 đến 4 nhịp tư liệu (`01.1 -> 01.2 -> 01.3 -> 01.4`)**.
  - Khi cặp tư liệu của vế câu sau (`01.3`, `01.4`) đi vào, cặp tư liệu của vế câu trước (`01.1`, `01.2`) bắt buộc phải trượt thoát nhẹ nhàng (`opacity: 1 -> 0, translateY: 0 -> -18px` trong `0.22s`).
