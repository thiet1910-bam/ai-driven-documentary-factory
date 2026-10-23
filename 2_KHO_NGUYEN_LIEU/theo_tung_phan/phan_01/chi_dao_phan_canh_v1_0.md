# 🎬 FILE CHỈ ĐẠO PHÂN CẢNH HỢP NHẤT (MASTER DIRECTOR BLUEPRINT) — `phan_01` (`00:00 -> 02:25.2`)

> **Vai trò của File này**: Đây là **Bản Thiết Kế Gốc Duy Nhất (`Single Source of Truth`)** đồng bộ 100% với [`chi_dao_phan_canh.json`](./chi_dao_phan_canh.json).
> - **Ở Bước 2 (Pha 2)**: Dùng để Đạo diễn, Biên kịch & Người dùng nghiệm thu kịch bản phân cảnh đa tư liệu (`01.1`, `01.2`, `01.3`...) và vòng đời **Vào - Giữ - Thoát (`t0 -> t1`)**.
> - **Sang Bước 3 (Pha 3)**: Script `pha-3-san-nguyen-lieu-theo-stt.py` đọc trực tiếp từ `chi_dao_phan_canh.json` để đi săn đúng 23 file tư liệu (`01.1 -> 06.4`) và ghi ngược đường dẫn thực tế vào file.
> - **Sang Bước 4 (Pha 4)**: Bàn dựng 5-Track (`index.html`) nạp thẳng cấu trúc này lên màn hình mà không cần viết lại!

---

## I. THống KÊ TỔNG QUAN BẢN CHỈ ĐẠO MỚI SO VỚI BẢN CŨ (`[📊 ĐỐI CHIẾU THỰC TẾ]`)

| Chỉ số Đạo diễn | Bản Cũ (Trước Vòng 5) | Bản Mới (`chi_dao_phan_canh.json`) | Đánh Giá Nâng Cấp |
|---|---|---|---|
| **Tổng số Phân cảnh lớn (`Scenes`)** | `7 cảnh` | **`6 Phân cảnh lớn` (`SC_01 -> SC_06`)** | Gom đúng 6 đại ý kịch bản |
| **Tổng số Tư liệu Hình ảnh / Video / Sticker thực tế** | Chỉ `12 file` (`~1.7 ảnh/cảnh`) | **`23 file tư liệu` (`01.1 -> 06.4`, đạt `3.8 tư liệu/cảnh`)** | **Tăng gần gấp đôi (`+92%`) mật độ hình ảnh thực tế!** |
| **Số tư liệu trong Cảnh mở đầu (`SC_01`)** | Chỉ `1 ảnh` (Tờ séc Alaska hiện sớm gây lộ kịch bản) | **`4 tư liệu` (`01.1 Ngôi nhà $7` $\rightarrow$ `01.2 Mỏ vàng tầng hầm` $\rightarrow$ `01.3 Bản đồ Alaska` $\rightarrow$ `01.4 Mỏ vàng & Dầu mỏ`)** | Bám sát từng vế câu ẩn dụ rồi mới lật mở Alaska |
| **Trần mật độ hiển thị cùng lúc (`max_concurrent`)** | `<= 3` | **`<= 3 phần tử` tại mọi thời điểm `0.25s`** | Vận hành theo cơ chế **Tiếp Sức Tư Liệu (`Visual Relay`)** — 0% đè chồng |

---

## II. BẢNG CHỈ ĐẠO PHÂN CẢNH CHI TIẾT THEO MÃ PHÂN CẤP (`01.1 -> 06.4`)

