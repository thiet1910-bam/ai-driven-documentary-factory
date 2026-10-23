# NHẬT KÝ TƯ DUY & TIẾN HÓA HỆ THỐNG DỰNG VIDEO TÀI LIỆU AI (MINDSET & EVOLUTION LOG)

> **MỤC ĐÍCH TỐI THƯỢNG CỦA TÀI LIỆU NÀY**:
> Tài liệu này là **Bộ Nhớ Dài Hạn (Institutional Memory)** của hệ thống sản xuất video tài liệu **Sử Để Hiểu Studio**. Mọi phiên làm việc AI mới hoặc bất kỳ nhân sự nào tiếp nhận bộ Skill `.agent/skills/dung-video-tai-lieu/` **BẮT BUỘC** phải đọc file này trước tiên để kế thừa toàn bộ tư duy, tránh lặp lại 100% các sai lầm cũ và dựng ra ngay sản phẩm đạt chuẩn thẩm mỹ **Đạo Diễn Chuyên Nghiệp (9.5–10/10)** ngay từ lần chạy đầu tiên.

---

## PHẦN I. LỊCH SỬ TIẾN HÓA QUA 4 VÒNG PHẢN BIỆN KHẮT KHE CỦA NGƯỜI DÙNG

### Vòng 1: Khủng hoảng "Làm Gộp Một Cục & Lưu File Bừa Bãi" (Điểm: 2/10)
- **Sai lầm của AI ban đầu**:
  1. Cố gắng nuốt trọn kịch bản và voice dài 10–45 phút trong một lượt chạy, không có cổng dừng báo cáo.
  2. Tải nguyên liệu hàng loạt và đặt tên tự do (`alaska.jpg`, `tsar.png`), dẫn đến khi kéo vào dòng thời gian (Timeline), người dùng không biết ảnh nào ứng với câu thoại nào, nguồn từ đâu.
- **Chỉ đạo & Phản biện của Người dùng**:
  - Bắt buộc chia thành **6 Pha có 6 Cổng Dừng Cứng (`🛑 CỔNG DỪNG 0 -> 5`)**. Xong mỗi Pha phải xuất báo cáo và dừng lại chờ duyệt.
  - **Pha 1**: Phải lấy Kịch bản làm tham chiếu ý nghĩa để cắt Voice + Text dài (10–45 phút) thành từng Phần nhỏ (`phan_01`, `phan_02`... dài `1.5 – 3.0 phút/phần`).
  - **Pha 2**: Chỉ làm cuốn chiếu từng Phần. Lập Bảng Đạo Diễn có **Mã STT cố định (`01_`, `02_`, `03_...`)**, mốc giây, lời thoại, cảnh cần tìm, định dạng, từ khóa AI và nguồn dự kiến.
  - **Pha 3**: Đi săn nguyên liệu và **lưu tên file gắn cứng theo đúng mã STT của Pha 2** (`01_00m00s_polaroid_...jpg`), kiểm duyệt bằng mắt AI (`read_file`) và báo cáo phương án thay thế nếu không có.

---

### Vòng 2: Khủng hoảng "Bàn Dựng Vỡ Bố Cục, Câm Tiếng Động & Thiếu Tính Năng Kéo Thả" (Điểm: 0/10 $\rightarrow$ 6/10)
- **Sai lầm của AI ở bản dựng HTML đầu tiên**:
  1. Đưa các nhãn quản lý nội bộ (`[STT 01]`, ghi chú tiếng Việt) đè thẳng lên khung hình video `1920x1080`.
  2. Không kêu tiếng động SFX, không có hiệu ứng chuyển động khi phần tử xuất hiện, video clip `.mp4` 4s bị đứng hình/trắng xóa do dùng `innerHTML = ''` xóa DOM mỗi khung hình.
  3. Không tua/kéo được thanh thời gian, không kéo thả được tọa độ ảnh trên màn hình, và thiếu thanh Phụ đề Song ngữ (EN + VI) có thể bật/tắt.
- **Giải pháp kỹ thuật đã khắc phục**:
  - Giải mã toàn bộ `phan_XX_voice.mp3` và `sfx/*.wav` vào RAM bằng `Web Audio API`, giữ DOM bền vững (`Persistent DOM + GSAP`), cho phép kéo thả tọa độ trực tiếp và bật/tắt phụ đề song ngữ.

---

### Vòng 3 & Vòng 4: Bước Nhảy Vọt Quyết Định — Xóa Bỏ "Đống Tạp Nham Tích Tụ", Xóa Nhãn Rác `SC_01` & Biến AI Thành Đạo Diễn Tự Mở Video Kiểm Duyệt Bằng Mắt

