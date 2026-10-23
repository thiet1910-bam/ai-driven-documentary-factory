---
name: dung-video-tai-lieu
description: "Đạo diễn & sản xuất video tài liệu điện ảnh (Vox / Johnny Harris / Lemmino / MagnatesMedia — Kiến trúc 5 Thế Giới Thị Giác v2.0 chống lặp lại cho video 5–30+ phút). Biến kịch bản & giọng đọc thành video MP4 1920x1080 qua BRIEF.md -> SPEC.md -> ledger.json -> REVIEW.md. Kích hoạt: /dung-video-tai-lieu"
---

# Hệ Thống Đạo Diễn Video Tài Liệu Đa Thế Giới (Chuẩn Văn Thiết v2.0 — Multi-World Architecture)

## 1. Kiểm tra Trạng thái Dự án (Định tuyến 1 lần — Route Once, Then Leave)
Kiểm tra thư mục phần đang làm (`2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/`) và khớp dòng đầu tiên:

| Trạng thái trên ổ cứng | Hành động bắt buộc |
| :--- | :--- |
| Chưa tách kịch bản/voice dài | Đọc `references/01_doc_vi_va_brief.md` $\rightarrow$ Chạy `buoc_1_cat_kich_ban_va_brief.py` $\rightarrow$ Xuất `BRIEF.md` (**Dừng Cổng 1**). |
| Đã có `BRIEF.md`, chưa có `SPEC.md` & `ledger.json` | Đọc `references/02_luong_hoa_spec_va_luat_cam.md` + `03_dao_dien_chuyen_dong_va_motip.md` $\rightarrow$ Xuất `SPEC.md`, `ledger.json`, `chi_dao_phan_canh.json` (**Dừng Cổng 2**). |
| Đã duyệt `SPEC.md`, chưa tải đủ nguyên liệu | Đọc `references/04_thiet_ke_am_thanh_va_nguyen_lieu.md` $\rightarrow$ Chạy `buoc_2_san_nguyen_lieu_theo_spec.py` $\rightarrow$ Kiểm tra 100% ảnh/video bằng `read_file` (**Dừng Cổng 3**). |
| Đã có nguyên liệu, chưa có `REVIEW.md` đạt `0 P0` | Chạy `buoc_3_kiem_toan_nhip_va_vet_cat.py` + `buoc_4_chup_luoi_anh_review.py` $\rightarrow$ Đọc `references/05_kiem_duyet_p0_p1_review.md` $\rightarrow$ Xuất `REVIEW.md` (**Dừng Cổng 4**). |
| Đã duyệt Bàn dựng HTML & `REVIEW.md` đạt chuẩn | Chạy `buoc_5_xuat_video_mp4.py --part <phan_XX>` $\rightarrow$ Hậu kiểm khung hình MP4 thực tế (**Dừng Cổng 5**). |

## 2. Hợp đồng 12 Điều khoản Cứng v2.0 (Hard Contract — Triệt Tiêu Vẻ Ngoài Công Nghiệp)
`python .agent/skills/dung-video-tai-lieu/scripts/buoc_3_kiem_toan_nhip_va_vet_cat.py` tự động chặn nếu vi phạm:

1. **Diệt trừ Tính từ:** Cấm viết "sinh động, hiện đại, mượt mà" chung chung. Mọi quyết định phải ghi thành **con số** trong `SPEC.md`.
2. **Luật Đa Thế Giới (`WORLD_VARIETY_GATE`):** Video dài 5–30 phút cấm nhốt người xem trên 1 mặt bàn Polaroid! Bắt buộc luân chuyển 5 Thế Giới Thị Giác (`world_type` / `scene_motif`):
   - `WORLD_1_FULL_MAP` (`MOTIF_3_CARTOGRAPHIC_3D_FLYOVER`): Bản đồ địa chính trị toàn màn hình `1920x1080` + Đường hành trình vẽ động (`MAP_ROUTE`).
   - `WORLD_2_CINEMA_FULLBLEED` (`MOTIF_2_BROLL_KINETIC_OVERDRIVE`): Tư liệu Video/Ảnh tràn 100% màn hình + Thanh đen điện ảnh `2.35:1` + Đèn chiếu tiêu điểm (`SPOTLIGHT_XRAY`).
   - `WORLD_3_DETECTIVE_CANVAS` (`MOTIF_1_DETECTIVE_CANVAS_PAN`): Bàn điều tra đa hướng nối sợi chỉ đỏ (`RED_STRING_LINK`), đảo vị trí Trái/Phải/Trung tâm liên tục.
   - `WORLD_4_DATA_STAGE` (`MOTIF_5_DATA_STORY_PROGRESSION`): Sân khấu dữ liệu toàn màn hình (không có Polaroid chia đôi), biểu đồ `SVG_LINE_CHART` / `TIMELINE_SCROLLER` / `ROUGH_EDGE_BARS` chiếm trung tâm.
   - `WORLD_5_ARCHIVE_XRAY` (`MOTIF_4_EVIDENCE_SPLIT_COLLISION`): Phóng đại văn kiện/tờ báo cổ hoặc đối đầu 2 thái cực kèm quét bút dạ quang (`SPOTLIGHT_XRAY`).