### 🎬 PHÂN CẢNH 1 (`SC_01`: `0.0s -> 18.0s`): ẨN DỤ NGÔI NHÀ $7, MỎ VÀNG TẦNG HẦM & CÚ HỚ CỦA NƯỚC NGA
> **Lời thoại**: *"Imagine selling your house for $7 and then finding out there was a gold mine in the basement. That is exactly what Russia did. Except the house was Alaska, and the basement had gold, oil, and a few hundred billion dollars."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`01.1_00m00s_polaroid_wooden_house_for_sale_7_dollars`** | `0.4s -> 8.2s` *(Thoát ở 8.2s)* | *"Imagine selling your **house for $7**..."* | **[TRÁI]** Ảnh ngôi nhà gỗ cổ thế kỷ 19. Đến `2.8s` đóng dấu đỏ **`SOLD FOR $7`** (`FX_01A`, thoát ở `4.4s`) kèm `rubber_stamp.wav`. | `POLAROID` (`.jpg`) | `19th century wooden cabin house historical photograph` (`wiki: Log cabin`) | Wikipedia / Wikimedia Commons |
| **`01.2_00m04s_polaroid_gold_mine_in_basement`** | `4.5s -> 8.2s` *(Thoát ở 8.2s)* | *"...and then finding out there was a **gold mine in the basement**."* | **[PHẢI]** Ảnh hầm mỏ vàng dưới lòng đất đặt đối xứng bên phải ngôi nhà (`sfx: low_boom.wav`). Đúng `8.2s`, **cả `01.1` và `01.2` cùng thoát sạch**! | `POLAROID` (`.jpg`) | `19th century underground gold mine miners historical` (`wiki: Gold mining`) | Wikipedia / Wikimedia Commons |
| **`01.3_00m08s_polaroid_russian_america_alaska_map`** | `8.4s -> 13.4s` *(Thoát ở 13.4s)* | *"That is exactly what **Russia did**. Except **the house was Alaska**..."* | **[TRÁI]** Bản đồ lãnh thổ Alaska của Nga năm 1867 (`map_whoosh.wav`) + **[PHẢI]** Thẻ `HEADLINE`: **`THE HOUSE WAS ALASKA`** (`FX_01B`, `8.8s -> 13.4s`). | `POLAROID` (`.jpg`) | `Russian America map 1867 Alaska territory` (`wiki: Russian America`) | Wikipedia / Wikimedia Commons |
| **`01.4_00m13s_polaroid_alaska_gold_and_oil_fields`** | `13.5s -> 17.9s` *(Thoát ở 17.9s)* | *"...and the basement had **gold, oil, and a few hundred billion dollars**."* | **[TRÁI]** Ảnh mỏ vàng & dầu mỏ Alaska (thay thế `01.3`) + **[PHẢI]** Bộ đếm số **`$500+ BILLION`** (`FX_01C`, `14.2s -> 17.9s`, `typewriter.wav`). | `POLAROID` (`.jpg`) | `Alaska gold mining oil derrick historical photograph` (`wiki: Nome Gold Rush`) | Wikipedia / Wikimedia Commons |

---

### 🎬 PHÂN CẢNH 2 (`SC_02`: `18.0s -> 36.0s`): MỨC GIÁ 2 XU/MẪU ANH, "TỦ ĐÁ CỦA SEWARD" & VƯỜN GẤU BẮC CỰC
> **Lời thoại**: *"The price: 2 cents an acre. And the funny part? Americans thought they were the ones getting robbed. They called it an icebox, a frozen wasteland, a polar bear garden. They had no idea they had just made one of the greatest deals in history."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`02.1_00m18s_polaroid_1868_treasury_check_7m`** | `18.1s -> 26.2s` *(Thoát ở 26.2s)* | *"The price: **2 cents an acre**..."* | **[TRÁI]** Tờ ngân phiếu 7.2 triệu USD mua Alaska + Vòng bút lông đỏ `RED_INK_CIRCLE` khoanh mức giá **`ONLY 2¢ PER ACRE!`** (`19.0s -> 23.2s`). | `POLAROID` (`.jpg`) | `Alaska Purchase check 7.2 million dollars 1868` (`wiki: Alaska Purchase`) | Wikipedia Lead Image |
| **`02.2_00m22s_sticker_william_seward`** | `22.4s -> 26.2s` *(Thoát ở 26.2s)* | *"...Americans thought **they were the ones getting robbed**."* | **[PHẢI]** Sticker tách nền Ngoại trưởng Mỹ **William H. Seward** — người bị báo chí Mỹ chỉ trích là bị Nga lừa. Đúng `26.2s` cả `02.1` & `02.2` thoát sạch! | `STICKER` tách nền (`.png`) | `William H. Seward portrait photograph` (`wiki: William H. Seward`) | Wikipedia Lead Image |
| **`02.3_00m26s_polaroid_seward_icebox_cartoon`** | `26.4s -> 31.4s` *(Thoát ở 31.4s)* | *"They called it **an icebox, a frozen wasteland**..."* | **[TRÁI]** Tranh biếm họa báo chí năm 1867 chế giễu tảng băng "Russian America". | `POLAROID` (`.jpg`) | `Seward's Folly political cartoon 1867 icebox` | Wikimedia Commons |
| **`02.4_00m29s_polaroid_polar_bear_garden_arctic`** | `29.0s -> 35.9s` *(Thoát ở 35.9s)* | *"...a **polar bear garden**. They had no idea they had just made one of the **greatest deals in history**."* | **[PHẢI]** Ảnh Gấu Bắc Cực trên băng giá (`29.0s`). Ở `31.6s`, bên trái (`02.3` đã thoát) hiện Phiếu hồ sơ + Con dấu đỏ **`GREATEST DEAL IN HISTORY`** (`33.2s -> 35.9s`). | `POLAROID` (`.jpg`) | `Polar bear Arctic ice historical illustration photograph` (`wiki: Polar bear`) | Wikipedia / Wikimedia Commons |

