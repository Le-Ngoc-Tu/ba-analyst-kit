# WORKFLOW 06: TUÂN THỦ PHÁP LÝ VIỆT NAM & NGHIỆM THU BÀN GIAO UAT (VIETNAM COMPLIANCE & UAT SIGN-OFF)
> **Mã quy trình**: `WF-06` | **Mục tiêu**: Hướng dẫn Agent thẩm định tuân thủ pháp lý Việt Nam và lập hồ sơ nghiệm thu UAT chuẩn thể thức.

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng yêu cầu: "Kiểm tra tuân thủ pháp lý Việt Nam...", "Rà soát Nghị định 13...", "Xác thực sinh trắc học Quyết định 2345...", "Lập biên bản nghiệm thu UAT...", hoặc "Chuẩn bị hồ sơ bàn giao ký duyệt...".

---

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### GIAI ĐOẠN 1: THẨM ĐỊNH TUÂN THỦ PHÁP LÝ (COMPLIANCE CHECK)

#### Bước 1: Kiểm Tra Nghị Định 13/2023/NĐ-CP (Bảo Vệ Dữ Liệu Cá Nhân)
1. Quét danh mục dữ liệu thu thập trong Scope Statement và Use Cases:
   - Dữ liệu cá nhân cơ bản: Họ tên, ngày sinh, số CCCD, số điện thoại, địa chỉ email.
   - Dữ liệu cá nhân nhạy cảm: Dữ liệu sinh trắc học (khuôn mặt, vân tay), vị trí địa lý GPS, dữ liệu tài chính/tài khoản ngân hàng.
2. Kiểm tra các bất biến thiết kế bắt buộc:
   - [ ] Có màn hình thu thập **Sự đồng ý tường minh (Explicit Consent)** trước khi người dùng đăng ký.
   - [ ] Checkbox đồng ý **không được tick sẵn** (bắt buộc người dùng chủ động chọn).
   - [ ] Có tính năng cho phép người dùng **rút lại sự đồng ý** hoặc **yêu cầu xóa vĩnh viễn dữ liệu** (Account Deletion).
   - [ ] Có kế hoạch mã hóa AES-256 dữ liệu nhạy cảm tại tầng lưu trữ.

#### Bước 2: Kiểm Tra Quyết Định 2345/QĐ-NHNN (Nếu Là Ứng Dụng Thanh Toán / Ví / Ngân Hàng)
1. Kiểm tra luồng chuyển tiền / thanh toán trong Use Cases:
   - [ ] Nếu số tiền chuyển $\ge 10,000,000$ VNĐ/lần hoặc tổng giao dịch ngày vượt $20,000,000$ VNĐ: Bắt buộc kích hoạt **Xác thực sinh trắc học khuôn mặt** đối soát với dữ liệu lưu trong chip CCCD.
   - [ ] Bổ sung các kịch bản ngoại lệ: Không có thiết bị NFC, camera không nhận diện được, hoặc khuôn mặt không khớp.

#### Bước 3: Kiểm Tra Luật Giao Dịch Điện Tử 2023 & Hóa Đơn Điện Tử
1. Kiểm tra luồng ký hợp đồng hoặc xác nhận giao dịch:
   - [ ] Áp dụng chữ ký số hoặc chữ ký điện tử an toàn (Remote Signing qua SmartCA).
   - [ ] Tích hợp API xuất hóa đơn điện tử tự động chuẩn XML theo Nghị định 123/2020 và Thông tư 78/2021.

---

### GIAI ĐOẠN 2: THỰC HIỆN NGHIỆM THU CHẤP NHẬN NGƯỜI DÙNG (UAT SIGN-OFF)

#### Bước 4: Lập Kế Hoạch UAT & Ma Trận Kịch Bản Nghiệm Thu
1. Trích xuất toàn bộ các tiêu chí nghiệm thu (Gherkin Scenarios) từ các Use Cases đã duyệt.
2. Thiết lập bảng **UAT Matrix**: Mã kịch bản, Phân hệ, Kết quả mong đợi, Trạng thái (Pass/Fail).

#### Bước 5: Phân Loại Lỗi Tồn Đọng (Defect Triage)
1. Gom lỗi theo 3 mức độ chuẩn:
   - **Critical (Chặn)**: Hệ thống sập, tính sai tiền, lộ dữ liệu $\to$ Phải sửa ngay.
   - **Major (Lớn)**: Chức năng chính bị lỗi, có cách giải quyết tạm thời $\to$ Sửa trước Go-live.
   - **Minor (Nhỏ)**: Lỗi chính tả, lệch màu giao diện $\to$ Chuyển sang Backlog, **cấm dùng làm lý do từ chối ký biên bản UAT**.

#### Bước 6: Xuất Bản Biên Bản Nghiệm Thu Chuẩn Nghị Định 30/2020/NĐ-CP
1. Áp dụng template: `templates/vietnam_uat_signoff_template.md`.
2. Kiểm tra đủ các yếu tố thể thức: Quốc hiệu, Tiêu ngữ, Căn cứ hợp đồng, Thành phần đại diện 2 bên, Kết luận nghiệm thu và Chữ ký đại diện.
3. Sử dụng công cụ `python scripts/export_ba_docx.py` để xuất sang định dạng Microsoft Word (`.docx`) sẵn sàng in ký hoặc gửi trình ký điện tử.
