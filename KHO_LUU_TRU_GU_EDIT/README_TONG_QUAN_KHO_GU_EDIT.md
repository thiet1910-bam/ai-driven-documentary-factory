# 🏛️ KHO LƯU TRỮ GU EDIT & THƯ VIỆN PHONG CÁCH THỊ GIÁC — ÂM THANH (STYLE VAULT)

> [!IMPORTANT]
> **Trạng thái tích hợp:** Thư mục này là **Kho Lưu Trữ Độc Lập (Staging & Reference Vault)** dùng để nghiên cứu, chuẩn hóa và tích lũy các Gu Edit, Hiệu ứng Chuyển cảnh, Typography, Bố cục Hình ảnh và Thiết kế Âm thanh (SFX).
> **Tuyệt đối chưa cập nhật vào `.agent/skills/` hay `AGENTS.md`** cho đến khi người dùng ra lệnh nâng cấp chính thức.

---

## I. CẤU TRÚC THƯ MỤC CHUẨN HÓA (`KHO_LUU_TRU_GU_EDIT/`)

```text
KHO_LUU_TRU_GU_EDIT/
├── README_TONG_QUAN_KHO_GU_EDIT.md               # Tài liệu tổng quan & Hướng dẫn nạp vào Agent/Skill sau này
├── 01_GU_EDIT_MAU/                               # Phân tích chuyên sâu từng Gu Edit từ các kênh/video mẫu
│   ├── GU_01_CARTOGRAPHIC_STORYBOOK_MAP.md       # Gu 1: Bản đồ Lịch sử Kể chuyện (Fortune of Nations - gP4ihbNXFrY)
│   ├── GU_02_VOX_EDITORIAL_DATA_MOTION.md        # Gu 2: Vox Editorial Data & Cutout Motion (RandomAI / Opus 5.5 - uIHJvUVaB34)
│   └── GU_03_HYBRID_SU_DE_HIEU_SIGNATURE.md      # Gu 3 (Tổng hợp): Sự kết hợp Gu 1 + Gu 2 cho kênh Sử Để Hiểu
├── 02_HIEU_UNG_CHUYEN_CANH/                      # Quy chuẩn Chuyển cảnh (Transitions), Nhịp điệu & Easing
│   └── QUY_CHUAN_CHUYEN_CANH_VA_CAMERA.md        # Easing curves, Camera Pan/Zoom, Torn-Paper Split, Hard Dark-Mode Invert
├── 03_TYPOGRAPHY_VA_TEXT_FX/                     # Hệ thống Phông chữ, Kinetic Typography & Nhấn chữ
│   └── QUY_CHUAN_TYPOGRAPHY_VA_TEXT_FX.md        # Cặp font Serif Italic + Condensed Sans, Marker Swipe, Strikethrough, Ticker
├── 04_HIEU_UNG_HINH_ANH_VA_BO_CUC/               # Quy chuẩn Xử lý Hình ảnh, Bản đồ, Cutout, Biểu đồ & Texture
│   ├── QUY_CHUAN_HINH_ANH_CUTOUT_VA_BIU_DO.md    # Halftone/Color Cutouts, Torn-Paper Card, Unit Array Chart, Map Arrows
│   ├── overlays_mau/                             # Nơi lưu các file .PNG/.SVG overlay mẫu (viền giấy xé, mũi tên, con dấu)
│   ├── stickers_mau/                             # Nơi lưu các mẫu nhân vật/vật thể tách nền viền trắng
│   └── textures_mau/                             # Nơi lưu nền giấy nhám, lưới đồ thị (grid), giấy cổ (parchment)
├── 05_HIEU_UNG_AM_THANH_SFX/                     # Thiết kế Âm thanh (Soundscape 50% chất lượng video)
│   ├── QUY_CHUAN_THIET_KE_AM_THANH_SFX.md        # Quy tắc phối Foley SFX theo từng chuyển động & cách sinh SFX bằng Python
│   ├── sfx_chuyen_canh/                          # Whoosh trầm, tiếng lật bản đồ, tiếng xé giấy
│   ├── sfx_text_va_so_lieu/                      # Tiếng bút dạ quẹt, máy đánh chữ, bộ đếm số (ticker), gạch chữ
│   ├── sfx_hinh_anh_va_stamp/                    # Tiếng đặt ảnh (paper slap), pop-up nhân vật, đóng dấu cao su (stamp slam)
│   └── sfx_ambient_nen/                          # Âm nền không gian (gió tuyết, sóng biển, phòng hồ sơ, drone trầm)
└── 06_VIDEO_MAU_THAM_CHIEU/                      # Lưu trữ Contact Sheets (Storyboard Frames) & Metadata video gốc
    ├── DANH_SACH_VIDEO_NGUON_VA_PHAN_TICH.md     # Bảng đối chiếu chi tiết các video mẫu đã bóc tách
    ├── frames_gu_01/                             # Contact sheets trích xuất từ video Gu 1 (gP4ihbNXFrY)
    └── frames_gu_02/                             # Contact sheets trích xuất từ video Gu 2 (uIHJvUVaB34)
```

---

## II. TÓM TẮT 2 GU EDIT GỐC ĐÃ BÓC TÁCH TRONG KHO