---

### 🎬 PHÂN CẢNH 3 (`SC_03`: `36.0s -> 60.0s`): 15.000 NĂM TRƯỚC — CÂY CẦU ĐẤT LIỀN BERINGIA ĐÃ BIẾN MẤT
> **Lời thoại**: *"This is the story of Alaska. And it starts long before Russia, long before America. It starts with a bridge that no longer exists. More than 15,000 years ago, the oceans were lower. And between Asia and North America, there was land — a bridge of grass and ice, hundreds of miles wide."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`03.1_00m36s_polaroid_ancient_alaska_glacier_wilderness`** | `36.2s -> 46.8s` *(Thoát ở 46.8s)* | *"This is the story of **Alaska**... long before Russia, long before America."* | **[TRÁI]** Núi tuyết & sông băng hoang sơ thời tiền sử của Alaska + **[PHẢI]** `HEADLINE`: **`A VANISHED LAND BRIDGE`** (`39.5s -> 46.8s`). | `POLAROID` (`.jpg`) | `Alaska mountain wilderness glacier historical photograph` (`wiki: Alaska Range`) | Wikipedia / Wikimedia Commons |
| **`03.2_00m47s_polaroid_beringia_land_bridge_map`** | `47.0s -> 59.9s` *(Thoát ở 59.9s)* | *"More than **15,000 years ago**, the oceans were lower. And between **Asia and North America, there was land**..."* | **[TRÁI]** Bản đồ cầu đất liền Beringia nối Á - Mỹ + Bộ đếm **`15,000+ YEARS AGO`** (`47.6s -> 53.5s` rồi thoát) + Khoanh mực đỏ `RED_INK_CIRCLE` vào eo biển Beringia (`52.0s`). | `POLAROID` (`.jpg`) | `Bering Land Bridge Beringia map Ice Age` (`wiki: Beringia`) | Wikipedia / Wikimedia Commons |
| **`03.3_00m54s_polaroid_steppe_grass_and_ice_landscape`** | `54.0s -> 59.9s` *(Thoát ở 59.9s)* | *"...a **bridge of grass and ice, hundreds of miles wide**."* | **[PHẢI]** Cảnh thảo nguyên cỏ và băng giá Kỷ Băng Hà (`Mammoth Steppe`) hiện ra ở nửa bàn phải sau khi bộ đếm `15,000` đã thoát. | `POLAROID` (`.jpg`) | `Pleistocene mammoth steppe tundra grass ice landscape` (`wiki: Mammoth steppe`) | Wikipedia / Wikimedia Commons |

---