- **Phản biện sắc bén của Người dùng (Kèm 2 ảnh chụp màn hình bằng chứng tại `SC_02` và `SC_03`)**:
  1. **Lỗi 1 — Spam Hiệu Ứng Lặp Lại Vô Nghĩa & Thiếu Kho Hiệu Ứng Thật**:
     - Khi được yêu cầu tăng nhịp dựng lên 2–3s/nhịp, AI đã mắc bệnh **"Spam Công Thức Máy Móc"**: Cảnh nào cũng ném đúng 1 công thức (`1 Polaroid + 1 Hộp chữ trắng + 1 Mũi tên đỏ lơ lửng chẳng chỉ vào đâu + 1 Hộp số đen + 1 Giấy vàng + 1 Con dấu đỏ`). Kính lúp ở `SC_03` thì đặt lệch ra mép giấy trắng chứ không soi đúng vào tảng băng; tiếng động SFX thì kêu liên thanh gây nhàm chán.
  2. **Lỗi 2 — Nhãn Kỹ Thuật `SC_01`, `SC_02`, `SC_03` Xuất Hiện Trên Video**:
     - Ở góc trên bên trái khung hình `1920x1080` lại hiện thanh chữ `[SC_02] THE BASEMENT TREASURE...`, `[SC_03] 1867 PRESS MOCKERY...` — đây là mã quản lý kỹ thuật của Editor, tuyệt đối không được phép nằm trong khung hình phim!
  3. **Lỗi 3 — Tích Tụ Thành "Một Đống Tạp Nham" Ở Cuối Cảnh (`Junk Pile Accumulation` tại `SC_02`)**:
     - Sai lầm chí mạng nhất: AI cho các thẻ chữ, hộp số, mũi tên, giấy ghi chú, con dấu xuất hiện cách nhau 2 giây nhưng **TẤT CẢ ĐỀU ĐỂ `t1` ĐẾN HẾT CẢNH (`t1 = 22.2s`)**!
     - Hệ quả: Hộp sau hiện ra không thay thế hộp trước mà chất đống lên nhau (`$500+ BILLION` bị tờ giấy vàng `PUBLIC REACTION` đè lên, rồi đè tiếp lên con dấu `PRICE: 2¢ / ACRE`), biến màn hình ở cuối `SC_02` thành một bãi rác thị giác!
     - **Chân lý Đạo diễn**: *"Có những hiệu ứng hình ảnh, text, đồ họa xuất hiện xong là phải thoát đi (`t1` kết thúc sớm)! Không cần thiết giữ lại thì hiện xong là hết, nhường chỗ sạch sẽ cho thông tin tiếp theo!"*
  4. **Lỗi 4 — AI Chưa Tự Mở Video Ra Xem Bằng Mắt Trong Vai Trò Đạo Diễn Trước Khi Giao Cho Người Dùng**:
     - Trước đây AI chỉ chạy script kiểm tra số học trên file JSON mà không tự chụp khung hình thật của video ra để ngắm bằng mắt (`read_file`), nên người dùng phải tự chụp màn hình chỉ ra lỗi.
     - **Mục tiêu cốt lõi của Skill**: Biến AI thành một **Tổng Đạo Diễn & Editor Chuyên Nghiệp** — sau khi dựng xong, AI bắt buộc phải tự mở trình duyệt chụp các khung hình thực tế (`scripts/pha-4-dao-dien-tu-xem-va-kiem-duyet.py`), dùng mắt AI (`read_file`) soi từng khung hình ở đầu/giữa/cuối cảnh, tự phát hiện lỗi đè chữ/tạp nham và tự sửa sạch sẽ 100% trước khi báo cáo ở `🛑 CỔNG DỪNG 4`!

---

### Vòng 5: Khủng hoảng "Đói Tư Liệu Hình Ảnh (`1 Cảnh = 1 Ảnh`)" & Cuộc Cách Mạng "File Chỉ Đạo Phân Cảnh Hợp Nhất Ở Pha 2" (`Master Director Script = Single Source of Truth cho cả Pha 2, Pha 3, Pha 4`)
- **Phản biện sắc bén & Chỉ đạo kiến trúc của Người dùng**:
  1. **Về mật độ tư liệu hình ảnh (`01.1`, `01.2`, `01.3`...)**:
     - *"1 Phần được chia ra nhiều Phân cảnh (`SC_01`, `SC_02`...). Trong 1 Phân cảnh, chỉ có 1 hình ảnh tư liệu xuất hiện thì quá ít! Ví dụ câu: `'Imagine selling your house for $7 and then finding out there was a gold mine in the basement'` — câu này có hàng loạt hình ảnh thực thể: **Ngôi nhà bán đi, Tờ tiền $7, Tầng hầm, Mỏ vàng**... Tại sao chỉ lấy đúng 1 ảnh, 1 video hoặc 1 sticker mà không tách thành các mã tư liệu con `01.1_00m00s_...`, `01.2_00m03s_...`?"*
  2. **Về Kiến trúc "File Chỉ Đạo Phân Cảnh Hợp Nhất" từ Bước 2 (Pha 2) xuyên suốt sang Bước 3 (Pha 3) và Bước 4 (Pha 4)**:
     - *"Cần phải tạo **File Chỉ Đạo Phân Cảnh ở Bước 2 (Pha 2) thật tốt**. Đồng thời chúng ta phải **sử dụng chính File Chỉ Đạo Phân Cảnh này để đi tìm nguyên liệu ở Bước 3 (Pha 3) VÀ để dựng/edit luôn ở Bước 4 (Pha 4)**!"*
