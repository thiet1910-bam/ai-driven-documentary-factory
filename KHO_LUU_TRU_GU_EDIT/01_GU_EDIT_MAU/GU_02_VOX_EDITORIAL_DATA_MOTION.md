# 📊 GU EDIT 02: VOX EDITORIAL DATA JOURNALISM & TACTILE CUTOUT MOTION
*(Phân tích từ Video mẫu: `https://www.youtube.com/watch?v=uIHJvUVaB34` — "Claude Opus 5.5 Is INSANE at Vox-Style Motion Graphics" / Kênh: RandomAI)*

> [!NOTE]
> **Bản chất thẩm mỹ (Core Aesthetic):** Phong cách **Đồ họa Báo chí Điều tra & Giải thích Dữ liệu kiểu Vox (Vox Explainer / Editorial Motion Graphics)**. Mọi khung hình đều giống như một trang tạp chí tài liệu sống động: kết hợp giữa **Giấy báo nhám ấm áp**, **Cắt dán báo chí có viền giấy xé răng cưa (Torn-Paper Cutouts)**, **Cặp phông chữ tương phản mạnh (Serif nghiêng + Condensed Sans đậm)**, **Biểu đồ số liệu có chất liệu vật lý**, và **Hệ thống âm thanh Foley chiếm 50% cảm xúc**.

---

## 1. BẢNG MÀU & CHẤT LIỆU NỀN (VOX EDITORIAL PALETTE)

| Thành phần | Mã màu Hex | Mô tả ứng dụng trong khung hình |
| :--- | :--- | :--- |
| **Nền Giấy Báo Sáng (Warm Editorial Cream)** | `#F2EEE4` $\rightarrow$ `#E5DFD0` | Nền chủ đạo cho 85% thời lượng, có độ nhám hạt giấy nhẹ (`paper grain`), lưới ô vuông mảnh ở rìa dưới (`subtle grid`) và bo tối nhẹ ở 4 góc (`radial vignette`). |
| **Nền Đảo Ngược Cao Trào (Climax Pitch Black)** | `#0A0A0A` | Đảo ngược toàn bộ màn hình sang màu đen tuyền ở câu chốt cuối cùng (`We're not paying for the FUTURE. We're paying for the PAST`), tạo cú sốc thị giác cực mạnh. |
| **Mực Đen Báo Chí (Editorial Ink Black)** | `#141414` | Màu chữ chính, thanh cột biểu đồ so sánh (`DEFENSE`), trục tọa độ và đường gạch ngang. |
| **Vàng Bút Dạ Quang (Vox Highlighter Yellow)** | `#F5C518` / `#FFDF2B` | Vệt bút dạ quét ngang từ khóa (`speeding up.`, `biggest bill`, `PAST`, `$1 TRILLION / YEAR`). |
| **Đỏ Báo Động Tài Chính (Editorial Crimson Red)** | `#D92318` | Con số/tiêu đề nguy cấp (`THE INTEREST`, `420+ PPM`, `$40 TRILLION`, thanh biểu đồ `#1 INTEREST`). |
| **Xanh Cobalt Nhấn Mạnh (Electric Editorial Blue)** | `#1D4ED8` / `#2546F0` | Dùng trong biến thể hiện đại để tô hộp chữ (`FREE VS. PAID`, `OPUS 5.5 + REMOTION`) hoặc từ khóa lớn (`project`, `low effort`). |
| **Chú Thích Nguồn Cố Định Ở Đáy (Footnote Grey)** | `#787267` | Dòng chữ nhỏ in nghiêng ở sát mép dưới bên trái (`Source: U.S. Treasury / Congressional Budget Office...`) tạo độ tin cậy tuyệt đối như báo chí chính thống. |

---

## 2. QUY TẮC TYPOGRAPHY PHỐI HỢP 3 TẦNG (THE 3-TIER VOX TYPOGRAPHY)

Điểm nhận diện đắt giá nhất của Gu 2 là **KHÔNG BAO GIỜ dùng 1 phông chữ đơn điệu cho cả câu**, mà chia 1 câu thành **3 tầng phông chữ tương phản**:

1. **Tầng 1 — Dẫn nhập cảm xúc (`Serif Italic`)**:
   - Phông chữ: *Instrument Serif Italic*, *Playfair Display Italic*, hoặc *Georgia Italic*.
   - Dùng cho nửa đầu câu mang tính kể chuyện: `"And it's..."`, `"The real problem is"`, `"the government's"`, `"We're not paying for the"`.
2. **Tầng 2 — Từ khóa bùng nổ (`Condensed Sans-Serif Bold` + `Marker Highlight` / `Underline`)**:
   - Phông chữ: *Bebas Neue*, *Anton*, *Oswald Bold*, hoặc *Impact*.
   - Dùng cho cụm từ trọng tâm ngay sau vế dẫn:
     - Quét nền vàng: `"And it's [speeding up.]"`, `"the government's [biggest bill]"`
     - In hoa đỏ + gạch chân: `"THE INTEREST"`
     - Gạch bỏ chữ cũ bằng nét đỏ (`Strikethrough`): `"~~FUTURE~~"` $\rightarrow$ hiện chữ mới trong hộp vàng `"PAST"`.
