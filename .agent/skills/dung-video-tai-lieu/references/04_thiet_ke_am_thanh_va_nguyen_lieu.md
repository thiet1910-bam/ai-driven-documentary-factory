# Bước 4: Săn Nguyên Liệu Đa Nguồn Theo Mã Phân Cấp & Thiết Kế Âm Thanh Vật Lý (`SFX` + `Volume Envelope`)

> **Đọc file này khi:** Tải nguyên liệu thực tế (Ảnh Polaroid, Sticker tách nền, Video B-Roll) và lập kịch bản âm thanh.

## 1. Quy Tắc Săn Nguyên Liệu Gắn Cứng Mã Phân Cấp (`01.1, 01.2, 01.3...`)
1. Chạy `python .agent/skills/dung-video-tai-lieu/scripts/buoc_2_san_nguyen_lieu_theo_spec.py <chi_dao_phan_canh_json> <out_dir>`.
2. Mọi file tải về tại `2_KHO_NGUYEN_LIEU/theo_tung_phan/<phan_XX>/` phải đặt tên khớp 100% với mã `stt_id`:
   - `images_polaroid/`: Ảnh tư liệu lịch sử (kèm các bản dự phòng `_alt2.jpg`, `_alt3.jpg`). Tự động đóng khung ngang (`reframe_to_landscape`) để không bao giờ cắt cụt đầu nhân vật.
   - `stickers_cutout/`: Nhân vật/vật thể tách nền bằng `rembg`, tự động lọc bỏ các đốm rác đen/trắng rời rạc ở 4 góc và bo viền kem dày `8px`.
   - `video_footage/`: Đoạn băng tư liệu chuyển động thật (`3.0s – 5.0s`) phục vụ cho `MOTIF_2_BROLL_KINETIC_OVERDRIVE`.
3. **Bắt buộc Kiểm Duyệt Bằng Mắt (`read_file`):** Đạo diễn AI phải mở xem trực tiếp từng bức ảnh/sticker vừa tải. Nếu ảnh sai niên đại hoặc sticker tách nền bị lẹm mặt, phải tráo ngay bằng bản `_alt2`/`_alt3` trước khi sang bước dựng.

---

## 2. Thiết Kế Âm Thanh Vật Lý Đa Lớp (`Cue Sheet SFX` — Học từ `sound-design.md`)

Mọi nhịp biến đổi thị giác trên màn hình bắt buộc phải có âm thanh vật lý đi kèm tại đúng mốc `t0` (sai số `<= 0.01s`), kèm lý do ngữ nghĩa (`sfx_reason`):

| Mã File Âm Thanh (`assets/sfx/`) | Khi nào kích hoạt? | Âm lượng chuẩn (`Volume`) |
| :--- | :--- | :--- |
| `paper_slide.wav` | Khi ảnh `POLAROID`, thẻ `DETECTIVE_TAPE_NOTE` hoặc biểu đồ `ROUGH_EDGE_BARS` trượt vào mặt bàn. | `35%` (`0.35`) |
| `sticker_pop_soft.wav` | Khi nhân vật/vật thể tách nền `STICKER` bật lên có độ nảy lò xo. | `40%` (`0.40`) |
| `marker_swipe.wav` | Khi bút dạ vàng quét ngang từ khóa trong `HEADLINE` hoặc vẽ vòng `RED_INK_CIRCLE`. | `38%` (`0.38`) |
| `red_pen_scratch.wav` | Khi gạch ngang chữ đỏ (`strikethrough`) hoặc viết ghi chú `HANDWRITTEN_CALLOUT`. | `42%` (`0.42`) |
| `rubber_stamp.wav` | Khi con dấu mộc đỏ `STAMP` đập mạnh xuống mặt bàn chốt luận điểm. | `45%` (`0.45`) |
| `paper_rip_split.wav` | Khi xé đôi màn hình (`TORN_PAPER_SPLIT`) hoặc chuyển cảnh `TORN_PAPER_WIPE`. | `45%` (`0.45`) |
| `counter_tick_loop.wav` | Khi bộ đếm `NUMBER_COUNTER` hoặc ma trận 100 người `WAFFLE_100_ARRAY` nhảy số. | `30%` (`0.30`) |
| `map_whoosh.wav` | Khi máy quay bay trên bản đồ (`MAP_FLYOVER_TRACK`) hoặc chuyển cảnh `CUT_THE_CURVE_LEFT`. | `35%` (`0.35`) |
| `low_boom.wav` | Khi đảo ngược sang nền Đen Cao Trào (`bg_mode: "DARK_CLIMAX"`) hoặc mở màn cú sốc. | `50%` (`0.50`) |
| `typewriter.wav` | Khi gõ chữ niên đại lịch sử hoặc trích dẫn hồ sơ mật. | `30%` (`0.30`) |

---

## 3. Biểu Đồ Uốn Lượn Nhạc Nền (`FFmpeg Volume Envelope`)
Không bao giờ để nhạc nền (BGM) chạy phẳng lì một mức âm lượng từ đầu tới cuối. Áp dụng đường bao âm lượng động:
- **0s – 12s (Mở màn / Hook):** Âm lượng nhạc nền dâng lên `22%` để tạo lực hút kịch tính.
- **12s – Trước kết 20s (Thân bài / Giải thích số liệu):** Tự động ép nhỏ xuống `10% – 12%` (Ducking) để giọng đọc (Voiceover) và tiếng động `SFX` nổi bật tuyệt đối.
- **20s cuối (Cao trào / Dark Climax & Payoff):** Đẩy âm lượng nhạc nền lên `25%` tạo dư âm cảm xúc mạnh trước khi hạ màn.