- **Phản biện Khắt Khe & Giải Pháp Gốc Rễ theo 3 Guru (`GURU.md`)**:
  1. **Ray Dalio (Minh bạch triệt để — Nói thẳng 2 căn bệnh cấu trúc của hệ thống cũ)**:
     - **Bệnh 1 — Lười biếng thị giác ở Pha 2**: Một phân cảnh dài `10 – 15 giây` chứa tới `3 – 4 hình ảnh thực thể` trong lời thoại, nhưng AI chỉ đi tải đúng **1 tấm ảnh duy nhất** (`01_00m00s_polaroid_alaska_check.jpg`) ghim chết một chỗ suốt 11 giây, rồi lấy 3–4 cái hộp chữ (`HEADLINE`, `COUNTER`, `NOTE`) đắp vào để "ăn gian" nhịp 2.5 giây! Thậm chí ở giây `0.0s -> 4.5s`, lời thoại đang nói chuyện ẩn dụ *"bán căn nhà giá $7 và mỏ vàng dưới tầng hầm"* (chưa hề nhắc chữ Alaska), nhưng AI đã vứt ngay tấm séc Alaska 7.2 triệu đô ra làm lộ hết bất ngờ (spoil).
     - **Bệnh 2 — Đứt gãy dữ liệu giữa Pha 2, Pha 3 và Pha 4 (`3 File rời rạc, mỗi Pha tự bịa lại từ đầu`)**:
       - Ở hệ thống cũ: Pha 2 xuất ra `ke_hoach_dao_dien_pha_2.md` (chỉ có bảng chữ sơ sài) + `manifest.json` (chỉ có từ khóa tìm ảnh). Sang Pha 3 tải ảnh xong, đến **Pha 4 Editor lại phải ngồi viết mới hoàn toàn một file `storyboard.json` khác** (lúc này mới tự nghĩ ra tọa độ `x, y, w, h`, lúc này mới tự thêm hiệu ứng `HEADLINE`, `STAMP`, `SFX`, lúc này mới gán `t0, t1`)!
       - **Hậu quả**: Những gì Đạo diễn chỉ đạo ở Pha 2 và những gì Editor dựng ở Pha 4 **không phải là một bản thiết kế duy nhất**! Đạo diễn duyệt ở Pha 2 một đằng, sang Pha 4 Editor lại tự chế hiệu ứng một nẻo gây ra đống tạp nham.
  2. **Elon Musk (Tư duy Nguyên lý Gốc rễ — Giải pháp "Một Bản Thiết Kế Tối Thượng Duy Nhất: `chi_dao_phan_canh.json`")**:
     - **Tại sao phải tách rời file kế hoạch Pha 2, file săn nguyên liệu Pha 3 và file dựng Pha 4?** Bản chất cả 3 Pha đều xoay quanh **cùng một cấu trúc bộ phim**!
     - **Giải pháp Kiến trúc Gốc Rễ — `FILE CHỈ ĐẠO PHÂN CẢNH HỢP NHẤT (Master Director Blueprint)`**:
       Ngay tại **Bước 2 (Pha 2)**, Đạo diễn & Biên kịch AI phải tạo ra bộ đôi đồng bộ **`chi_dao_phan_canh.md`** (bản trình bày trực quan cho Người dùng duyệt) và **`chi_dao_phan_canh.json`** (bản dữ liệu gốc duy nhất — Single Source of Truth) chứa trọn vẹn **100% thông tin cho cả Pha 3 lẫn Pha 4**:
       - **Cấp Phân cảnh (`scenes`: `SC_01`, `SC_02`...)**: Chia theo luận điểm câu chuyện (`8 – 20s`).
       - **Cấp Nhịp Tư liệu Con (`sub_assets`: `01.1`, `01.2`, `01.3`, `01.4`...)**: Bóc tách từng vế câu thành `2 – 4 tư liệu thực tế (Ảnh / Sticker / Video)` kèm sẵn:
         1. **Thông số cho Pha 3 (Săn nguyên liệu)**: `stt_id` (`01.1_00m00s_...`), `asset_type` (`POLAROID` / `STICKER` / `VIDEO_CLIP`), `search_queries` (danh sách từ khóa chính + từ khóa dự phòng `_alt2`, `_alt3` có khóa niên đại lịch sử), `expected_source`, và `expected_save_path`.
         2. **Thông số chỉ đạo sẵn cho Pha 4 (Bàn dựng HTML)**: Định nghĩa sẵn ngay từ Pha 2 **Vòng đời Vào - Giữ - Thoát (`t0 -> t1`)**, **Bố cục vùng hiển thị (`slot: LEFT_MAIN | RIGHT_MAIN | CENTER_FOCUS`, tọa độ `x, y, w, h, rot`)**, **Hiệu ứng đi kèm (`companion_fx` như khoanh mực đỏ, nhãn số)** và **Tiếng động Foley có lý do ngữ nghĩa (`sfx` + `sfx_reason`)**!
       - **Luồng vận hành liền mạch `Pha 2 -> Pha 3 -> Pha 4` không cần viết lại**:
         - **Ở Pha 2**: Đạo diễn & Biên kịch lập `chi_dao_phan_canh.json` + `.md` $\rightarrow$ Kiểm tra sẵn không quá 3 phần tử cùng lúc (`max_concurrent <= 3`) ngay trên giấy!
         - **Sang Pha 3**: Script săn nguyên liệu đọc thẳng `chi_dao_phan_canh.json`, tự động tải toàn bộ `01.1`, `01.2`, `01.3`, `01.4`... và điền đường dẫn file thực tế (`verified_src`) + kết quả Đạo diễn soi mắt (`director_eye_check`) ngược vào chính file đó!
         - **Sang Pha 4**: Bàn dựng HTML (`index.html`) đọc thẳng từ `chi_dao_phan_canh.json` (hoặc ánh xạ 1:1 sang `storyboard.json`) để hiển thị ngay lập tức theo đúng 100% ý đồ Đạo diễn đã chốt ở Pha 2!
  3. **Charlie Munger (Tư duy Ngược — Nếu gộp tất cả vào File Chỉ Đạo Phân Cảnh ở Bước 2 mà làm SAI thì rủi ro gì, và cách khóa chặt?)**:
     - *Rủi ro 1 — Bảng báo cáo Pha 2 quá rối mắt cho Người dùng nếu đổ hết tọa độ kỹ thuật (`x=100, y=140`) ra bảng Markdown*:
       - **Giải pháp chặn đứng**: Tách rõ **2 lớp hiển thị từ cùng 1 nguồn**:
         - File **`chi_dao_phan_canh.json`** lưu đầy đủ tọa độ `x, y, w, h` cho máy chạy ở Pha 3 & Pha 4.
         - Bảng báo cáo **`chi_dao_phan_canh.md`** trình Người dùng ở `🛑 CỔNG DỪNG 2` dùng ngôn ngữ Đạo diễn dễ đọc: cột `Mã Phân Cấp (01.1, 01.2)` | `Mốc Giây Vào -> Thoát` | `Vế Câu Thoại` | `Chỉ Đạo Hình Ảnh & Vị Trí Bố Cục (Trái/Phải/Giữa + Hiệu ứng đi kèm)` | `Định Dạng` | `Từ Khóa Săn Đa Nguồn (Chính & Dự phòng)`.
     - *Rủi ro 2 — Ảnh thực tế tải về ở Pha 3 có tỷ lệ khung hình (ngang/dọc) khác dự kiến ở Pha 2*:
       - **Giải pháp chặn đứng**: Ở Pha 3, sau khi tải ảnh thật về và biết kích thước thật (`width x height`), script tự động tinh chỉnh nhẹ khung `w, h` trong file chỉ đạo để ảnh dọc không bị cắt mất đầu nhân vật lịch sử, rồi Đạo diễn mở Browser ở Pha 4 kiểm tra lại bằng mắt!
     - *Rủi ro 3 — Tích tụ "Bãi rác Ảnh" khi tăng số lượng ảnh lên `01.1, 01.2, 01.3, 01.4`*:
       - **Giải pháp chặn đứng — Cơ chế "Tiếp Sức Tư Liệu Theo Cặp (`Visual Relay`)" ngay trong File Chỉ Đạo Bước 2**:
         - Mỗi Phân cảnh (`SC_01`) được chia thành các **Cặp Nhịp (`Relay Pairs`)**: Ví dụ ở `SC_01` (`0.0s -> 11.0s`), Nhịp A (`0.0s - 4.6s`) gồm `01.1 (Ngôi nhà $7 bên trái)` + `01.2 (Mỏ vàng tầng hầm bên phải)`; đúng `4.6s` cả hai cùng **Thoát sạch (`Exit`)** để nhường mặt bàn cho Nhịp B (`4.6s - 11.0s`) gồm `01.3 (Bản đồ Alaska lớn hơn Texas bên trái)` + `01.4 (Ngân phiếu 7.2 triệu đô bên phải)`.
         - Nhờ vậy, 1 Phân cảnh có tới **4 tư liệu thực tế (`01.1 -> 01.4`)**, nhưng tại mọi thời điểm `t` trên màn hình chỉ có **tối đa 2 tư liệu + 1 điểm nhấn (`<= 3 phần tử`)**!

