# BẢNG THÔNG SỐ ĐỊNH LƯỢNG & DANH SÁCH CẤM (`SPEC.md`) — `phan_03`

```text
GOAL:    Khán giả bị cuốn vào 3 khúc cua lịch sử nghẹt thở của Alaska (1896 -> 1925 -> 1942) mà không có bất kỳ giây nào màn hình đứng chờ giọng đọc.
OUTPUT:  1920x1080 @ 30fps, thời lượng 150.73s (4,522 frames)
LOOK:    Nền luân phiên theo tâm lý: CREAM_GRID (#F4EFE6) cho điều tra & đối chiếu số liệu + PARCHMENT_MAP (#E8DCC4) cho hành trình địa lý + DARK_CLIMAX (#0B0C0E) cho chiến sự Thế chiến II 1942 tại đảo Attu;
         Mực chính: #111317 | Đỏ điều tra: #D92318 | Vàng bút dạ: #F5C518 | Xanh băng giá: #1D4ED8;
         Chữ tiêu đề: Playfair Display Bold Italic & Oswald Condensed (>= 48px) | Chữ chú thích: >= 28px.
NUMBERS: max_dead_stretch <= 2.8s (Tuyệt đối 0 cảnh báo P1 > 4.5s) | max_concurrent <= 3 | hero_fill >= 42% | mixed_media_ratio >= 52%
MOTION:  Vào cảnh: expo.out (0.45s) | Thoát cảnh: power3.in (0.30s) | Lò xo: damping 0.75 | Motion blur vết cắt: 10px (chữ) / 18px (khung cảnh)
```

## 1. Bảng Phân Bổ 5 Mô-Típ Luân Phiên Cho 8 Phân Cảnh (`scene[i].scene_motif != scene[i-1].scene_motif`)

| Mã Cảnh | Mốc Giây (`t0 -> t1`) | Thời Lượng | Mô-típ Dàn Dựng (`scene_motif`) | Chuyển Động Máy Quay (`camera_move`) | Kỹ Thuật Nối Cảnh (`seam_transition`) | Chế Độ Nền (`bg_mode`) | Số Nhịp Con (`Sub-Beats`) |
| :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: |
| **`sc_01`** | `0.0s -> 17.8s` | `17.8s` | `MOTIF_1_DETECTIVE_CANVAS_PAN` | `DESK_PAN_ZOOM` | `ZOOM_THROUGH` | `CREAM_GRID` | `6 nhịp (01.1 -> 01.6)` |
| **`sc_02`** | `17.8s -> 37.5s` | `19.7s` | `MOTIF_2_BROLL_KINETIC_OVERDRIVE` | `KEN_BURNS_PUSH` | `TORN_PAPER_WIPE` | `PARCHMENT_MAP` | `6 nhịp (02.1 -> 02.6)` |
| **`sc_03`** | `37.5s -> 61.5s` | `24.0s` | `MOTIF_4_EVIDENCE_SPLIT_COLLISION` | `DESK_PAN_ZOOM` | `CUT_THE_CURVE_LEFT` | `CREAM_GRID` | `7 nhịp (03.1 -> 03.7)` |
| **`sc_04`** | `61.5s -> 87.5s` | `26.0s` | `MOTIF_3_CARTOGRAPHIC_3D_FLYOVER` | `MAP_FLYOVER_TRACK` | `ZOOM_THROUGH` | `PARCHMENT_MAP` | `8 nhịp (04.1 -> 04.8)` |
| **`sc_05`** | `87.5s -> 103.0s` | `15.5s` | `MOTIF_5_DATA_STORY_PROGRESSION` | `DRAMATIC_PULL_BACK` | `INVERSE_ZOOM_ARRIVAL` | `CREAM_GRID` | `5 nhịp (05.1 -> 05.5)` |
| **`sc_06`** | `103.0s -> 126.2s` | `23.2s` | `MOTIF_2_BROLL_KINETIC_OVERDRIVE` | `KEN_BURNS_PUSH` | `CUT_THE_CURVE_LEFT` | **`DARK_CLIMAX`** | `7 nhịp (06.1 -> 06.7)` |
| **`sc_07`** | `126.2s -> 137.8s` | `11.6s` | `MOTIF_4_EVIDENCE_SPLIT_COLLISION` | `DESK_PAN_ZOOM` | `ZOOM_THROUGH` | `CREAM_GRID` | `4 nhịp (07.1 -> 07.4)` |
| **`sc_08`** | `137.8s -> 150.73s` | `12.93s` | `MOTIF_3_CARTOGRAPHIC_3D_FLYOVER` | `MAP_FLYOVER_TRACK` | `INVERSE_ZOOM_ARRIVAL` | `PARCHMENT_MAP` | `4 nhịp (08.1 -> 08.4)` |

> **Kiểm chứng Chống Lặp Mô-típ:** `MOTIF_1` $\rightarrow$ `MOTIF_2` $\rightarrow$ `MOTIF_4` $\rightarrow$ `MOTIF_3` $\rightarrow$ `MOTIF_5` $\rightarrow$ `MOTIF_2` $\rightarrow$ `MOTIF_4` $\rightarrow$ `MOTIF_3`. **Tuyệt đối `0` cặp cảnh liền kề trùng mô-típ!**

## 2. Danh Sách CẤM Mặc Định Của `phan_03` (`BANNED`)
1. **CẤM** để đoạn leo núi băng Chilkoot (`28.3s -> 36.8s`) hay đoạn chạy tiếp sức bão tuyết (`78.3s -> 85.5s`) đứng yên 1 tấm ảnh quá `2.8 giây` — bắt buộc tách thành chuỗi tư liệu nối tiếp (`Visual Relay`) + khoanh mực đỏ / bộ đếm bậc thang.
2. **CẤM** lặp lại bố cục `[Ảnh bên trái + Hộp chữ bên phải]` ở 2 cảnh liên tiếp.
3. **CẤM** dùng vòng lặp `Math.sin` nhấp nhô tại chỗ để câu giờ.
4. **CẤM** cắt cảnh chết đà (phải tuân thủ đúng 7 vết cắt trong `ledger.json`).
5. **CẤM** để quá `3` phần tử trung tâm hiển thị cùng lúc (`max_concurrent <= 3`).
6. **CẤM** in nhãn kỹ thuật `[SC_01]`, `[STT_01]` lên màn hình `1920x1080`.