3. **Tầng 3 — Nhãn dữ liệu kỹ thuật (`Monospace / Typewriter`)**:
   - Phông chữ: *Courier Prime*, *IBM Plex Mono*, *Space Mono*.
   - Dùng cho tiêu đề phụ phía trên (`THE U.S. NATIONAL DEBT`, `BORROWED SINCE YOU HIT PLAY`), nhãn trục biểu đồ (`SEP 2017`, `AUG 2026`, `280 PPM`) và dòng trích dẫn nguồn ở đáy màn hình.

---

## 3. 8 CƠ CHẾ ĐỒ HỌA & CHUYỂN ĐỘNG ĐẶC TRƯNG (VOX MOTION MECHANICS)

1. **`TORN_PAPER_HUD_TICKER` (Thẻ Giấy Xé Đếm Số Thời Gian Thực Góc Trên Phải)**:
   - Ngay từ giây `00:00` (`"Before this video ends, America will borrow over 2 million more dollars"`), bộ đếm tiền `$53,973` xuất hiện giữa màn hình cùng thanh tiến trình `NOW ---------> END`.
   - Sau đó, bộ đếm này **thu nhỏ vào một mảnh giấy xé răng cưa (`torn paper card`) ghim cố định ở góc trên bên phải** (`BORROWED SINCE YOU HIT PLAY: $439,498` $\rightarrow$ `$825,024` $\rightarrow$ `$1,981,600`) và nhảy số liên tục suốt video!
2. **`TORN_PAPER_VERTICAL_SPLIT` (Chia Đôi Màn Hình Bằng Vết Giấy Xé Dọc)**:
   - Trong ví dụ CO2 (`200 YEARS AGO` vs `TODAY`), màn hình được chia đôi 50/50 bởi **một dải giấy xé răng cưa có đổ bóng 3D ở chính giữa**.
   - Bên trái: Tranh cắt rời làng quê xanh mát + lọ thủy tinh chứa 280 hạt đen (`280 PPM`).
   - Bên phải: Tranh cắt rời nhà máy khói bụi + lọ thủy tinh chứa 420 hạt đen & đỏ (`420+ PPM`).
3. **`PHYSICAL_UNIT_STACKING` (Xếp Chồng Vật Thể Cắt Rời Thay Cho Con Số Khô Khan)**:
   - Khi nói về nợ quốc gia hay ngân sách, thay vì chỉ viết chữ, hệ thống dùng **hình ảnh cắt rời các cọc tiền đô la xanh (`3D Cash Stacks`)** xếp thành hàng ngang và mọc chồng lên trên đỉnh cột biểu đồ (`DEFENSE` gắn hình máy bay chiến đấu cutout, `INTEREST` gắn cọc tiền cutout).
4. **`STEPPED_ACCELERATION_LINE_CHART` (Biểu Đồ Đường Có Khung Chú Thích Thời Gian)**:
   - Đường biểu đồ màu đỏ (`$40 TRILLION`) tự vẽ từ trái sang phải trên hệ trục tọa độ tối giản.
   - Phía dưới trục hoành có dấu ngoặc nhọn chỉ rõ khoảng cách thời gian: `SEP 2017 <---- under 9 years ----> AUG 2026`.
5. **`ROUGH_EDGE_HORIZONTAL_BARS` (Biểu Đồ Thanh Ngang Có Viền Giấy Xé Nhám)**:
   - Khi so sánh 4 khoản chi lớn nhất năm `2048 [PROJECTED]`, 4 thanh ngang (`#1 INTEREST`, `SOCIAL SECURITY`, `MEDICARE`, `DEFENSE`) phóng ra từ trái sang phải. Đặc biệt, **mép viền của cả 4 thanh đều có độ nhám răng cưa như xé từ giấy màu** chứ không phẳng lì như đồ họa công nghiệp, đi kèm nhãn vàng dán nghiêng `BIGGEST BILL`.
6. **`TORN_RECEIPT_DOCUMENT_CARD` (Thẻ Hóa Đơn / Bảng Kê Giấy Xé Nằm Nghiêng)**:
   - Bên trái biểu đồ cột là một tờ phiếu giấy trắng có mép dưới xé răng cưa (`U.S. FEDERAL BUDGET`), trong đó dòng `INTEREST — $1 TRILLION / YEAR` được tô bút dạ vàng toàn bộ dòng.
7. **`CLIMAX_DARK_INVERT_WITH_CUTOUT` (Đảo Ngược Nền Đen & Vật Thể Ẩn Dụ Cuối Cảnh)**:
   - Ở câu kết luận triết lý, nền kem lập tức chuyển sang **Đen Tuyền (`#0A0A0A`)**. Bên trái là chữ tương phản `~~FUTURE~~` $\rightarrow$ `PAST` cùng tổng số tiền đỏ rực `$2,367,125`; bên phải là một chiếc **đồng hồ cát cổ điển tách nền sắc nét (`Hourglass Cutout`)** đang chảy những hạt cát cuối cùng.
8. **`COLORFUL_HALFTONE_CUTOUTS` (Ảnh Cắt Rời Rực Rỡ Có Viền Trắng Mỏng)**:
   - Các đối tượng minh họa (quả địa cầu, mặt trăng, phi hành gia, Vạn Lý Trường Thành, lọ thủy tinh CO2) được tách nền sạch tuyệt đối, tăng độ bão hòa màu (`vibrant color`) để nổi bật trên nền giấy kem trung tính.