### 🎬 PHÂN CẢNH 4 (`SC_04`: `60.0s -> 92.0s`): NHỮNG CON NGƯỜI ĐẦU TIÊN Ở CHÂU MỸ & 5 DÂN TỘC BẢN ĐỊA "ALYESKA"
> **Lời thoại**: *"People walked across it, following the animals they hunted. Surprised, they were the first humans to ever set foot in the Americas. Some kept moving south. Others stayed. They became the Inupiat, the Yupik, the Unangan, the Tlingit, the Athabaskan. They even gave the land its name. Alaska comes from a native word that means the great land."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`04.1_01m00s_sticker_woolly_mammoth_hunters`** | `60.2s -> 71.2s` *(Thoát ở 71.2s)* | *"People walked across it, **following the animals they hunted**..."* | **[TRÁI]** Sticker tách nền Đàn voi ma mút Kỷ Băng Hà (`Woolly Mammoths`). | `STICKER` tách nền (`.png`) | `Woolly mammoth Charles R. Knight prehistoric hunters` (`wiki: Woolly mammoth`) | Wikipedia / Wikimedia Commons |
| **`04.2_01m04s_polaroid_paleo_indians_first_humans_americas`** | `64.2s -> 71.2s` *(Thoát ở 71.2s)* | *"...they were the **first humans to ever set foot in the Americas**."* | **[PHẢI]** Tranh/ảnh tư liệu những cư dân tiền sử đầu tiên đặt chân sang châu Mỹ + Con dấu đỏ **`FIRST AMERICANS`** (`66.5s -> 71.2s`). Đúng `71.2s` cả 3 thoát sạch! | `POLAROID` (`.jpg`) | `Paleo-Indians hunting Ice Age Beringia illustration` (`wiki: Paleo-Indians`) | Wikipedia / Wikimedia Commons |
| **`04.3_01m12s_polaroid_inupiat_yupik_arctic_family`** | `71.4s -> 81.3s` *(Thoát ở 81.3s)* | *"Others stayed. They became the **Inupiat, the Yupik, the Unangan**..."* | **[TRÁI]** Ảnh tư liệu gia đình người bản địa phương Bắc Inupiat / Yupik (ống kính Edward S. Curtis). | `POLAROID` (`.jpg`) | `Inupiat Eskimo family Alaska Edward S. Curtis photograph` (`wiki: Iñupiat`) | Wikipedia / Wikimedia Commons |
| **`04.4_01m16s_polaroid_tlingit_athabaskan_chief`** | `75.5s -> 91.9s` *(Thoát ở 91.9s)* | *"...the **Tlingit, the Athabaskan**... Alaska comes from a native word that means **'The Great Land'**."* | **[PHẢI]** Chân dung Tù trưởng Tlingit / Athabaskan. Ở `81.6s`, bên trái (`04.3` đã thoát) hiện bảng `HEADLINE`: **`'THE GREAT LAND'`** (`81.6s -> 91.9s`). | `POLAROID` (`.jpg`) | `Tlingit chief Alaska historical portrait 1913` (`wiki: Tlingit`) | Wikipedia / Wikimedia Commons |

---

### 🎬 PHÂN CẢNH 5 (`SC_05`: `92.0s -> 120.5s`): NĂM 1741 — THUYỀN TRƯỞNG VITUS BERING, VỤ ĐẮM TÀU & CON THUYỀN SỐNG SÓT
> **Lời thoại**: *"Then in 1741, a ship appeared. Its captain was Vitus Bering, a Danish explorer working for the Russian Empire. His mission: find out what lies east of Siberia. He found Alaska. Bering never made it home. He died on the way back, shipwrecked on a frozen island. But his crew survived the winter, built a new boat from the wreck, and sailed home..."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`05.1_01m32s_polaroid_st_peter_ship_1741`** | `92.2s -> 107.2s` *(Thoát ở 107.2s)* | *"Then in **1741, a ship appeared**... find out what lies east of Siberia."* | **[TRÁI]** Con tàu St. Peter & bản đồ hải trình 1741 + **[PHẢI]** Bộ đếm **`YEAR 1741 A.D.`** (`92.8s -> 96.5s` rồi thoát). | `POLAROID` (`.jpg`) | `Vitus Bering ship St. Peter 1741 expedition map` (`wiki: Second Kamchatka Expedition`) | Wikipedia / Wikimedia Commons |
| **`05.2_01m36s_sticker_vitus_bering`** | `96.7s -> 107.2s` *(Thoát ở 107.2s)* | *"Its captain was **Vitus Bering**, a Danish explorer working for the Russian Empire."* | **[PHẢI]** Sticker tách nền chân dung Thuyền trưởng Vitus Bering (xuất hiện ngay khi bộ đếm 1741 thoát). Đúng `107.2s` cả `05.1` & `05.2` thoát sạch! | `STICKER` tách nền (`.png`) | `Vitus Bering portrait painting` (`wiki: Vitus Bering`) | Wikipedia Lead Image |
| **`05.3_01m47s_polaroid_bering_island_shipwreck`** | `107.4s -> 120.4s` *(Thoát ở 120.4s)* | *"Bering never made it home. He died on the way back, **shipwrecked on a frozen island**."* | **[TRÁI]** Ảnh tư liệu đảo Bering băng giá nơi tàu đắm + **[PHẢI]** `HEADLINE`: **`SHIPWRECKED IN WINTER`** (`108.0s -> 113.0s` rồi thoát). | `POLAROID` (`.jpg`) | `Bering Island shipwreck winter 1741 Commander Islands` (`wiki: Bering Island`) | Wikipedia / Wikimedia Commons |
| **`05.4_01m53s_polaroid_survivors_rebuilt_boat_1742`** | `113.2s -> 120.4s` *(Thoát ở 120.4s)* | *"But his crew **survived the winter, built a new boat from the wreck, and sailed home**..."* | **[PHẢI]** Tranh/ảnh tư liệu thủy thủ đoàn Nga dựng trại mùa đông và đóng lại thuyền gỗ từ xác tàu đắm năm 1742 (thay thế `HEADLINE` vừa thoát). | `POLAROID` (`.jpg`) | `18th century Russian expedition wooden boat camp Siberia` (`wiki: Sven Waxell`) | Wikipedia / Wikimedia Commons |

