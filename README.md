# AI-Driven Documentary Factory (`v1.0`)

Hệ thống sản xuất Video Tài Liệu Điều Tra Lịch Sử & Địa Chính Trị theo phong cách **Vox / Johnny Harris / MagnatesMedia** (`1920x1080 @ 30fps`), vận hành bằng Skill `.agent/skills/dung-video-tai-lieu` với **5 Bước — 5 Cổng Dừng Bắt Buộc (Hard Gates)** và **Quy tắc Chống Quan Liêu (Zero Rubber-Stamp Rule)**.

## Cấu Trúc Thư Mục Chuẩn 3 Ngăn

```text
AI-Driven Documentary Factory/
├── .agent/skills/dung-video-tai-lieu/   # Bộ Skill 5 Bước + Scripts tự động hóa + Templates + Kho SFX/FX
├── 1_INPUT_NHAN_SU/                     # Kịch bản gốc, cấu hình cắt phần & timestamps từng phần (phan_01 -> phan_05)
├── 2_KHO_NGUYEN_LIEU/
│   ├── dung_chung_toan_kenh/            # Kho SFX (.wav), Textures giấy nhăn HD & FX Overlays dùng chung
│   └── theo_tung_phan/                  # Hồ sơ từng phần (BRIEF.md, chi_dao_phan_canh.json, REVIEW.md, images_polaroid, stickers_cutout, director_review_frames)
├── 3_OUTPUT_VIDEO_HOAN_CHINH/           # Đầu ra video .mp4 từng phần và bản ghép nối hoàn chỉnh
├── KHO_LUU_TRU_GU_EDIT/                 # Cẩm nang tư duy đạo diễn & quy chuẩn thẩm mỹ kênh
├── index.html                           # Bàn dựng 5-Track NLE HTML5 Canvas / Web Audio trực quan
└── AGENTS.md                            # Quy tắc vận hành bắt buộc cho AI Agent
```

## Quy Trình 5 Bước — 5 Cổng Dừng Bắt Buộc

1. **Bước 1:** Bóc tách kịch bản & giọng đọc theo mạch ý nghĩa (`buoc_1_cat_kich_ban_va_brief.py`) -> Lập `BRIEF.md` -> **Cổng Dừng 1**.
2. **Bước 2:** Thiết kế Blueprint đạo diễn (`chi_dao_phan_canh.json` & `ledger.json`) -> Kiểm toán nhịp & chống đè chữ (`buoc_3_kiem_toan_nhip_va_vet_cat.py`) -> **Cổng Dừng 2**.
3. **Bước 3:** Săn lùng nguyên liệu lịch sử xác thực (`buoc_2_san_nguyen_lieu_theo_spec.py`), tách nền Sticker (`rembg`), kiểm duyệt 100% bằng mắt (`read_file`) -> **Cổng Dừng 3**.
4. **Bước 4:** Chụp lưới ảnh 17 khung hình trình duyệt thực tế (`buoc_4_chup_luoi_anh_review.py`), kiểm duyệt mắt & lập biên bản `REVIEW.md` -> **Cổng Dừng 4**.
5. **Bước 5:** Kết xuất Video `.mp4` độc lập (`buoc_5_xuat_video_mp4.py`), hậu kiểm khung hình MP4 thực tế -> **Cổng Dừng 5**.