---

### Vòng 6: Nâng Cấp Lên Phiên Bản 2.0 (`Multi-Mode Vox & Cartographic Documentary Studio`) & Cơ Chế Sao Lưu Dự Phòng Phiên Bản 1.0 (`v1.0 Backup Vault`)
- **Yêu cầu & Quyết định của Người dùng**:
  1. Nghiên cứu và giải phẫu 2 video mẫu đỉnh cao thế giới vào Kho Lưu Trữ Gu Edit (`KHO_LUU_TRU_GU_EDIT/`):
     - **Gu 01 (`Cartographic Storybook Map`)**: Phong cách bản đồ địa chính trị 2.5D ấm áp, Sticker minh họa viền kem dày `8px`, và Ghim Đỏ + Đường nối Vector (`Red Pin + Dashed Connector`).
     - **Gu 02 (`Vox Editorial Data & Cutout Motion`)**: Phong cách báo chí điều tra số liệu (Data Journalism) với nền lưới kỹ thuật (`Editorial Cream Grid`) đảo chiều sang nền Đen Than Chì (`Dark Climax Mode #111317`) ở các cảnh bóc trần sự thật/khủng hoảng, kết hợp HUD Mốc niên đại (`era_label`), Đồng hồ nhảy số góc phải (`hud_ticker`), Nguồn trích dẫn học thuật (`source_footnote`), Typography 3 tầng gạch ngang đỏ (`strikethrough`), Chia đôi màn hình rách giấy (`TORN_PAPER_SPLIT`), và Biểu đồ Lưới 100 ô / Cột răng cưa (`WAFFLE_100_ARRAY`, `ROUGH_EDGE_BARS`).
  2. **Nguyên tắc An toàn Bất di bất dịch trước khi nâng cấp Skill**:
     - Bắt buộc đóng băng và sao lưu toàn bộ **Skill Phiên bản 1.0 (`v1.0 — Archival Detective Desk`)** vào thư mục dự phòng độc lập `.agent/backups/skill_v1_0_backup/` kèm script khôi phục 1-click `python .agent/backups/skill_v1_0_backup/restore_v1_0.py`.
  3. **Kiến trúc Tương thích Ngược 100% (`100% Backward-Compatible v2.0 Engine`)**:
     - Mọi file `chi_dao_phan_canh.json` của Phiên bản 1.0 vẫn chạy nguyên vẹn trên Bàn dựng HTML (`index.html`), trình kiểm tra bố cục (`pha-4-kiem-tra-bo-cuc.py`) và bộ kết xuất `.mp4` (`pha-5-xuat-video-mp4.py`).
     - Các lớp chỉ đạo định hướng cấp Phân cảnh (`era_label`, `hud_ticker`, `source_footnote`) nằm gọn ở mép biên an toàn (`Edge Safe Margins`) nên **không chiếm dụng hạn ngạch 3 phần tử trung tâm (`max_concurrent <= 3`)**, giúp khung hình vừa đạt chiều sâu báo chí Vox vừa giữ sạch mặt bàn 100%!

