# Bước 3: 5 Mô-Típ Dàn Dựng Sinh Động, Dòng Chảy Máy Quay & Sổ Cái Vết Cắt (`ledger.json`)

> **Đọc file này khi:** Thiết kế `ledger.json` và `chi_dao_phan_canh.json` (`storyboard.json`). Kế thừa trực tiếp từ `motion-doctrine` và `cut-the-curve` của HeyGen HyperFrames.

## 1. Ma Trận 5 Mô-Típ Dàn Dựng Sinh Động (`scene_motif` — Cấm 2 Cảnh Liền Kề Trùng Nhau)

Mỗi Phân cảnh (`SC_01`, `SC_02`...) bắt buộc chọn 1 trong 5 Mô-típ sau sao cho `scene[i].scene_motif != scene[i-1].scene_motif`:

| Mã `scene_motif` | Bản chất Thị giác & Cách Máy Quay Diễn (`camera_move`) | Tổ hợp Phần tử Chủ đạo (`beats[]`) |
| :--- | :--- | :--- |
| **`MOTIF_1_DETECTIVE_CANVAS_PAN`** | **Bàn Thám Tử & Máy Quay Lia Cận Cảnh:** Mở góc rộng mặt bàn rồi đẩy ống kính (`DESK_PAN_ZOOM`: `scale 1.0 -> 1.18`) lia từ manh mối `XX.1` sang `XX.2`. | `POLAROID` + `RED_INK_CIRCLE` (khoanh mực đỏ) + `HANDWRITTEN_CALLOUT` (chữ viết tay mũi tên cong) + `DETECTIVE_TAPE_NOTE`. |
| **`MOTIF_2_BROLL_KINETIC_OVERDRIVE`** | **Video B-Roll Thật Chiếm Lĩnh + Đại Tự Gạch Bỏ:** Băng tư liệu chuyển động thật (`VIDEO_CLIP`) chiếm `65%–85%` khung hình (`KEN_BURNS_PUSH`). | `VIDEO_CLIP` + `STICKER` (nhân vật tách nền nổi khối ở tiền cảnh) + `HEADLINE` 3 tầng có `strikethrough` gạch đỏ lầm tưởng cũ. |
| **`MOTIF_3_CARTOGRAPHIC_3D_FLYOVER`** | **Sa Bàn Bản Đồ Chiến Thuật & Đường Bay Động:** Nền `PARCHMENT_MAP`, máy quay (`MAP_FLYOVER_TRACK`) trượt theo hành trình địa lý từ vùng A sang vùng B. | Bản đồ lịch sử + `HANDWRITTEN_CALLOUT` chỉ điểm + `STAMP` (`radar_ring: true` có vòng tròn nét đứt xoay). |
| **`MOTIF_4_EVIDENCE_SPLIT_COLLISION`** | **Đối Đầu Trực Diện / Xé Giấy Chia Đôi Màn Hình:** Hai thái cực (Xưa vs Nay / Giá rẻ vs Giá trị thật) lao vào từ 2 phía đối lập. | `TORN_PAPER_SPLIT` (vết giấy xé dọc chính giữa `x: 915`) + 2 tư liệu đối xứng + `STAMP` đóng chốt hạ giữa vết xé. |
| **`MOTIF_5_DATA_STORY_PROGRESSION`** | **Kể Chuyện Bằng Số Liệu Biến Đổi 3 Nhịp:** Không hiện biểu đồ tĩnh! Biểu đồ biến đổi nhân quả theo 3 nhịp giọng đọc liên tiếp (có thể bật `bg_mode: "DARK_CLIMAX"` ở cảnh cao trào). | Nhịp 1: `NUMBER_COUNTER` mồi $\rightarrow$ Nhịp 2: `WAFFLE_100_ARRAY` (100 hình người) hoặc `ROUGH_EDGE_BARS` vọt lên $\rightarrow$ Nhịp 3: `RED_INK_CIRCLE` khoanh điểm bất thường. |

---

## 2. Định Luật Bảo Toàn Động Lượng Qua Vết Cắt (The Vector Law & `ledger.json`)

