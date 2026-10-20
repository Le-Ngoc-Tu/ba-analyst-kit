# CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
**Độc lập – Tự do – Hạnh phúc**
***
*Hà Nội, ngày [DD] tháng [MM] năm 2026*

# BIÊN BẢN NGHIỆM THU CHẤP NHẬN NGƯỜI DÙNG (UAT SIGN-OFF)
> **Số văn bản**: `.../BBNT-UAT/[TÊN DỰ ÁN]`  
> **Căn cứ**: Hợp đồng dịch vụ phần mềm số: `[Số Hợp Đồng]` ký ngày `[Ngày Ký]`  
> **Áp dụng chuẩn**: Thể thức văn bản hành chính Việt Nam (Nghị định 30/2020/NĐ-CP)  

---

## I. THÀNH PHẦN THAM GIA NGHIỆM THU

### 1. ĐẠI DIỆN BÊN A (BÊN SỬ DỤNG / CHỦ ĐẦU TƯ): [TÊN DOANH NGHIỆP A]
- Ông/Bà: **[Họ và tên]** — Chức vụ: **[Giám đốc Vận hành / Trưởng phòng Nghiệp vụ]** (Trưởng đoàn).
- Ông/Bà: **[Họ và tên]** — Chức vụ: **[Chuyên viên phụ trách UAT]**.

### 2. ĐẠI DIỆN BÊN B (ĐƠN VỊ PHÁT TRIỂN / NHÀ THẦU): [TÊN DOANH NGHIỆP B]
- Ông/Bà: **[Họ và tên]** — Chức vụ: **[Project Manager / Quản trị dự án]** (Trưởng đoàn).
- Ông/Bà: **[Họ và tên]** — Chức vụ: **[Senior Business Analyst]**.
- Ông/Bà: **[Họ và tên]** — Chức vụ: **[QA Lead / Trưởng nhóm kiểm thử]**.

---

## II. THỜI GIAN VÀ ĐỊA ĐIỂM
- **Thời gian**: Bắt đầu từ ngày [DD/MM/YYYY] đến ngày [DD/MM/YYYY].
- **Môi trường thử nghiệm**: Môi trường Staging/UAT tại địa chỉ `[URL hệ thống UAT]`.

---

## III. NỘI DUNG VÀ KẾT QUẢ KIỂM THỬ NGHIỆM THU (UAT MATRIX)

Hai bên đã cùng nhau thực hiện kiểm thử chấp nhận toàn bộ các tính năng theo đúng Phạm vi đã thống nhất trong **Tuyên bố phạm vi (Scope Statement)**. Kết quả đo đạc như sau:

| STT | Phân Hệ / Chức Năng | Tổng Số Kịch Bản | Đạt (Pass) | Không Đạt (Fail) | Tỷ Lệ Đạt (%) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | [Phân hệ 1: Tiếp nhận yêu cầu & Định danh] | 25 | 25 | 0 | 100% |
| 2 | [Phân hệ 2: Giám định tổn thất & Tải media] | 30 | 29 | 1 | 96.7% |
| 3 | [Phân hệ 3: Tra cứu tiến độ & Tự phục vụ] | 20 | 20 | 0 | 100% |
| 4 | [Phân hệ 4: Tích hợp API & Báo cáo quản trị] | 15 | 15 | 0 | 100% |
| **TỔNG** | **Toàn bộ hệ thống** | **90** | **89** | **1** | **98.9%** |

---

## IV. PHÂN LOẠI TỒN ĐỌNG & KẾ HOẠCH KHẮC PHỤC (DEFECT TRIAGE)

| Mã Lỗi | Mô Tả Hiện Tượng | Mức Độ | Trách Nhiệm | Thời Hạn Xử Lý |
| :---: | :--- | :---: | :--- | :---: |
| **DEF-01** | Tốc độ tải video trên mạng 3G yếu bị chậm hơn 3 giây so với cam kết | Minor | Bên B tối ưu nén ảnh | Trong bản cập nhật v1.1 |

*Ghi chú*: Toàn bộ 01 lỗi tồn đọng thuộc nhóm **Minor (Lỗi nhỏ/Thẩm mỹ)**, không gây gián đoạn quy trình nghiệp vụ cốt lõi, không làm sai lệch số liệu tài chính và không vi phạm an toàn thông tin.

---

## V. KẾT LUẬN VÀ CAM KẾT CỦA HAI BÊN

1. **Ý kiến của Bên A (Chủ đầu tư)**:
   - Hệ thống phần mềm hoạt động ổn định, đáp ứng đầy đủ các yêu cầu nghiệp vụ cốt lõi và tuân thủ các quy định về bảo vệ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP.
   - **Bên A CHÍNH THỨC ĐỒNG Ý NGHIỆM THU GIAI ĐOẠN UAT** và cho phép đưa hệ thống vào vận hành thử nghiệm chính thức (Go-Live).

2. **Cam kết của Bên B (Đơn vị phát triển)**:
   - Cam kết khắc phục dứt điểm lỗi tồn đọng `DEF-01` trong vòng 07 ngày làm việc kể từ ngày ký biên bản.
   - Bắt đầu thực hiện chế độ bảo hành và hỗ trợ kỹ thuật vận hành 24/7 theo đúng điều khoản hợp đồng.

Biên bản này được lập thành 04 (bốn) bản có giá trị pháp lý như nhau, Bên A giữ 02 bản, Bên B giữ 02 bản để làm căn cứ thực hiện các thủ tục thanh quyết toán tiếp theo.

---

## VI. ĐẠI DIỆN CÁC BÊN KÝ TÊN VÀ ĐÓNG DẤU

| ĐẠI DIỆN BÊN A (CHỦ ĐẦU TƯ)<br>*(Ký, ghi rõ họ tên và đóng dấu)* | ĐẠI DIỆN BÊN B (ĐƠN VỊ PHÁT TRIỂN)<br>*(Ký, ghi rõ họ tên và đóng dấu)* |
| :---: | :---: |
| <br><br><br><br>**[Họ và tên Người đại diện Bên A]** | <br><br><br><br>**[Họ và tên Người đại diện Bên B]** |
