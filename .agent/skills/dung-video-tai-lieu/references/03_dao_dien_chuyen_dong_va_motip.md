# Bước 3: Kiến Trúc 5 Thế Giới Thị Giác (`v2.0`), Bất Đối Xứng Bố Cục & Động Cơ Vết Cắt (`ledger.json`)

> **Đọc file này khi:** Thiết kế `ledger.json` và `chi_dao_phan_canh.json` (`storyboard.json`). Kế thừa trực tiếp từ `story.md` (§5 Worlds), `motion-doctrine`, `cut-the-curve` của HeyGen HyperFrames, `remotion-maps`, `remotion-data-viz` và `sound-design.md`.

---

## 1. Ma Trận 5 Thế Giới Thị Giác (`world_type` / `scene_motif` — Xóa Bỏ Căn Bệnh Bàn Polaroid 2 Cột)

Để một bộ phim tài liệu dài **5–30+ phút** cuốn hút như **Johnny Harris, Vox, Lemmino, MagnatesMedia**, mỗi cảnh (`sc_01`, `sc_02`...) bắt buộc phải bước vào một **Thế Giới Thị Giác (`world_type`)** khác hẳn cảnh trước cả về **không gian nền, tỷ lệ khung hình, bố cục tọa độ và sự hiện diện của HUD**:

| Mã `world_type` (hoặc `scene_motif`) | Không gian Sân khấu & HUD (`Stage & Atmosphere`) | Quy tắc Tọa độ & Phần tử Chủ đạo (`Hero Layout & Beats`) |
| :--- | :--- | :--- |
| **`WORLD_1_FULL_MAP`**<br>(`MOTIF_3_CARTOGRAPHIC_3D_FLYOVER`) | **Bản Đồ Địa Chính Trị Toàn Màn Hình (`1920x1080`):** Bản đồ phóng tràn toàn bộ hoặc `90%` sân khấu (`x=0..80, y=0..60, w=1760..1920, h=960..1080`), tắt khung viền Polaroid trắng để người xem chìm hẳn vào địa hình. | Bản đồ nền full-bleed + `MAP_ROUTE` (đường hành trình đứt nét vẽ động nối từ tọa độ `[x1,y1]` $\rightarrow$ `[x2,y2]` kèm ghim radar & nhãn dặm/km) + `HANDWRITTEN_CALLOUT` hoặc `STAMP`. |
| **`WORLD_2_CINEMA_FULLBLEED`**<br>(`MOTIF_2_BROLL_KINETIC_OVERDRIVE`) | **Điện Ảnh Tư Liệu Tràn Viền (`Letterbox 2.35:1`):** Video B-Roll hoặc Ảnh lịch sử bung tràn **100% khung hình (`x=0, y=0, w=1920, h=1080`)**, bật 2 thanh đen điện ảnh trên/dưới (`90px`), tắt lưới bàn giấy. | `VIDEO_CLIP` / `POLAROID` (`full_bleed: true`) + `SPOTLIGHT_XRAY` (làm tối `68%` xung quanh, chiếu sáng tiêu điểm kèm nhãn thuyết minh) hoặc `HEADLINE` nổi trên nền tối điện ảnh + `STICKER` nhân vật tiền cảnh. |
| **`WORLD_3_DETECTIVE_CANVAS`**<br>(`MOTIF_1_DETECTIVE_CANVAS_PAN`) | **Bàn Điều Tra Phóng Sự Đa Điểm & Dây Đỏ:** Mặt bàn giấy nhăn có lưới tọa độ. **CẤM lặp lại công thức đặt Polaroid ở `x=110`!** Phải đảo chiều (Ảnh bên phải `x=1020`, chữ bên trái `x=100`; hoặc 2 bằng chứng nối nhau bằng sợi chỉ đỏ). | `POLAROID` + `RED_STRING_LINK` (sợi chỉ đỏ căng giữa 2 đinh ghim nối bằng chứng A sang bằng chứng B) + `DETECTIVE_TAPE_NOTE` + `RED_INK_CIRCLE`. |
| **`WORLD_4_DATA_STAGE`**<br>(`MOTIF_5_DATA_STORY_PROGRESSION`) | **Sân Khấu Dữ Liệu Tối Giản Toàn Màn Hình (`Dark/Cream Data Stage`):** **KHÔNG CÓ ẢNH POLAROID CHIA ĐÔI MÀN HÌNH!** Toàn bộ trung tâm màn hình (`x=220..260, y=150..180, w=1400, h=620`) dành trọn cho đại cảnh dữ liệu biến hình. | `TIMELINE_SCROLLER` (thước phim niên đại chạy ngang qua các mốc năm) HOẶC `SVG_LINE_CHART` (biểu đồ đường vẽ dần theo thời gian kèm điểm nổ đỏ) HOẶC `WAFFLE_100_ARRAY` / `ROUGH_EDGE_BARS` khổ đại (`w=1360`). |
| **`WORLD_5_ARCHIVE_XRAY`**<br>(`MOTIF_4_EVIDENCE_SPLIT_COLLISION`) | **Soi Hiển Vi Văn Kiện Báo Chí / Đối Đầu Trực Diện:** Phóng đại tờ báo cổ / sắc lệnh lịch sử ở trung tâm hoặc chia đôi màn hình bằng vết rách giấy `TORN_PAPER_SPLIT`, dùng đèn chiếu `SPOTLIGHT_XRAY` hoặc vệt bút dạ quang quét trực tiếp câu trích dẫn. | Văn kiện trung tâm (`x=280..420, w=1080..1360`) + `SPOTLIGHT_XRAY` (khung sáng soi dòng chữ báo chí) hoặc `TORN_PAPER_SPLIT` + `STAMP` chốt hạ. |

