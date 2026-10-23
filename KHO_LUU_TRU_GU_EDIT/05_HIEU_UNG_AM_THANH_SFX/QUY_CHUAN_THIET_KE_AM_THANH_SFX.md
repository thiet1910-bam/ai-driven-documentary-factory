# 🔊 QUY CHUẨN THIẾT KẾ ÂM THANH & HIỆU ỨNG FOLEY (SOUNDSCAPE & SFX DESIGN)

> [!IMPORTANT]
> Trích dẫn nguyên văn từ nghiên cứu Gu Edit 2 (`uIHJvUVaB34` @ `07:26 – 07:55`):
> *"Visuals are only one half of the equation when it comes to these engaging Vox style animations. The other crucial half relies on immersive sound design... **Honestly, 50% of the perceived quality in motion graphics comes directly from the soundscape.** This includes perfectly timed sound effects, ambient textures, and a high-quality voiceover."*

---

## 1. PHÂN LOẠI 4 NHÓM THƯ MỤC ÂM THANH TRONG KHO (`05_HIEU_UNG_AM_THANH_SFX/`)

| Thư mục con | Các file `.WAV` chuẩn | Khi nào được phép kích hoạt? (Quy tắc Có Lý Do) |
| :--- | :--- | :--- |
| **`sfx_chuyen_canh/`** | `map_whoosh.wav`<br>`paper_rip_split.wav`<br>`camera_glide_soft.wav` | - `map_whoosh.wav`: Khi mở bản đồ mới hoặc camera lướt nhanh từ vùng này sang vùng khác.<br>- `paper_rip_split.wav`: Khi xé đôi màn hình (`Torn-Paper Split` giữa `XƯA` và `NAY`). |
| **`sfx_text_va_so_lieu/`** | `marker_swipe.wav`<br>`typewriter.wav`<br>`counter_tick_loop.wav`<br>`red_pen_scratch.wav` | - `marker_swipe.wav`: Khi vệt bút dạ vàng/xanh quét qua từ khóa chính.<br>- `typewriter.wav` / `counter_tick_loop.wav`: Khi bộ đếm tiền/năm (`NUMBER_COUNTER`) nhảy số hoặc khi lưới 100 hình người quét phần trăm.<br>- `red_pen_scratch.wav`: Khi gạch bỏ chữ (`~~FUTURE~~`) hoặc khoanh vòng mực đỏ. |
| **`sfx_hinh_anh_va_stamp/`** | `paper_slide.wav`<br>`sticker_pop_soft.wav`<br>`rubber_stamp.wav`<br>`low_boom.wav` | - `paper_slide.wav`: Khi đặt tấm ảnh Polaroid hoặc phiếu hồ sơ xuống mặt bàn.<br>- `sticker_pop_soft.wav`: Khi bật nhân vật tách nền (`STICKER` / `FIGURINE`) hoặc cọc tiền xếp chồng.<br>- `rubber_stamp.wav`: Khi đóng dấu mộc đỏ (`SOLD FOR $7`, `NEUTRAL`, `PROJECTED`).<br>- `low_boom.wav`: Khi đảo ngược màn hình sang nền đen (`Pitch-Black Climax`) hoặc mở cảnh bi kịch lịch sử. |
| **`sfx_ambient_nen/`** | `arctic_wind_subtle.wav`<br>`ocean_waves_ship.wav`<br>`vinyl_room_tone.wav` | Lớp âm thanh nền cực nhẹ (`volume: 0.08 – 0.12`) dưới giọng đọc để lấp đầy khoảng trống không gian mà không làm lấn át giọng kể chuyện. |

---

## 2. QUY TẮC VÀNG KHI PHỐI ÂM THANH (AUDIO MIXING & TIMING RULES)

1. **Độ trễ 0.00s so với Chuyển động (`Frame-Accurate Sync`)**:
   - Tiếng `rubber_stamp.wav` phải nổ đúng vào frame con dấu chạm mặt giấy (`t0 + 0.12s`), không được kêu trước hay kêu trễ.
   - Tiếng `marker_swipe.wav` phải bắt đầu đúng frame vệt màu vàng bắt đầu quét (`t0`).
2. **Tỷ lệ Âm lượng Chuẩn (`Master Gain Staging`)**:
   - **Track A1 (`Voiceover`)**: `100%` (`0 dB` — ưu tiên số 1, rõ ràng tuyệt đối).
   - **Track A2 (`Foley SFX`)**: `38% – 45%` (`-7.5 dB` — nghe êm tai, giòn nhưng không làm giật mình hay đè giọng đọc).
   - **Ambient Texture**: `8% – 12%` (`-20 dB`).
3. **Khả năng Tự Sinh SFX Vật Lý Bằng Python (`Procedural Python Audio Synthesis`)**:
   - Theo đúng kiến trúc từ Gu 2 (`09:15`): Khi cần một hiệu ứng âm thanh đặc thù (như tiếng đếm tiền tăng tốc theo hàm mũ, tiếng giấy xé dài 0.6s hay tiếng chuông trầm chuyển chương), hệ thống có thể dùng Python (`wave` + `math` + `struct`) để tổng hợp sóng âm (`filtered noise + frequency sweep + envelope decay`) trực tiếp ra file `.wav` `44100Hz 16-bit`.