---

### 🎬 PHÂN CẢNH 6 (`SC_06`: `120.5s -> 145.2s`): CƠN SỐT "VÀNG MỀM" (LÔNG RÁI CÁ BIỂN) & THẢM KỊCH CỦA NGƯỜI UNANGAN
> **Lời thoại**: *"...Sea otter fur. The softest, thickest fur in the world. In China, a single pelt was worth a fortune. Russians called it 'Soft Gold'. And the rush was on. Serious. Russian hunters poured across the sea island by island. They forced the native Unangan people to hunt for them. Thousands died from violence and disease."*

| Mã Phân Cấp (`Sub-STT`) | Mốc Giây (`Vào -> Thoát`) | Vế Câu Thoại Kích Hoạt | Chỉ Đạo Hình Ảnh, Bố Cục (`Trái/Phải`) & Hiệu Ứng Đi Kèm | Định Dạng | Từ Khóa Săn Đa Nguồn (Khóa Niên Đại) | Nguồn Dự Kiến |
|---|---|---|---|---|---|---|
| **`06.1_02m01s_sticker_sea_otter_soft_gold`** | `120.6s -> 133.6s` *(Thoát ở 133.6s)* | *"**Sea otter fur**. The softest, thickest fur in the world."* | **[TRÁI]** Sticker tách nền Rái cá biển Bắc Thái Bình Dương. | `STICKER` tách nền (`.png`) | `Sea otter Enhydra lutris fur photograph` (`wiki: Sea otter`) | Wikipedia Lead Image |
| **`06.2_02m06s_polaroid_qing_dynasty_china_fur_trade`** | `125.8s -> 133.6s` *(Thoát ở 133.6s)* | *"In **China, a single pelt was worth a fortune**. Russians called it **'Soft Gold'**."* | **[PHẢI]** Tranh/ảnh thương mại lông thú với giới quý tộc nhà Thanh Trung Hoa + Con dấu đỏ **`CALLED 'SOFT GOLD'`** (`130.0s -> 133.6s`). Đúng `133.6s` thoát sạch! | `POLAROID` (`.jpg`) | `Qing dynasty mandarin fur robe China trade 18th century` (`wiki: Maritime fur trade`) | Wikipedia / Wikimedia Commons |
| **`06.3_02m14s_video_aleutian_sea_hunters`** | `133.8s -> 139.2s` *(Thoát ở 139.2s)* | *"Russian hunters **poured across the sea island by island**."* | **[TRÁI]** Đoạn Video 4s chuyển động đoàn thuyền thợ săn Nga vượt biển + **[PHẢI]** `HEADLINE`: **`ISLAND BY ISLAND`** (`134.2s -> 139.2s`). | `VIDEO_CLIP` (`.mp4`) | `Aleutian Islands sea otter hunting archival footage` | YouTube / Wikimedia Motion |
| **`06.4_02m19s_polaroid_unangan_aleut_forced_hunters`** | `139.3s -> 145.1s` | *"They **forced the native Unangan people to hunt** for them. **Thousands died** from violence and disease."* | **[TRÁI]** Ảnh người bản địa Unangan (Aleut) chèo thuyền săn bắt dưới sự cưỡng bức + **[PHẢI]** Phiếu hồ sơ **`THE TRAGEDY OF THE UNANGAN`** (`139.6s -> 145.1s`). | `POLAROID` (`.jpg`) | `Aleut Unangan hunters kayaks historical illustration` (`wiki: Aleuts`) | Wikipedia / Wikimedia Commons |

