# WORKFLOW 04: SOẠN THẢO USE CASE CHI TIẾT & USER STORIES (USE CASE & USER STORIES)
> **Mã quy trình**: `WF-04` | **Mục tiêu**: Hướng dẫn Agent soạn thảo đặc tả Use Case tương tác chi tiết kết hợp Agile Gherkin AC.

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng yêu cầu: "Viết Use Case cho chức năng...", "Đặc tả chức năng...", "Viết User Story và tiêu chí nghiệm thu...".

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### Bước 1: Khởi Tạo Định Danh & Tra Cứu Thư Viện Use Case Kinh Điển
1. **Tra cứu mẫu có sẵn**: Trước khi viết mới, kiểm tra xem yêu cầu có thuộc **Top 10 Use Case phổ biến** trong [common_use_cases_library.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/common_use_cases_library.md) hay không:
   - *Đăng nhập 2FA / Sinh trắc học (UC-AUTH-01)*
   - *Định danh điện tử eKYC CCCD chip (UC-AUTH-02)*
   - *Thanh toán VietQR Napas (UC-PAY-01)*
   - *Tìm kiếm, Lọc đa chiều & Phân trang (UC-SEARCH-01)*
   - *Tải lên tệp & chứng từ an toàn (UC-FILE-01)*
   - *Quy trình phê duyệt đa tầng (UC-WF-01)*
   - *Bắn thông báo đa kênh (UC-NOTIF-01)*
   - *Xuất dữ liệu Excel (UC-DATA-01)*
   - *Nhập dữ liệu hàng loạt Excel (UC-IMPORT-01)*
   - *Nhật ký kiểm toán Audit Trail (UC-AUDIT-01)*
   $\to$ Kế thừa trực tiếp cấu trúc luồng lỗi, quy tắc nghiệp vụ và tiêu chuẩn Gherkin có sẵn.
2. Đặt tên Use Case: `Động từ + Danh từ` (Ví dụ: *Tải lên chứng từ bồi thường*).
3. Viết câu phạm vi: *"Quá trình bắt đầu khi... và kết thúc khi..."*.
4. Phân định rõ:
   - **Primary Actor**: Tác nhân chính trực tiếp thao tác.
   - **Secondary Actor**: Nhân sự hỗ trợ / tiếp nhận phía sau.
   - **System Actor**: Các hệ thống bên ngoài tham gia xử lý (S3, Payment...).

### Bước 2: Thiết Lập Pre-Conditions & Post-Conditions
1. **Pre-Conditions**: Điều kiện trạng thái trước khi mở màn hình (Đã đăng nhập, quyền hạn, trạng thái hồ sơ).
2. **Post-Conditions**: Trạng thái hệ thống sau khi hoàn thành (Bản ghi được tạo, trạng thái cập nhật, notification gửi đi).

### Bước 3: Soạn Thảo Luồng Chuẩn (Basic Flow / Happy Path)
1. Liệt kê tuần tự từng bước tương tác giữa User và System, đánh số từ 1 đến hết.
2. Mỗi bước bắt đầu bằng chủ thể rõ ràng: `"[Actor]: [Hành động]..."`.
3. Tránh mô tả kỹ thuật cài đặt bên trong (như SELECT SQL hay tên biến).

### Bước 4: Soạn Thảo Các Luồng Rẽ Nhánh & Ngoại Lệ
1. **Alternate Flows (Luồng thay thế)**: Đánh số theo bước rẽ nhánh (`3a, 3b...`). Mô tả hành động rẽ nhánh và **chỉ rõ bước quay trở lại luồng chuẩn**.
2. **Exception Flows (Luồng lỗi)**: Mô tả nguyên nhân lỗi, thông báo lỗi bằng tiếng Việt hiển thị cho người dùng, và hành động dọn dẹp trạng thái.

### Bước 5: Cầu Nối Agile — User Story & Tiêu Chuẩn Nghiệm Thu Gherkin
1. Viết 1 - 2 User Stories:
   ```text
   Là một (As a): [Actor]
   Tôi muốn (I want): [Thực hiện thao tác]
   Để (So that): [Đạt lợi ích]
   ```
2. Viết tối thiểu 2 kịch bản nghiệm thu định dạng Gherkin (`Given... When... Then...`):
   - Kịch bản 1: Thành công (Happy Path).
   - Kịch bản 2: Xử lý ngoại lệ hoặc dữ liệu đầu vào sai (Exception Flow).

### Bước 6: Dựng Sơ Đồ Tuần Tự Tương Tác Mermaid (Sequence Diagram)
1. Vẽ sơ đồ tương tác giữa `Actor -> UI -> Server -> DB/External`.
2. Sử dụng khối `alt / else` để thể hiện luồng thành công và luồng rẽ nhánh lỗi.

### Bước 7: Xuất Bản Tài Liệu
1. Áp dụng template: `templates/use_case_template.md`.
2. Lưu tệp tại: `docs/use_cases/UC_[CODE]_[NAME].md`.
