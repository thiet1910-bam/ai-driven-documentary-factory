# ✍️ QUY CHUẨN TYPOGRAPHY & HIỆU ỨNG CHỮ ĐỘNG (KINETIC TYPOGRAPHY & TEXT FX)

> [!IMPORTANT]
> Cả hai video mẫu (`gP4ihbNXFrY` và `uIHJvUVaB34`) đều chứng minh rằng **Chữ trên màn hình không phải là phụ đề lặp lại lời thoại**, mà là **Vũ khí nhấn trọng tâm (Editorial Visual Anchors)**.

---

## 1. BỘ 4 PHÔNG CHỮ CHUẨN TRONG KHO GU EDIT

| Vai trò | Tên Phông Chữ Chuẩn (Google Fonts / Windows) | Đặc điểm nhận diện | Dùng ở đâu? |
| :--- | :--- | :--- | :--- |
| **1. Serif Nghiêng Kể Chuyện (`Editorial Serif Italic`)** | `Instrument Serif Italic`, `Playfair Display Italic`, `Georgia Italic` | Thanh lịch, giàu tính báo chí/văn học, nét thanh nét đậm rõ rệt. | Cụm từ mở đầu câu trên tiêu đề Vox (`"And it's..."`, `"The real problem is"`, `"the government's"`). |
| **2. Sans-Serif Đậm Nén (`Heavy Condensed Impact`)** | `Bebas Neue`, `Oswald Bold`, `Anton`, `Impact` | Cao, khỏe, nén chặt theo chiều ngang, đập ngay vào mắt trong 0.2 giây. | Từ khóa chính được tô bút dạ vàng/xanh, con số thống kê lớn (`$500+ BILLION`, `THE INTEREST`, `420+ PPM`), con dấu (`NEUTRAL`). |
| **3. Monospace Máy Đánh Chữ (`Archival Typewriter`)** | `Courier Prime Bold`, `IBM Plex Mono`, `Consolas` | Đậm chất hồ sơ lưu trữ, báo cáo tài chính và chú thích bản đồ. | Chú thích dưới ảnh Polaroid, dòng tiêu đề phụ, bảng kê ngân sách (`U.S. FEDERAL BUDGET`), và dòng nguồn (`Source:...`) ở đáy. |
| **4. Chữ Viết Tay Ghi Chú (`Handwritten Callout`)** | `Caveat Bold`, `Kalam`, `Segoe Print` | Tự nhiên như người kể chuyện vừa viết tay trực tiếp lên bản đồ. | Ghi chú đi kèm mũi tên cong chỉ vào nhân vật trên bản đồ Gu 1 (`eating grass`, `paid by two different kings`). |

---

## 2. 7 HIỆU ỨNG CHỮ ĐỘNG ĐẶC TRƯNG (7 SIGNATURE TEXT FX)

### 2.1. `MIXED_SERIF_SANS_HIGHLIGHT` (Cặp Chữ Hỗn Hợp + Bút Dạ Quét Ngang)
- **Mẫu chuẩn từ Gu 2**:
  - Cùng một dòng hoặc hai dòng sát nhau:
    - Chữ `And it's` viết bằng *Serif Italic* màu đen `#141414`.
    - Chữ `speeding up.` viết nghiêng đậm đặt trên vệt bút dạ vàng `#F5C518` quét từ trái sang phải (`scaleX: 0 -> 1`).
- **Tác dụng**: Tạo nhịp điệu thị giác như mắt người đang đọc báo và cầm bút dạ gạch chân từ quan trọng nhất.

### 2.2. `RED_STRIKETHROUGH_REPLACE` (Gạch Bỏ Từ Cũ $\rightarrow$ Đập Từ Mới)
- **Mẫu chuẩn từ Gu 2**:
  - Dòng 1: `We're not paying for the` (*Serif Italic* trắng).
  - Dòng 2: `FUTURE` (*Condensed Sans* xám tối `#666666`, cỡ `76px`) bị **một vệt sơn đỏ gạch ngang chính giữa (`Strikethrough`)** đúng lúc giọng đọc nhấn chữ *"not"*.
  - Dòng 3 & 4: `We're paying for the` $\rightarrow$ **`PAST`** (chữ đen đậm nằm trong khối hộp vàng `#F5C518` bật sáng rực rỡ).

### 2.3. `LIVE_ODOMETER_NUMBER_TICKER` (Bộ Đếm Số Nhảy Liên Tục Kèm Đơn Vị)
- **Mẫu chuẩn từ Gu 1 & Gu 2**:
  - Không bao giờ hiện ngay con số tĩnh (`$40 TRILLION` hay `1,450,042`).
  - Luôn chạy hàm nội suy bậc 3 (`easeOutCubic: 1 - (1 - p)^3`) trong `0.75s – 1.1s` để các chữ số cuộn nhanh từ `0` (hoặc số khởi điểm) lên con số mục tiêu, hoặc nhảy từng giây một (`$53,973` $\rightarrow$ `$2,367,125`).

### 2.4. `YEAR_BADGE_WITH_MICRO_STAMP` (Thẻ Năm Kèm Dấu Đỏ Nhỏ Nghiêng)
- **Mẫu chuẩn từ Gu 2**:
  - Khi nói về mốc dự báo tương lai (`By 2048...`), hiển thị hộp chữ nhật nền đen chữ trắng `2048`, ngay góc dưới bên phải của hộp `2048` có đóng đè một con dấu đỏ nhỏ nằm nghiêng `-12deg` mang chữ `PROJECTED`.

### 2.5. `NO_LIST_REJECTION_CARDS` (Thẻ Liệt Kê Phủ Định Chữ "NO" Đỏ)
- **Mẫu chuẩn từ Gu 1**:
  - Khi giải thích một vùng đất thiếu thốn tài nguyên (`NO big rivers to the sea`, `NO wide plains for huge farms`), từng thẻ giấy kem bật ra bên trái bản đồ: bên trái thẻ là chữ **`NO`** màu đỏ đậm cỡ lớn, bên phải là cụm từ giải thích bằng chữ viết tay cùng hình minh họa mờ.

### 2.6. `HANDWRITTEN_CURVED_POINTER` (Chữ Viết Tay + Mũi Tên Vẽ Tay Chỉ Điểm)
- **Mẫu chuẩn từ Gu 1**:
  - Dùng khi trên màn hình có nhiều nhân vật hoặc vùng lãnh thổ: dòng chữ ngắn (`2–4 từ`) hiện ra kèm mũi tên cong màu trắng hoặc đỏ chỉ thẳng vào đối tượng đang được nhắc tới.

### 2.7. `CINEMATIC_DUAL_SUBTITLE_BAR` (Thanh Phụ Đề Song Ngữ Chuẩn Điện Ảnh)
- **Quy chuẩn cố định theo yêu cầu người dùng**:
  - Đặt tại trung tâm cạnh dưới (`bottom: 36px`), hộp bo tròn `radius: 10px`, nền đen mờ `rgba(12, 14, 18, 0.91)`, viền vàng mảnh `#F5C518`.
  - Dòng trên: Tiếng Anh (`White #FFFFFF`, Bold `25px`).
  - Dòng dưới: Tiếng Việt (`Gold #F5C518`, SemiBold `20px`).