---

## III. 🎬 BIÊN BẢN ĐỐI CHẤT NỘI BỘ PHA 2: ĐẠO DIỄN & BIÊN KỊCH CHECK $\leftrightarrow$ EDITOR ĐIỀU CHỈNH

1. **👷 Editor AI (Bản thiết kế đầu tiên)**:
   - Bóc tách `phan_01` từ 12 mã đơn lẻ (`01_ -> 12_`) lên **23 mã phân cấp (`01.1 -> 06.4`)** trong `chi_dao_phan_canh.json`.
2. **🎬 Đạo diễn & Biên kịch AI (Kiểm tra độc lập & Phản biện khắt khe)**:
   - **Kiểm tra 1 — Mật độ hình ảnh tại `SC_01`**: Xác nhận đã tách câu mở đầu thành 4 tư liệu rõ rệt (`01.1 Ngôi nhà gỗ $7` $\rightarrow$ `01.2 Hầm mỏ vàng` $\rightarrow$ `01.3 Bản đồ Nga bán Alaska` $\rightarrow$ `01.4 Mỏ vàng & Giàn khoan dầu Alaska`). Không còn lỗi quăng tờ séc Alaska ra ở giây `0.4s` làm lộ kịch bản!
   - **Kiểm tra 2 — Các hình ảnh cụ thể trong lời thoại ở `SC_02 -> SC_06`**:
     - Giây `29.0s` nhắc *"a polar bear garden"* $\rightarrow$ Đã có mã `02.4_00m29s_polaroid_polar_bear_garden_arctic`.
     - Giây `54.0s` nhắc *"a bridge of grass and ice"* $\rightarrow$ Đã có mã `03.3_00m54s_polaroid_steppe_grass_and_ice_landscape`.
     - Giây `71.4s - 78.4s` điểm danh 5 dân tộc bản địa (*Inupiat, Yupik, Unangan, Tlingit, Athabaskan*) $\rightarrow$ Đã tách thành 2 bức ảnh đối xứng (`04.3` Inupiat/Yupik bên trái & `04.4` Tlingit/Athabaskan bên phải).
     - Giây `113.2s` nhắc *"built a new boat from the wreck"* $\rightarrow$ Đã có mã `05.4_01m53s_polaroid_survivors_rebuilt_boat_1742`.
     - Giây `126.5s` nhắc *"In China, a single pelt was worth a fortune"* $\rightarrow$ Đã có mã `06.2_02m06s_polaroid_qing_dynasty_china_fur_trade`.
   - **Kiểm tra 3 — Kiểm tra toán học `max_concurrent` ngay trên File Chỉ Đạo**: Chạy kiểm tra từng mốc `0.25s` trên toàn bộ `145.2s`, xác nhận `Max Concurrent = 3` (không giây nào vượt quá 3 phần tử cùng lúc).
3. **🔧 Editor AI (Xác nhận hoàn tất Pha 2)**:
   - Đã lưu đồng bộ cả 2 file [chi_dao_phan_canh.json](file:///e:/02_CHANNEL/thu-nghiem/edit-video/2_KHO_NGUYEN_LIEU/theo_tung_phan/phan_01/chi_dao_phan_canh.json) và [chi_dao_phan_canh.md](file:///e:/02_CHANNEL/thu-nghiem/edit-video/2_KHO_NGUYEN_LIEU/theo_tung_phan/phan_01/chi_dao_phan_canh.md).
   - **Tuyệt đối chưa tải bất kỳ file ảnh/video mới nào** trước khi có lệnh duyệt ở Cổng Dừng 2.