Để bộ phim dài 3 phút mượt như **một cú máy liên hoàn (One Continuous Camera Flow)** thay vì các slide PowerPoint rời rạc, trước khi dựng phải lập **Sổ Cái Vết Cắt (`ledger.json`)** theo 4 quy luật vật lý:

1. **Cùng Trục (`Axis`) & Cùng Chiều (`Direction`):** Cảnh A thoát ra theo trục nào (`X`, `Y`, hoặc `Z`) thì Cảnh B phải lao vào theo đúng trục và chiều đó. Cấm đảo chiều kiểu bóng bàn (ping-pong) nếu không có lực va chạm.
2. **Quy tắc Dấu Tỷ Lệ trên Trục Z (`Z Scale-Sign Rule`):**
   - **Đẩy tới (`ZOOM_THROUGH` — dấu `+`):** Cảnh A phóng to xuyên qua ống kính (`scale: 1.0 -> 1.22`, `blur: 0 -> 10px`, `power3.in` trong `0.22s`) $\rightarrow$ Cảnh B bắt đầu từ nhỏ và tiếp tục lớn lên vào mặt phẳng nét (`scale: 0.75 -> 1.0`, `blur: 10px -> 0`, `expo.out` trong `0.48s`).
   - **Kéo lùi (`INVERSE_ZOOM_ARRIVAL` — dấu `-`):** Cảnh A thu nhỏ lùi xa (`scale: 1.0 -> 0.8`) $\rightarrow$ Cảnh B ập từ phía sau máy quay xuống (`scale: 1.25 -> 1.0`). **Cấm tuyệt đối** việc Cảnh A thu nhỏ (`-`) mà Cảnh B lại phóng từ nhỏ lên lớn (`+`)!
3. **Cắt Trên Đường Cong Vận Tốc (`CUT_THE_CURVE_LEFT` — Mặc định dòng chảy ngang):**
   - Chủ thể Cảnh A trượt sang trái một quãng ngắn `~12% khung hình` (`x: 0 -> -230px`, `power4.in`, mờ dần ở 30% quãng đường đầu); ngay tại đỉnh vận tốc, chủ thể Cảnh B lao từ `x: +230px -> 0` (`power4.out`) nối tiếp đúng vận tốc đó.
4. **Vật Dẫn Đường Qua Vết Cắt (`Carrier`):** Luôn chọn 1 vật thể (con số, tấm bản đồ, vết giấy xé `TORN_PAPER_WIPE`) làm cầu nối dẫn mắt người xem băng qua điểm cắt.

---

## 3. Cấu Trúc 12 Loại Phần Tử & Ghim Định Hướng 3 Góc (`chi_dao_phan_canh.json`)

- **3 Ghim Định Hướng Cấp Cảnh (Nằm ở mép biên an toàn, không tính vào hạn ngạch 3 phần tử trung tâm):**
  - `era_label` (Góc trên trái): Nhãn niên đại lịch sử (*Serif Bold Italic*, VD: `"1867 • ALASKA PURCHASE"`).
  - `source_footnote` (Góc dưới trái): Nguồn trích dẫn học thuật kiểu Vox (`"Source: U.S. Treasury Warrant • Library of Congress"`).
  - `hud_ticker` (Góc trên phải): Thẻ giấy xé đếm chỉ số xuyên cảnh (`{"label": "DEAL PRICE", "value": "2¢ / ACRE"}`).
- **12 Loại Phần Tử Trung Tâm (`beats[].type`):**
  `POLAROID`, `STICKER`, `VIDEO_CLIP`, `HEADLINE` (hỗ trợ `strikethrough`), `NUMBER_COUNTER`, `DETECTIVE_TAPE_NOTE`, `RED_INK_CIRCLE`, `STAMP` (hỗ trợ `radar_ring: true`), `TORN_PAPER_SPLIT`, `WAFFLE_100_ARRAY`, `ROUGH_EDGE_BARS`, `HANDWRITTEN_CALLOUT`.