---

### Vòng 7: Cuộc Cách Mạng Khử Tính Công Nghiệp & Nâng Cấp Lên Phiên Bản 3.0 (`v3.0 — Chuẩn Văn Thiết: Anti-Industrial Living Documentary Engine`)
- **Phản biện đắt giá từ Sếp của anh Văn Thiết & Tư duy Nhân – Quả**:
  - Nhận xét thực tế khi xem video: *"Nhìn kiểu công nghiệp và lặp lại nhỉ. Có mô-típ edit sinh động không?"*
  - **Giải phẫu Nhân – Quả (Đối chiếu với [`01_PHAN_TICH_CAU_TRUC_SKILL_DOI_THU_QUOC_TE.md`](../00_KHO_SKILLS_VA_CONG_CU_QUOC_TE/01_PHAN_TICH_CAU_TRUC_SKILL_DOI_THU_QUOC_TE.md) & [`02_TU_DUY_THIET_KE_SKILL_VAN_THIET.md`](../00_KHO_SKILLS_VA_CONG_CU_QUOC_TE/02_TU_DUY_THIET_KE_SKILL_VAN_THIET.md))**:
    1. **Nhân 1 — Đồng phục Bố cục Trái – Phải:** Ở bản v2.0, dù đã có 12 loại phần tử, AI vẫn vô thức đặt hầu hết các cảnh theo đúng 1 khuôn: `[Ảnh Polaroid bên Trái + Hộp chữ/Ảnh bên Phải]` trên nền giấy phẳng $\rightarrow$ Xem 3–4 cảnh liên tiếp là não người nhận ra ngay công thức lặp lại.
    2. **Nhân 2 — Phép tính Trung bình cộng che giấu "Khoảng Chết Đứng Hình" (`Dead Stretch`):** Ở bản v2.0, `pha-4-kiem-tra-bo-cuc.py` chỉ chia trung bình (`159.3s / 40 nhịp = 3.98s/nhịp`) và báo `0 lỗi`. Nhưng khi nâng cấp script lên v3.0 đo trực tiếp từng khoảng trống giữa 2 sự kiện (`Dead Stretch Gate`), máy phát hiện ngay **11 khoảng chết dài từ `5.0s` đến `9.8s`** mà khung hình đứng im chờ giọng đọc!
    3. **Nhân 3 — Thiếu Chuyển động Máy quay (`Camera with intent`) & Cắt cảnh trên đường cong (`Cut-the-Curve`):** Khung sân khấu đứng tĩnh 100% và các cảnh cắt rời rạc như lật trang PowerPoint.
- **Giải pháp Cấy Ghép Tinh Hoa Quốc Tế Vào Phiên Bản 3.0 (`v3.0`)**:
  1. **Sao lưu an toàn `v2.0`** tại `.agent/backups/skill_v2_0_backup/`.
  2. **Thiết lập Bảng Con Số Định Lượng (`Spec Numbers`) & 6 Điều CẤM Mặc Định (`BANNED DEFAULTS`)** trong `references/gu-tham-my-va-kho-hieu-ung.md`.
  3. **Bắt buộc luân phiên 5 Mô-típ Dàn Dựng Sinh Động (`scene_motif`) ở Pha 2 (`references/pha-2-dao-dien-phan-canh.md`)**:
     - `MOTIF_1_DETECTIVE_CANVAS_PAN` (Bàn thám tử & Máy quay lia cận cảnh)
     - `MOTIF_2_BROLL_KINETIC_OVERDRIVE` (Video B-Roll thật chiếm lĩnh + Chữ động khổng lồ)
     - `MOTIF_3_CARTOGRAPHIC_3D_FLYOVER` (Sa bàn bản đồ chiến thuật & Đường bay động)
     - `MOTIF_4_EVIDENCE_SPLIT_COLLISION` (Đối đầu trực diện / Xé giấy chia đôi màn hình)
     - `MOTIF_5_DATA_STORY_PROGRESSION` (Kể chuyện bằng số liệu biến đổi liên hoàn 3 nhịp)
     - **Luật sắt:** Hai cảnh liên tiếp cấm trùng `scene_motif` (`scene[i].scene_motif != scene[i-1].scene_motif`), đi kèm `camera_move` và `seam_transition` (`CUT_THE_CURVE_LEFT`, `ZOOM_THROUGH`, `INVERSE_ZOOM_ARRIVAL`, `TORN_PAPER_WIPE`).
  4. **Nâng cấp Chốt chặn Toán học `scripts/pha-4-kiem-tra-bo-cuc.py` lên v3.0**: Tự động bắt lỗi **Lặp mô-típ (P0)**, đo **Khoảng chờ dài nhất (`Max Hold Stretch` - P1)** và báo cáo **Tỷ lệ Chất liệu Động (`Mixed-Media Entropy`)** ngay bằng con số!

