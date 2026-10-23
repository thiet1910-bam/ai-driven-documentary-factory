# BỘ NÃO TỔNG CHỈ HUY — HỆ THỐNG SẢN XUẤT VIDEO TÀI LIỆU (CHUẨN VĂN THIẾT V3.0)

Mọi hành động trong dự án này bắt buộc khởi đầu bằng việc đọc cổng chính siêu mỏng tại:
👉 **[`.agent/skills/dung-video-tai-lieu/SKILL.md`](./.agent/skills/dung-video-tai-lieu/SKILL.md)**

## Cấu Trúc Vận Hành Chuẩn Hóa (Đã Khử Tính Công Nghiệp & Phân Tầng Tri Thức)
1. **Cổng Điều Phối & Hợp Đồng 10 Điều Khoản (`SKILL.md` — 45 dòng, 5 KB):** Kiểm tra trạng thái dự án theo chuỗi file (`BRIEF.md` $\rightarrow$ `SPEC.md` $\rightarrow$ `ledger.json` $\rightarrow$ `REVIEW.md`) và chỉ nạp cẩm nang tương ứng với bước hiện tại.
2. **5 Cẩm Nang Chuyên Sâu (`references/`):**
   - [`01_doc_vi_va_brief.md`](./.agent/skills/dung-video-tai-lieu/references/01_doc_vi_va_brief.md): Cắt voice/text dài + Lên 3 tuyến truyện (`STORYLINES.md`) & chốt `BRIEF.md`.
   - [`02_luong_hoa_spec_va_luat_cam.md`](./.agent/skills/dung-video-tai-lieu/references/02_luong_hoa_spec_va_luat_cam.md): Quy đổi mọi tính từ cảm tính thành Con số (`SPEC.md`) + 8 Lệnh CẤM mặc định (`BANNED`).
   - [`03_dao_dien_chuyen_dong_va_motip.md`](./.agent/skills/dung-video-tai-lieu/references/03_dao_dien_chuyen_dong_va_motip.md): Luân phiên 5 Mô-típ sinh động (`scene_motif`) + Dòng chảy máy quay (`camera_move`) + Sổ cái vết cắt (`ledger.json` — `Cut-the-Curve` / `Zoom-Through`).
   - [`04_thiet_ke_am_thanh_va_nguyen_lieu.md`](./.agent/skills/dung-video-tai-lieu/references/04_thiet_ke_am_thanh_va_nguyen_lieu.md): Săn nguyên liệu đa nguồn theo mã `01.1, 01.2` + Thiết kế âm thanh vật lý (`SFX`) & Biểu đồ âm lượng (`Volume Envelope`).
   - [`05_kiem_duyet_p0_p1_review.md`](./.agent/skills/dung-video-tai-lieu/references/05_kiem_duyet_p0_p1_review.md): Kiểm toán toán học + Mở trình duyệt chụp lưới ảnh thực tế + Ghi biên bản `REVIEW.md` (P0/P1/P2).
3. **6 Công Cụ Thực Thi & Chốt Chặn Code (`scripts/`):**
   - `buoc_0_kiem_tra_moi_truong.py` & `khoi_tao_kho_hieu_ung.py`
   - `buoc_1_cat_kich_ban_va_brief.py`
   - `buoc_2_san_nguyen_lieu_theo_spec.py`
   - `buoc_3_kiem_toan_nhip_va_vet_cat.py` *(Chốt chặn tự động bắt lỗi đè chữ, lặp mô-típ, khoảng chết đứng hình)*
   - `buoc_4_chup_luoi_anh_review.py`
   - `buoc_5_xuat_video_mp4.py`
4. **Kho Sao Lưu Dự Phòng:** Bản `v1.0` và `v2.0` được bảo toàn tại `.agent/backups/skill_v1_0_backup/` và `.agent/backups/skill_v2_0_backup/`.
