# QUY TRÌNH: GIÁM ĐỊNH TỔN THẤT TẠI HIỆN TRƯỜNG (ONSITE CLAIMS INSPECTION)
> **Mã quy trình**: `PROC-CLAIMS-01`  
> **Trạng thái**: Approved  
> **Áp dụng chuẩn**: Bridging The Gap (Laura Brandenburg, CBAP)  

---

## 1. THÔNG TIN QUY TRÌNH (DOCUMENT INFORMATION)

| Trường Thông Tin | Giá Trị Chi Tiết |
| :--- | :--- |
| **Tiêu đề quy trình (Process Title)** | Giám định tổn thất tại hiện trường (Conduct Onsite Claims Inspection) |
| **Chủ sở hữu quy trình (Process Owner)** | Lê Văn Bình — Trưởng phòng Giám định bồi thường |
| **Phiên bản (Version)** | 1.0 |
| **Trạng thái (Status)** | Approved |
| **Ngày cập nhật (Date)** | 2026-10-19 |

---

## 2. MỤC ĐÍCH & PHẠM VI (PURPOSE & SCOPE)

> "Quy trình này mô tả trạng thái tương lai (To-Be) của hoạt động giám định tổn thất tài sản và xe cơ giới tại hiện trường có ứng dụng Mobile App. Mục đích nhằm số hóa 100% hồ sơ giấy, chuẩn hóa bằng chứng video/ảnh và rút ngắn thời gian xử lý hồ sơ.  
> **Quy trình này bắt đầu khi** Giám định viên tiếp nhận lệnh điều động giám định từ hệ thống trung tâm **và kết thúc khi** Biên bản giám định điện tử cùng đầy đủ media được nộp thành công vào hệ thống CRM."

---

## 3. ĐIỀU KIỆN KÍCH HOẠT (ENTRY CRITERIA)

- [ ] Lệnh điều động giám định đã được hệ thống phê duyệt kèm tọa độ GPS địa điểm tổn thất.
- [ ] Chủ tài sản hoặc người đại diện hợp pháp đã có mặt tại hiện trường.

---

## 4. DỮ LIỆU & VẬT PHẨM ĐẦU VÀO (INPUTS)

- **Đầu vào 1**: Thông báo phân công hồ sơ điện tử gửi qua ứng dụng di động kèm Mã hồ sơ bồi thường (Claim ID).
- **Đầu vào 2**: Giấy tờ đăng ký xe, giấy phép lái xe, hoặc giấy chứng nhận quyền sở hữu nhà đất của chủ tài sản.

---

## 5. SƠ ĐỒ LUỒNG CÔNG VIỆC PHÂN LÀN (WORKFLOW SWIMLANE DIAGRAM)

```mermaid
flowchart TD
    subgraph Agent_Lane [Giám Định Viên (Claims Agent)]
        S([Bắt đầu: Nhận lệnh giám định trên App]) --> Step1[Di chuyển đến hiện trường & Xác thực danh tính chủ xe]
        Step1 --> Step2[Chụp ảnh chi tiết tổn thất & Quay video tổng quan 60s]
        Step2 --> Step3[Nhập ước tính chi phí sửa chữa sơ bộ]
        Step3 --> Step4{Hồ sơ thuộc diện tranh chấp/nghi vấn?}
    end

    subgraph Customer_Lane [Chủ Tài Sản / Chủ Nhà (Home Owner)]
        Step5 --> Step6[Xem lại biên bản trên màn hình điện thoại & Ký chữ ký số]
        Step6 --> Step7([Kết thúc: Nhận mã hồ sơ tra cứu qua tin nhắn SMS])
    end

    subgraph System_Lane [Hệ Thống Trung Tâm (CRM & Storage)]
        Step4 -->|Nghi vấn gian lận| Ex1[Chuyển luồng sang Tổ Điều Tra Gian Lận]
        Step4 -->|Hợp lệ thông thường| Step5[Hệ thống tổng hợp Biên bản giám định điện tử]
        Step6 --> Sync[Lưu trữ ảnh/video vào S3 & Cập nhật trạng thái CRM: ĐÃ GIÁM ĐỊNH]
        Sync --> Step7
    end

    classDef startEnd fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    class S,Step7 startEnd;
    class Step4 decision;
```

---

## 6. MÔ TẢ CHI TIẾT TỪNG BƯỚC HOẠT ĐỘNG (ACTIVITY DESCRIPTIONS)

### Bước 1: Tiếp cận hiện trường và xác thực chủ tài sản
- **Người thực hiện**: Giám định viên.
- **Thao tác**: Kiểm tra đối chiếu số khung, số máy hoặc giấy chứng nhận quyền sở hữu. Bật định vị GPS trên App để xác thực có mặt tại tọa độ được chỉ định.