---

## PHẦN II. 15 QUY LUẬT VÀNG BẤT DI BẤT DỊCH CỦA ĐẠO DIỄN & EDITOR AI CHUYÊN NGHIỆP

1. **Quy luật 1 — Luật "Vào - Giữ 3 Giây - Thoát Sạch" (`Enter -> Hold -> Clean Exit Lifecycle`)**:
   - Tuyệt đối **CẤM** để các thẻ chữ/hiệu ứng phụ (`HEADLINE`, `NUMBER_COUNTER`, `DETECTIVE_TAPE_NOTE`, `STAMP`, `RED_INK_CIRCLE`, `FOCUS_FRAME`) nằm lì trên màn hình từ lúc xuất hiện cho tới tận cuối cảnh!
   - Mỗi thẻ phụ chỉ được xuất hiện đúng **`3.0 – 5.0 giây`** ứng với câu thoại đang đọc, sau đó **PHẢI TỰ THOÁT MƯỢT MÀ (`Fade Out` tại `t1`)** để dọn sạch mặt bàn trước khi thẻ thông tin tiếp theo xuất hiện ở vị trí đó!

2. **Quy luật 2 — Luật "Tối Đa 3 Phần Tử Cùng Lúc" (`Clean Stage Law: Max 3 Concurrent Items`)**:
   - Tại bất kỳ mili-giây `t` nào trên toàn bộ video, trên khung hình `1920x1080` **chỉ được phép có tối đa 2 đến 3 phần tử hiển thị cùng lúc**:
     - `1 Tư liệu Mỏ neo Chính` (`POLAROID`, `STICKER`, hoặc `VIDEO_CLIP` ở bên trái hoặc bên phải).
     - `1 Thẻ Luận điểm / Đồ họa Đang Nói Tới` (`HEADLINE`, `NUMBER_COUNTER`, hoặc `DETECTIVE_TAPE_NOTE` ở phía đối diện).
     - (Tùy chọn) `1 Điểm nhấn Trực tiếp` (`RED_INK_CIRCLE`, `FOCUS_FRAME` khoanh trên ảnh, hoặc `STAMP` đóng chốt hạ ở khoảng trống riêng biệt).
   - Script `scripts/pha-4-kiem-tra-bo-cuc.py` sẽ **báo lỗi đỏ ngay lập tức** nếu tại bất kỳ giây nào có `> 3` phần tử xuất hiện cùng lúc!

3. **Quy luật 3 — Cấm Tuyệt Đối Mọi Nhãn Mã Kỹ Thuật (`SC_01`, `STT_01`, Viền Chọn) Trên Khung Hình Video `1920x1080`**:
   - Khung hình `1920x1080` là màn ảnh rộng điện ảnh: **KHÔNG BAO GIỜ** được vẽ thanh `[SC_01]`, `[SC_02]`, `[STT_01]` lên video!
   - Chỉ báo cảnh hiện tại (`CẢNH HIỆN TẠI: ...`) chỉ được phép nằm trên thanh công cụ Studio (`Topbar`) và trên thước đo `5-Track Timeline`. Viền nét đứt vàng (`user-selected-item`) chỉ hiện khi người dùng chủ động bấm chuột vào phần tử để kéo, không bao giờ tự bật sẵn làm bẩn khung hình.

4. **Quy luật 4 — Kho Hiệu Ứng Đồ Họa PNG Trong Suốt & Âm Thanh Foley Thật (`Real FX Overlays & Natural Foley Vault`)**:
   - Sử dụng bộ tài nguyên đồ họa PNG Alpha trong suốt lưu tại `2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/fx_overlays/` (được khởi tạo bởi `scripts/tai-kho-hieu-ung-chuyen-nghiep.py`):
     - `red_ink_circle.png`: Vòng khoanh bút lông mực đỏ vẽ tay thật (đặt trực tiếp lên chi tiết cần khoanh trên ảnh tư liệu).
     - `archival_focus_frame.png`: Khung ngắm tiêu điểm 4 góc chữ L (soi đúng vào chi tiết trong tranh/bản đồ).
     - `masking_tape_strip.png`: Băng dính giấy xé răng cưa thật dán trên đầu thẻ hồ sơ.
     - `compass_rose_vintage.png`: Hoa gió la bàn hàng hải cổ in chìm tinh tế trên mặt bàn giấy.
   - Âm thanh Foley (`2_KHO_NGUYEN_LIEU/dung_chung_toan_kenh/sfx/*.wav`) phải trầm ấm, tự nhiên, không chói tai và chỉ điểm xuyết đúng nhịp chuyển động.