3. **Luật Cấm Lặp Bố Cục 2 Cột (`LAYOUT_ASYMMETRY_GATE`):** Cấm đặt tư liệu chính (`Hero Asset`) ở cùng một phía (ví dụ góc trái `x < 320`) quá **2 cảnh liên tiếp**! Trong một phần (7–9 cảnh), ít nhất `50%` số cảnh phải là Toàn màn hình (`w >= 1350`), Trung tâm hoặc Đảo sang phải (`x >= 720`).
4. **Luật Khoảng Chết (`dead_stretch <= 4.0s`):** Cấm để màn hình đứng im chờ giọng đọc. Mỗi cảnh chia thành các nhịp nhân quả (`01.1`, `01.2`, `01.3`...).
5. **Luật Sân Khấu Sạch (`max_concurrent <= 3`):** Tại mọi thời điểm `t`, tối đa `3` phần tử hiển thị cùng lúc.
6. **Luật Tỷ Lệ Chủ Thể (`hero_fill >= 40%`):** Vật thể chính phải chiếm tối thiểu `40%` chiều rộng hoặc chiều cao khung hình `1920x1080`.
7. **Luật Bảo Toàn Động Lượng Vết Cắt (`SEAM_MOMENTUM_GATE`):** Cấm cắt cảnh khi hình đã dừng hẳn. Điểm nối giữa Cảnh A và Cảnh B phải thực thi vật lý: `ZOOM_THROUGH`, `INVERSE_ZOOM`, `CUT_THE_CURVE_LEFT`, `RACK_FOCUS_BLUR`, hoặc `PAPER_RIP_WIPE`.
8. **Luật Biến Đổi HUD Theo Thế Giới (`Adaptive HUD`):** Cấm đóng đinh 4 góc HUD suốt 30 phút. Ở `WORLD_2_CINEMA_FULLBLEED` bật thanh đen điện ảnh `Letterbox` và ẩn lưới bàn giấy; ở `WORLD_4_DATA_STAGE` chuyển sang sân khấu tối giản.
9. **Luật Đa Chất Liệu (`mixed_media >= 50%`):** Tối thiểu `50%` tổng số nhịp phải là `VIDEO_CLIP`, `STICKER`, `MAP_ROUTE`, `SPOTLIGHT_XRAY`, `TIMELINE_SCROLLER`, `SVG_LINE_CHART`, `WAFFLE_100_ARRAY`, `ROUGH_EDGE_BARS`.
10. **Luật Âm Thanh 3 Tầng & Biểu Đồ Nhạc Nền (`3-Layer Soundscape`):** Kết hợp `Voiceover` + `Dynamic BGM Bed` (tự động dâng ở đầu/cuối phần & chuyển cảnh, hạ xuống khi thuyết minh) + `Precision Foley SFX`.
11. **Luật Chống Quan Liêu (`Zero Rubber-Stamp Rule`):** Bắt buộc dùng `read_file` mở xem 100% nguyên liệu tải về và 100% khung hình chụp từ trình duyệt trước khi mở Cổng Dừng.
12. **Luật 5 Cổng Dừng Bắt Buộc (`5 Hard Gates`):** Dừng cứng chờ lệnh `"Duyệt"` của người dùng sau mỗi bước (Bước 1 -> Bước 5).

## 3. Bảng Điều Hướng Nạp Theo Tầng (Chỉ đọc file khi tới đúng bước)

| Nhu cầu thực thi | File cẩm nang phải đọc (`references/` & `templates/`) | Script thực thi (`scripts/`) |
| :--- | :--- | :--- |
| Kiểm tra môi trường & Kho đồ họa/SFX | — | `buoc_0_kiem_tra_moi_truong.py`, `khoi_tao_kho_hieu_ung.py` |
| Cắt Voice/Text dài & Lên 3 Tuyến truyện | `references/01_doc_vi_va_brief.md`, `templates/mau_01_brief_va_storylines.md` | `buoc_1_cat_kich_ban_va_brief.py` |
| Lượng hóa Con số & Lập Danh sách CẤM | `references/02_luong_hoa_spec_va_luat_cam.md`, `templates/mau_02_spec_thong_so.md` | — |
| Chọn 5 Thế Giới, Máy quay & Vết cắt Vector | `references/03_dao_dien_chuyen_dong_va_motip.md`, `templates/mau_03_so_cai_chuyen_canh_ledger.json` | `buoc_3_kiem_toan_nhip_va_vet_cat.py` |
| Săn Ảnh/Sticker/Video & Trộn SFX | `references/04_thiet_ke_am_thanh_va_nguyen_lieu.md` | `buoc_2_san_nguyen_lieu_theo_spec.py` |
| Chụp lưới ảnh Browser & Ghi `REVIEW.md` | `references/05_kiem_duyet_p0_p1_review.md`, `templates/mau_04_bien_ban_kiem_duyet_review.md` | `buoc_4_chup_luoi_anh_review.py` |
| Xuất MP4 1920x1080 @ 30fps hoàn chỉnh | `references/05_kiem_duyet_p0_p1_review.md` (§4) | `buoc_5_xuat_video_mp4.py` |
