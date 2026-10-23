---
name: dung-video-tai-lieu
description: "Đạo diễn & sản xuất video tài liệu điện ảnh (Vox / Johnny Harris / Cartographic). Biến kịch bản & giọng đọc thành video MP4 1920x1080 qua chuỗi trạng thái BRIEF.md -> SPEC.md -> ledger.json -> REVIEW.md. Kích hoạt: /dung-video-tai-lieu"
---

# Hệ Thống Đạo Diễn Video Tài Liệu Điện Ảnh (Chuẩn Văn Thiết v3.0)

## 1. Kiểm tra Trạng thái Dự án (Định tuyến 1 lần — Route Once, Then Leave)
Kiểm tra thư mục phần đang làm (`2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/`) và khớp dòng đầu tiên:

| Trạng thái trên ổ cứng | Hành động bắt buộc |
| :--- | :--- |
| Chưa tách kịch bản/voice dài | Đọc `references/01_doc_vi_va_brief.md` $\rightarrow$ Chạy `buoc_1_cat_kich_ban_va_brief.py` $\rightarrow$ Xuất `BRIEF.md`. |
| Đã có `BRIEF.md`, chưa có `SPEC.md` & `ledger.json` | Đọc `references/02_luong_hoa_spec_va_luat_cam.md` + `03_dao_dien_chuyen_dong_va_motip.md` $\rightarrow$ Xuất `SPEC.md`, `ledger.json`, `chi_dao_phan_canh.json`. |
| Đã duyệt `SPEC.md`, chưa tải đủ nguyên liệu | Đọc `references/04_thiet_ke_am_thanh_va_nguyen_lieu.md` $\rightarrow$ Chạy `buoc_2_san_nguyen_lieu_theo_spec.py` $\rightarrow$ Kiểm tra ảnh bằng `read_file`. |
| Đã có nguyên liệu, chưa có `REVIEW.md` đạt `0 P0` | Chạy `buoc_3_kiem_toan_nhip_va_vet_cat.py` + `buoc_4_chup_luoi_anh_review.py` $\rightarrow$ Đọc `references/05_kiem_duyet_p0_p1_review.md` $\rightarrow$ Xuất `REVIEW.md`. |
| Đã duyệt Bàn dựng HTML & `REVIEW.md` đạt chuẩn | Chạy `buoc_5_xuat_video_mp4.py --part <phan_XX>` $\rightarrow$ Hậu kiểm khung hình MP4 thực tế. |

## 2. Hợp đồng 10 Điều khoản Cứng (Hard Contract — Chống Công Nghiệp)
`python .agent/skills/dung-video-tai-lieu/scripts/buoc_3_kiem_toan_nhip_va_vet_cat.py` tự động chặn nếu vi phạm:

1. **Diệt trừ Tính từ:** Cấm viết "sinh động, hiện đại, mượt mà" chung chung. Mọi quyết định phải ghi thành **con số** trong `SPEC.md` trước khi dựng.
2. **Luật Khoảng Chết (`dead_stretch <= 2.8s`):** Cấm để màn hình đứng im chờ giọng đọc quá `2.8s`. Mỗi cảnh phải chia thành các nhịp nhân quả (`01.1`, `01.2`, `01.3`...) nối tiếp nhau.
3. **Luật Sân Khấu Sạch (`max_concurrent <= 3`):** Tại mọi thời điểm `t`, tối đa `3` phần tử trung tâm hiển thị cùng lúc. Phần tử cũ phải thoát (`Exit`) trước khi phần tử mới vào.
4. **Luật Tỷ Lệ Chủ Thể (`hero_fill >= 40%`):** Vật thể chính phải chiếm tối thiểu `40%` chiều rộng hoặc chiều cao khung hình `1920x1080`.
5. **Luật Bất Đối Xứng Mô-Típ (`no_motif_repeat`):** Hai cảnh liên tiếp cấm trùng `scene_motif` (bắt buộc xoay vòng 5 Mô-típ trong `03_dao_dien_chuyen_dong_va_motip.md`).
6. **Luật Bảo Toàn Động Lượng Vết Cắt (`ledger.json` Seam Law):** Cấm cắt cảnh khi hình đã dừng hẳn. Điểm nối giữa Cảnh A và Cảnh B phải khớp trục (`X/Y/Z`), cùng dấu vận tốc và cắt ngay trên đỉnh đường cong (`Cut-the-Curve` / `Zoom-Through`).
7. **Luật Cấm Lắc Lư Câu Giờ (`no_idle_wobble`):** Cấm dùng vòng lặp `Math.sin` nhấp nhô tại chỗ để lấp thời gian trống.
8. **Luật Đa Chất Liệu (`mixed_media >= 40%`):** Tối thiểu `40%` tổng số nhịp phải là `VIDEO_CLIP` quay thật, `STICKER` tách nền, Bản đồ 2.5D/3D hoặc Biểu đồ động (cấm dùng 100% khung `POLAROID` tĩnh).
9. **Luật Âm Thanh Vật Lý & Biểu Đồ Âm Lượng:** Mọi chuyển động phải gắn `SFX` khớp tới `0.01s`; nhạc nền phải uốn lượn theo `Volume Envelope`.
10. **Luật Cổng Dừng & Kiểm Duyệt Mắt (`REVIEW.md`):** Dừng cứng sau mỗi bước để người dùng duyệt. Cấm giao sản phẩm khi còn lỗi `P0` trên lưới ảnh chụp thật.

## 3. Bảng Điều Hướng Nạp Theo Tầng (Chỉ đọc file khi tới đúng bước)

| Nhu cầu thực thi | File cẩm nang phải đọc (`references/` & `templates/`) | Script thực thi (`scripts/`) |
| :--- | :--- | :--- |
| Kiểm tra môi trường & Kho đồ họa/SFX | — | `buoc_0_kiem_tra_moi_truong.py`, `khoi_tao_kho_hieu_ung.py` |
| Cắt Voice/Text dài & Lên 3 Tuyến truyện | `references/01_doc_vi_va_brief.md`, `templates/mau_01_brief_va_storylines.md` | `buoc_1_cat_kich_ban_va_brief.py` |
| Lượng hóa Con số & Lập Danh sách CẤM | `references/02_luong_hoa_spec_va_luat_cam.md`, `templates/mau_02_spec_thong_so.md` | — |
| Chọn 5 Mô-típ, Máy quay & Vết cắt Vector | `references/03_dao_dien_chuyen_dong_va_motip.md`, `templates/mau_03_so_cai_chuyen_canh_ledger.json` | `buoc_3_kiem_toan_nhip_va_vet_cat.py` |
| Săn Ảnh/Sticker/Video & Trộn SFX | `references/04_thiet_ke_am_thanh_va_nguyen_lieu.md` | `buoc_2_san_nguyen_lieu_theo_spec.py` |
| Chụp lưới ảnh Browser & Ghi `REVIEW.md` | `references/05_kiem_duyet_p0_p1_review.md`, `templates/mau_04_bien_ban_kiem_duyet_review.md` | `buoc_4_chup_luoi_anh_review.py` |
| Xuất MP4 1920x1080 @ 30fps hoàn chỉnh | `references/05_kiem_duyet_p0_p1_review.md` (§4) | `buoc_5_xuat_video_mp4.py` |