5. **Quy luật 5 — Chống Lặp Lại Công Thức Nhàm Chán (Đổi Bố Cục & Nhịp Điệu Theo Nội Dung)**:
   - Không bao giờ áp dụng một khuôn mẫu giống hệt nhau cho mọi cảnh.
   - Nếu một cảnh dài (25–30s như `sc_05`, `sc_06`, `sc_07`), phải **thay đổi cả Tư liệu Chính ở giữa cảnh** (ví dụ: Nửa đầu hiện Voi ma mút Băng hà `60s-71s` rồi thoát đi; nửa sau hiện Chân dung Tộc trưởng Bản địa `71s-92s` ở phía đối diện) để khung hình luôn tươi mới!

6. **Quy luật 6 — Bắt Buộc Kiểm Tra Va Chạm Cả Con Dấu (`STAMP`) Lẫn Thẻ Chữ**:
   - Không bao giờ miễn trừ `STAMP` khỏi thuật toán kiểm tra đè chữ! Con dấu `STAMP` bắt buộc phải nằm ở tọa độ trống riêng biệt (hoặc chỉ xuất hiện sau khi thẻ chữ trước đó đã thoát), tuyệt đối không được đè lên bất kỳ hộp chữ nào.

7. **Quy luật 7 — Bàn Dựng Đa Làn 5-Track NLE Timeline Chuyên Nghiệp (`index.html`)**:
   - Khung dưới hiển thị 5 làn Track độc lập (`V1: Ảnh & Video STT`, `FX1: Hiệu ứng Vào/Ra`, `SUB1: Phụ đề SRT EN/VI`, `A1: Sóng âm Voiceover`, `A2: Tiếng động Foley`) đồng bộ với kim thời gian đỏ (`Playhead`), nhìn vào Track `FX1` sẽ thấy rõ các khối hiệu ứng xếp nối đuôi nhau kiểu bậc thang (`Vào -> Thoát -> Vào -> Thoát`) thay vì kéo dài chồng chất lên nhau!

8. **Quy luật 8 — Quy Trình "AI Tự Đóng Vai Đạo Diễn Mở Video Kiểm Duyệt Bằng Mắt" (`pha-4-dao-dien-tu-xem-va-kiem-duyet.py`)**:
   - Ở Pha 4, sau khi chạy xong kiểm tra toán học `pha-4-kiem-tra-bo-cuc.py`, AI **BẮT BUỘC** phải chạy `python .agent/skills/dung-video-tai-lieu/scripts/pha-4-dao-dien-tu-xem-va-kiem-duyet.py <phan_XX>`.
   - Script này dùng trình duyệt Headless chụp lại 8 bức ảnh màn hình thật (`1920x1080`) của video tại các giây đầu, giữa và cuối cảnh.
   - AI **BẮT BUỘC** phải dùng `read_file` mở xem trực tiếp các bức ảnh chụp thật này bằng mắt AI, tự đánh giá với tư cách Đạo diễn xem có bị đè chữ, lệch vị trí khoanh vùng hay tạp nham không. Nếu phát hiện bất kỳ hạt sạn nào, AI phải tự sửa ngay trong `storyboard.json` và chụp lại cho đến khi hoàn hảo 10/10 rồi mới được phép trình người dùng ở `🛑 CỔNG DỪNG 4`!

9. **Quy luật 9 — 6 Cổng Dừng Cứng Bất Di Bất Dịch (`🛑 CỔNG DỪNG 0 -> 5`)**:
   - Tuyệt đối không chạy gộp nhiều Pha trong 1 lượt.

10. **Quy luật 10 — Chế Độ Mở Rộng Video Toàn Màn Hình & Thanh Điều Khiển Nổi Cho Editor (`Theater / Fullscreen Video Mode`)**:
    - Trên Bàn dựng `index.html`, khung xem trước `1920x1080` khi chia sẻ diện tích với bảng Inspector bên phải và 5-Track Timeline bên dưới sẽ bị thu nhỏ lại, khiến Editor khó soi kỹ chi tiết nhỏ hoặc thưởng thức trọn vẹn cảm xúc bộ phim.
    - Do đó, Bàn dựng HTML bắt buộc phải trang bị **Nút bấm Mở rộng Toàn màn hình (`⛶ Toàn Màn Hình (F)` trên Topbar & `⛶ Phóng To Video (F)` trên thanh NLE Toolbar)** cùng phím tắt **`F`** (hoặc **`ESC`** để thoát):
      - Khi bấm vào, ẩn tạm thời Topbar, Inspector và 5-Track Timeline, phóng khung hình Video `1920x1080` lấp đầy 100% màn hình (kích hoạt cả HTML5 Fullscreen API).
      - Hiển thị **Thanh điều khiển nổi thu gọn (`#fs-floating-hud`)** ở sát đáy màn hình gồm: `▶ PHÁT (SPACE)`, `⏮ 00:00`, Thanh kéo tua nhanh (`Scrubber`), Đồng hồ `Timecode`, và nút `🗗 Thu Nhỏ Về Bàn Dựng (ESC)` để Editor vừa xem toàn màn hình vừa tua/chỉnh vị trí phần tử trực tiếp.

11. **Quy luật 11 — Cơ Chế Đối Chất 2 Vai Trò Độc Lập Ở Mọi Pha (`🎬 Đạo Diễn / Biên Kịch Check ↔ 👷 Editor Điều Chỉnh`)**:
    - Chống bệnh quan liêu "check cho có": Trước khi mở bất kỳ Cổng Dừng nào (từ Pha 1 đến Pha 5), AI phải tách thành 2 vai trò đối lập (`👷 Editor thực thi` $\rightarrow$ `🎬 Đạo diễn/Biên kịch soi lỗi độc lập` $\rightarrow$ `🔧 Editor sửa lỗi & xác minh lại`). Đặc biệt ở Pha 4, Đạo diễn bắt buộc mở trình duyệt chụp 100% các Scene (`_A_` nửa đầu & `_B_` cuối cảnh), dùng `read_file` soi từng ảnh để bắt cả những hạt sạn thị giác mà toán học không thấy (như mảnh rác tách nền trên Sticker hay chữ đang mờ).

