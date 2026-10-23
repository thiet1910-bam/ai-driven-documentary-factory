# BẢNG THÔNG SỐ ĐỊNH LƯỢNG & DANH SÁCH CẤM (`SPEC.md`)

```text
GOAL:    [Cảm xúc & nhận thức của khán giả sau khi xem xong phần này, 1 câu]
OUTPUT:  1920x1080 @ 30fps, thời lượng [XXX.X]s ([XXXX] frames)
LOOK:    Nền chính: CREAM_GRID (#F4EFE6, 3% hạt giấy) + PARCHMENT_MAP (#E8DCC4) + 1 cảnh cao trào DARK_CLIMAX (#0B0C0E);
         Mực chính: #111317 | Điểm nhấn Đỏ điều tra: #D92318 | Điểm nhấn Vàng bút dạ: #F5C518;
         Chữ tiêu đề: Playfair Display Bold Italic &Oswald Condensed (>= 48px) | Chữ chú thích: >= 28px.
NUMBERS: max_dead_stretch <= 2.8s | max_concurrent <= 3 | hero_fill >= 40% | mixed_media_ratio >= 40%
MOTION:  Vào cảnh: expo.out (0.45s) | Thoát cảnh: power3.in (0.30s) | Lò xo: damping 0.75 | Motion blur vết cắt: 10px-18px
```

## 1. Bảng Phân Bổ 5 Mô-Típ Luân Phiên (`scene_motif` — Cấm 2 Cảnh Liền Kề Trùng Nhau)

| Mã Cảnh | Mốc Giây (`t0 -> t1`) | Mô-típ Dàn Dựng (`scene_motif`) | Chuyển Động Máy Quay (`camera_move`) | Kỹ Thuật Nối Cảnh (`seam_transition`) | Số Tư Liệu Con (`XX.1..XX.4`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `sc_01` | `0.0s -> 11.0s` | `MOTIF_2_BROLL_KINETIC_OVERDRIVE` | `KEN_BURNS_PUSH` | `CUT_THE_CURVE_LEFT` | `4 nhịp (01.1 -> 01.4)` |
| `sc_02` | `11.0s -> 24.5s` | `MOTIF_1_DETECTIVE_CANVAS_PAN` | `DESK_PAN_ZOOM` | `ZOOM_THROUGH` | `4 nhịp (02.1 -> 02.4)` |
| `sc_03` | `24.5s -> 38.0s` | `MOTIF_3_CARTOGRAPHIC_3D_FLYOVER` | `MAP_FLYOVER_TRACK` | `TORN_PAPER_WIPE` | `4 nhịp (03.1 -> 03.4)` |

## 2. Danh Sách CẤM Mặc Định Của Phim Này (`BANNED`)
- **CẤM** đặt 1 Ảnh Polaroid bên trái + 1 Hộp chữ bên phải lặp lại ở 2 cảnh liên tiếp.
- **CẤM** để bất kỳ khoảng thời gian nào `> 2.8s` không có phần tử mới Vào/Thoát hoặc đổi góc máy quay.
- **CẤM** dùng vòng lặp `Math.sin` nhấp nhô tại chỗ để câu giờ.
- **CẤM** cắt cảnh khi hình đã dừng hẳn hoặc dùng mờ dần (crossfade) không có vật dẫn đường (`Carrier`).
- **CẤM** để quá `3` phần tử trung tâm hiển thị cùng lúc tại bất kỳ mili-giây nào.
- **CẤM** in mã kỹ thuật `[SC_01]`, `[STT_01]` lên màn hình `1920x1080`.