---

## 2. Luật Bất Đối Xứng Tọa Độ (`LAYOUT_ASYMMETRY_GATE` — Chống Quen Mắt 100%)

1. **Cấm đặt Tư liệu chính (`Hero Asset`) ở góc trái (`x < 350`, `w < 1200`) quá 2 cảnh liên tiếp!**
2. Mỗi phần (`7–9` cảnh) bắt buộc xoay vòng 4 kiểu bố cục không gian (`layout_mode`):
   - `FULL_BLEED` (`x=0, y=0, w=1920, h=1080` — Chiếm 100% khung hình, dùng cho `WORLD_1_FULL_MAP` và `WORLD_2_CINEMA_FULLBLEED`).
   - `CENTER_STAGE` (`x=240..360, y=140..170, w=1200..1440, h=620..680` — Sân khấu trung tâm, dùng cho `WORLD_4_DATA_STAGE` và `WORLD_5_ARCHIVE_XRAY`).
   - `RIGHT_ANCHOR` (Tư liệu hình ảnh nằm bên phải `x=960..1060`, thẻ phân tích/ghi chú nằm bên trái `x=90..120`).
   - `LEFT_ANCHOR` (Tư liệu hình ảnh nằm bên trái `x=90..130`, thẻ phân tích nằm bên phải `x=920..980` — **Chỉ được phép dùng tối đa 25%–30% số cảnh trong 1 phần!**).

---

## 3. Kho 16 Hiệu Ứng Thị Giác Chuẩn Quốc Tế (`beats[].type`)

Ngoài 12 hiệu ứng của bản `v1.0`, bản `v2.0` bổ sung **4 Vũ Khí Đồ Họa Động Toàn Màn Hình** lấy cảm hứng từ `remotion-maps`, `remotion-data-viz` và `Vox Archive`:

1. **`MAP_ROUTE` (Đường Hành Trình Bản Đồ Động — Johnny Harris Style):**
   - Vẽ đường cong/đường đứt nét chạy dần từ điểm xuất phát `(from_x, from_y)` tới điểm đích `(to_x, to_y)` (tọa độ tương đối trên khung `1920x1080`), kèm vòng tròn radar phát sáng ở 2 đầu, nhãn địa danh (`from_label`, `to_label`) và hộp khoảng cách (`distance_label`, VD: `"1,700 MILES • 8 MONTHS"`).
2. **`SPOTLIGHT_XRAY` (Đèn Chiếu Tiêu Điểm & Phóng Đại Báo Chí — Vox / Lemmino Style):**
   - Phủ lớp mặt nạ tối mờ (`dim_alpha: 0.68`) lên toàn bộ bức ảnh/video nền, chỉ khoét sáng một khung tiêu điểm tại `(x, y, w, h)` với viền vàng/đỏ sắc nét và thẻ chú thích phóng sự (`label`, `sub`).
3. **`TIMELINE_SCROLLER` (Thước Đo Niên Đại Điện Ảnh — Johnny Harris / Fern Style):**
   - Một trục thời gian ngang khổ lớn (`x=180, y=220, w=1560, h=460`) hiển thị chuỗi các mốc năm lịch sử (`events: [{"year": "1867", "title": "PURCHASE"}, {"year": "1896", "title": "KLONDIKE GOLD"}, ...]`), trong đó kim chỉ đỏ và khung sáng trượt mượt tới năm mục tiêu (`active_year`).
4. **`SVG_LINE_CHART` (Biểu Đồ Đường Tăng Trưởng/Sụp Đổ Động — Remotion Data-Viz Style):**
   - Khung biểu đồ khổ lớn vẽ đường gấp khúc chạy từ trái sang phải theo thời gian thực (`points: [{"label": "1896", "value": 10}, ...]`), có vùng tô bóng dưới đường biểu đồ, đường tham chiếu ngang và điểm nổ đỏ tại cột mốc cao trào (`peak_note`).
5. **`RED_STRING_LINK` (Sợi Chỉ Đỏ Hồ Sơ Thám Tử — Detective Board Style):**
   - Căng một sợi chỉ đỏ vật lý có bóng đổ nối từ đinh ghim `(from_x, from_y)` của bằng chứng A sang đinh ghim `(to_x, to_y)` của bằng chứng B kèm nhãn mối liên hệ (`label`).

---

## 4. Động Cơ Chuyển Cảnh Bảo Toàn Động Lượng Thật (`True Velocity-Matched Seam Engine`)

Tại ranh giới `0.32s` cuối Cảnh A và `0.38s` đầu Cảnh B, cả `index.html` lẫn `buoc_5_xuat_video_mp4.py` thực thi biến đổi vật lý thật theo `seam_transition` của cảnh:
- `ZOOM_THROUGH`: Phóng xuyên tâm (`scale 1.0 -> 1.28` + nhòe Gaussian) $\rightarrow$ Cảnh sau đón từ `scale 0.78 -> 1.0`.
- `INVERSE_ZOOM`: Thu lùi (`scale 1.0 -> 0.82`) $\rightarrow$ Cảnh sau chụp từ `scale 1.24 -> 1.0` xuống mặt phẳng nét.
- `CUT_THE_CURVE_LEFT`: Trượt ngang có đà `230px` sang trái theo đường cong `power4`.
- `RACK_FOCUS_BLUR`: Đẩy độ nhòe ống kính DSLR lên `14px` ngay tại điểm cắt rồi lấy nét lại ở cảnh mới.
- `PAPER_RIP_WIPE`: Quét dải giấy xé ngang màn hình mở ra Thế giới mới.