| Tiêu chí | 🗺️ **GU EDIT 1: Cartographic Storybook & Illustrated Map**<br>*(Nguồn: `gP4ihbNXFrY` — Switzerland Should Be Poor)* | 📊 **GU EDIT 2: Vox Editorial Data & Cutout Motion**<br>*(Nguồn: `uIHJvUVaB34` — Claude Opus 5.5 Vox-Style)* |
| :--- | :--- | :--- |
| **Triết lý Cốt lõi** | Biến toàn bộ câu chuyện lịch sử/địa chính trị thành một **bàn sa bàn bản đồ sống động**, nơi nhân vật minh họa, mũi tên quân sự và con dấu tương tác trực tiếp trên lãnh thổ. | Biến các con số, luận điểm kinh tế - lịch sử khô khan thành **trải nghiệm thị giác kiểu báo chí điều tra (Vox Editorial)** với ảnh cắt rời (cutouts), thẻ giấy xé (torn paper) và biểu đồ động. |
| **Màu nền & Chất liệu** | Nền bản đồ giấy da cổ (`#E8DEC5` Parchment), bản đồ địa hình vệ tinh 3D tối màu, kết hợp khung cảnh minh họa sơn dầu u tối khi kể chuyện bi kịch. | Nền giấy báo kem ấm (`#F3EFE6`) có bo tối 4 góc (vignette), lưới kẻ ô kỹ thuật mảnh (`grid`), và **đảo ngược sang nền Đen Tuyền (`#0D0D0D`)** ở câu chốt cao trào. |
| **Hệ thống Chữ (Typography)** | - Số năm lịch sử ở góc trên trái dùng **Serif cổ điển** (`1817`, `1515`, `1855`).<br>- Ghi chú giải thích dùng **chữ viết tay nghiêng (Handwritten/Script)** kèm mũi tên trắng/đỏ chỉ thẳng vào đối tượng.<br>- Con số thống kê lớn đặt trong hộp vàng (`#F5C518`) hoặc chữ đỏ/trắng khổng lồ. | - Kết hợp **Serif nghiêng thanh lịch** (*Instrument Serif / Playfair Display Italic*) cho vế dẫn và **Sans-Serif đậm nén** (*Bebas Neue / Oswald / Anton*) cho từ khóa chính.<br>- **Marker Swipe** (vệt bút dạ vàng `#F5C518` hoặc xanh `#1E40FF` quét dưới chữ).<br>- **Strikethrough** (gạch ngang đỏ qua từ cũ như `~~FUTURE~~` $\rightarrow$ nổi bật từ mới `PAST`). |
| **Chuyển động & Bố cục** | - **Persistent Chapter Tracker**: Bảng 3 câu hỏi lớn luôn ghim nhỏ ở góc trên bên phải màn hình để giữ mạch cấu trúc.<br>- **Map Radial Arrows**: Các mũi tên đỏ phóng tỏa tròn từ trung tâm lãnh thổ ra xung quanh.<br>- **Figurines & Badges**: Nhân vật chibi/minh họa có đế gỗ trượt trên bản đồ; khiên quốc huy (Shield), bong bóng bảo vệ (Glass Bubble), vòng tròn nét đứt xoay quanh con dấu `NEUTRAL`. | - **Persistent Live Counter**: Bộ đếm tiền/thời gian chạy liên tục ở góc trên phải (`BORROWED SINCE YOU HIT PLAY: $1,596,074`).<br>- **Split-Screen Torn Paper**: Chia đôi màn hình `200 YEARS AGO` vs `TODAY` bằng vệt giấy xé răng cưa dọc chính giữa.<br>- **Stacked Cutouts & Unit Charts**: Cọc tiền xếp chồng mọc lên theo nhịp; thanh ngang có viền giấy xé (`rough edge`); thẻ năm đóng dấu `2048 [PROJECTED]`. |
| **Thiết kế Âm thanh (SFX)** | Tiếng gió rít, tiếng bước chân hành quân, tiếng đóng dấu mộc lịch sử, tiếng vẽ nét mực trên bản đồ, tiếng chuông trầm chuyển chương. | **50% linh hồn của video**: Tiếng đếm số cơ học (ticker), tiếng bút dạ quẹt (marker swipe), tiếng giấy xé/đặt thẻ giấy (paper slap), tiếng gạch chữ (scratch), tiếng bass trầm khi đảo nền đen. |

---

## III. QUY TRÌNH CẬP NHẬT VÀO AGENT & SKILL TRONG TƯƠNG LAI

Khi người dùng muốn bổ sung hoặc nâng cấp bất kỳ hiệu ứng nào từ kho này vào hệ thống sản xuất chính (`.agent/skills/dung-video-tai-lieu/`):
1. **Bước 1**: Mở file `.md` tương ứng trong `KHO_LUU_TRU_GU_EDIT/` (`01_`, `02_`, `03_`, `04_`, `05_`) để chọn mã hiệu ứng (ví dụ: `TORN_PAPER_SPLIT`, `UNIT_ARRAY_GRID`, `PERSISTENT_CORNER_TRACKER`, `DARK_MODE_CLIMAX_INVERT`).
2. **Bước 2**: Bổ sung tài sản hình ảnh vào `04_HIEU_UNG_HINH_ANH_VA_BO_CUC/` và âm thanh vào `05_HIEU_UNG_AM_THANH_SFX/`.
3. **Bước 3**: Ra lệnh cho Agent đồng bộ từ `KHO_LUU_TRU_GU_EDIT/` sang `.agent/skills/dung-video-tai-lieu/references/gu-tham-my-va-kho-hieu-ung.md`, `index.html` (Pha 4) và `pha-5-xuat-video-mp4.py` (Pha 5).