12. **Quy luật 12 — Bóc Tách Đa Tư Liệu Theo Từng Vế Câu & Mã Phân Cấp Cha-Con (`01.1_`, `01.2_`, `01.3_` — Visual-First, Anti-1-Scene-1-Image)**:
    - **Cấm tuyệt đối bệnh "1 Phân cảnh = 1 Ảnh tư liệu duy nhất"**: Ở Pha 2, Đạo diễn & Biên kịch phải mổ xẻ từng câu thoại trong 1 Phân cảnh (`SC_XX`) thành các **Thực thể Thị giác (`Visual Nouns`)** theo từng vế câu (ví dụ: *Ngôi nhà bán $7* $\rightarrow$ *Mỏ vàng dưới tầng hầm* $\rightarrow$ *Bản đồ Alaska* $\rightarrow$ *Tờ séc 7.2 triệu đô*).
    - Mỗi Phân cảnh (`SC_01`, `SC_02`...) phải có **từ 2 đến 4 nguyên liệu hình ảnh/video/sticker thực tế** được đánh mã phân cấp **`01.1_00m00s_...`, `01.2_00m02s_...`, `01.3_00m04s_...`** thay vì lười biếng lấy 1 ảnh rồi đắp toàn chữ lên.
    - Các tư liệu con (`01.1` $\rightarrow$ `01.2` $\rightarrow$ `01.3`) vận hành theo nguyên lý **Tiếp Sức Thị Giác (`Visual Relay`)**: tư liệu của vế câu trước hiển thị `2.2 – 4.5s` xong sẽ thu hồi (`Exit`) để tư liệu của vế câu sau xuất hiện, giữ khung hình luôn giàu hình ảnh mà vẫn sạch sẽ (`max_concurrent <= 3`).

13. **Quy luật 13 — Kiến Trúc "Một File Chỉ Đạo Phân Cảnh Hợp Nhất" Ở Pha 2 Xuyên Suốt Sang Pha 3 & Pha 4 (`Master Director Blueprint: Single Source of Truth`)**:
    - Ngay tại **Bước 2 (Pha 2)**, Đạo diễn & Biên kịch phải xuất ra **File Chỉ Đạo Phân Cảnh Hợp Nhất (`chi_dao_phan_canh.json` & `chi_dao_phan_canh.md`)** chứa đầy đủ:
      1. Danh sách mã tư liệu con (`01.1`, `01.2`, `01.3`...), từ khóa tìm kiếm chính & dự phòng có khóa niên đại lịch sử (phục vụ trực tiếp cho **Bước 3 — Săn nguyên liệu**).
      2. Mốc thời gian **Vào - Giữ - Thoát (`t0 -> t1`)**, vùng bố cục (`LEFT_MAIN`, `RIGHT_MAIN`, `CENTER_FOCUS`), tọa độ `x, y, w, h`, hiệu ứng đồ họa đi kèm (`companion_fx`) và tiếng động `sfx` có lý do ngữ nghĩa (phục vụ trực tiếp cho **Bước 4 — Bàn dựng HTML**).
    - **Tuyệt đối cấm** tình trạng Pha 2 viết một kiểu, sang Pha 3 tìm một kiểu, rồi sang Pha 4 Editor lại tự bịa ra một file `storyboard.json` khác! Pha 3 và Pha 4 bắt buộc đọc và cập nhật trực tiếp trên chính File Chỉ Đạo Phân Cảnh đã được duyệt ở Pha 2.

14. **Quy luật 14 — Tự Động Kế Thừa 100% Tư Duy Cho Mọi Dự Án & Nhân Sự Mới**:
    - Toàn bộ bộ công cụ (`pha-0` đến `pha-5`, `tai-kho-hieu-ung-chuyen-nghiep.py`, `pha-4-dao-dien-tu-xem-va-kiem-duyet.py`) và tài liệu tư duy này nằm gọn trong Skill `.agent/skills/dung-video-tai-lieu/`.

15. **Quy luật 15 — Bảo Toàn Bản Sao Lưu Dự Phòng `v1.0` & Khai Thác Đúng Lúc 6 Vũ Khí Thị Giác `v2.0` (`Vox & Cartographic Hybrid`)**:
    - Bản gốc **Phiên bản 1.0 (`v1.0`)** luôn được bảo toàn nguyên trạng tại `.agent/backups/skill_v1_0_backup/` (khôi phục bất cứ lúc nào bằng `python .agent/backups/skill_v1_0_backup/restore_v1_0.py`).
    - Khi đạo diễn ở **Phiên bản 2.0 (`v2.0`)**, luôn gắn `era_label` và `source_footnote` cho các phân cảnh có mốc lịch sử/số liệu kiểm chứng; chỉ bật `bg_mode: "DARK_CLIMAX"` ở đúng 1–2 phân cảnh cao trào bóc trần sự thật để tạo cú sốc thị giác đắt giá nhất!