### Bước 2: Chụp ảnh tổn thất và quay video hiện trường
- **Người thực hiện**: Giám định viên.
- **Thao tác**: Chụp tối thiểu 4 góc toàn cảnh và các ảnh cận cảnh từng điểm hư hỏng. Quay 1 video tối đa 60 giây ghi lại âm thanh và hiện trường xung quanh.
- **Quy tắc liên quan**: Tuân thủ quy tắc `BR-01`.

### Bước 3: Lập dự toán sơ bộ và xuất biên bản
- **Người thực hiện**: Giám định viên.
- **Thao tác**: Chọn danh mục phụ tùng cần thay thế hoặc sửa chữa từ kho dữ liệu bảng giá tiêu chuẩn. App tự động tính tổng chi phí ước tính.

### Bước 4: Kiểm tra gian lận và ký biên bản điện tử
- **Người thực hiện**: Giám định viên & Chủ tài sản.
- **Thao tác**: Nếu phát hiện dấu hiệu gian lận hoặc không trùng khớp hiện trường, xử lý theo Ngoại lệ `EX-01`. Nếu hợp lệ, chủ tài sản ký trực tiếp bằng tay trên màn hình cảm ứng của App.

---

## 7. CÁC TÌNH HUỐNG NGOẠI LỆ (EXCEPTIONS)

| Mã Ngoại Lệ | Điểm Phát Sinh | Mô Tả Tình Huống | Hướng Xử Lý Khắc Phục |
| :---: | :---: | :--- | :--- |
| **EX-01** | Bước 4 | Vết tích tổn thất không khớp với lời khai tai nạn | Đóng băng hồ sơ, gắn cờ nghi vấn (Fraud Flag) và chuyển cho Tổ Điều tra đặc biệt |
| **EX-02** | Bước 2 | Mất sóng di động tại hiện trường (khu vực hẻo lánh) | App tự động lưu video/ảnh vào bộ nhớ mã hóa cục bộ trên máy và tự động đồng bộ khi có sóng trở lại |

---

## 8. BẢNG QUY TẮC NGHIỆP VỤ (BUSINESS RULES MATRIX)

| Mã Quy Tắc | Nội Dung Quy Tắc Nghiệp Vụ | Bước Áp Dụng |
| :---: | :--- | :---: |
| **BR-01** | Mọi ảnh chụp hiện trường bắt buộc phải có Watermark tự động nhúng Tọa độ GPS và Dấu thời gian (Timestamp) | Bước 2 |
| **BR-02** | Nếu chi phí ước tính vượt quá 50,000,000 VNĐ, bắt buộc phải có sự tham gia của Giám định viên cấp Senior | Bước 3 |
| **BR-03** | Biên bản giám định điện tử bắt buộc phải có đủ chữ ký của cả Giám định viên và Chủ tài sản | Bước 4 |

---

## 9. SẢN PHẨM ĐẦU RA (OUTPUTS)

- **Đầu ra 1**: Biên bản giám định điện tử định dạng PDF có mã băm bảo mật SHA-256 kèm chữ ký số hai bên.
- **Đầu ra 2**: Bộ tệp hình ảnh và video gốc được lưu trữ trên Cloud Storage.

---

## 10. TIÊU CHUẨN KẾT THÚC (EXIT CRITERIA)

- [ ] Hồ sơ bồi thường trên CRM chuyển sang trạng thái: `ĐÃ GIÁM ĐỊNH HIỆN TRƯỜNG`.
- [ ] Chủ tài sản nhận được tin nhắn SMS xác nhận kèm link tra cứu tiến độ bồi thường.

---

## 11. PHÂN QUYỀN VAI TRÒ & CHỈ SỐ HIỆU SUẤT (ROLES & METRICS)

### Bảng Phân Quyền
| Vai Trò | Trách Nhiệm | Ai Đảm Nhận |
| :--- | :--- | :--- |
| **Claims Agent** | Khảo sát thực địa, quay chụp, lập biên bản | Giám định viên cơ động |
| **Home Owner** | Cung cấp giấy tờ, xác nhận tổn thất, ký biên bản | Khách hàng mua bảo hiểm |
| **Fraud Specialist** | Thẩm định các trường hợp nghi vấn gian lận | Chuyên viên Ban Kiểm soát nội bộ |

### Chỉ Số Đo Lường Hiệu Quả (Metrics)
1. **Thời gian lập và nộp hồ sơ tại hiện trường**: Giảm từ 8 giờ xuống $\le$ 6 giờ làm việc.
2. **Tỷ lệ hồ sơ đầy đủ bằng chứng media hợp lệ ngay lần đầu**: Đạt $\ge 98\%$.
