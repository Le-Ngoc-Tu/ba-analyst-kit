# WORKFLOW 03: MÔ HÌNH HÓA QUY TRÌNH NGHIỆP VỤ (BUSINESS PROCESS MODELING)
> **Mã quy trình**: `WF-03` | **Mục tiêu**: Hướng dẫn Agent phân tích và mô hình hóa quy trình As-Is / To-Be kèm sơ đồ Mermaid Swimlane.

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng yêu cầu: "Thiết kế quy trình cho...", "Vẽ sơ đồ quy trình...", "Mô tả quy trình xử lý...".

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### Bước 1: Khóa Cặp Ranh Giới Quy Trình
1. Đặt tên quy trình theo cấu trúc: `Động từ + Danh từ` (Verb - Noun).
2. Viết câu phạm vi bắt buộc:
   > *"Quy trình này bắt đầu khi [Sự kiện bắt đầu] và kết thúc khi [Sự kiện hoàn tất]."*
3. Xác định rõ quy trình này mô tả trạng thái hiện trạng (**As-Is**) hay tương lai (**To-Be**).

### Bước 2: Phân Định Entry/Exit Criteria vs Inputs/Outputs
1. Liệt kê **Entry Criteria** (Điều kiện trạng thái cần có trước khi bắt đầu).
2. Liệt kê **Inputs** (Form, email, bản ghi số cụ thể).
3. Liệt kê **Outputs** (Sản phẩm hữu hình sinh ra).
4. Liệt kê **Exit Criteria** (Tiêu chuẩn công nhận thành công, chuyển sang quy trình kế tiếp).

### Bước 3: Dựng Sơ Đồ Mermaid Phân Làn (Swimlane Diagram)
1. Xác định các vai trò (Roles) tham gia.
2. Vẽ sơ đồ Mermaid Flowchart phân làn bằng `subgraph [Tên vai trò]`.
3. Mọi điểm rẽ nhánh hình thoi (Decision Point) bắt buộc phải có đủ 2 luồng ra: Luồng thành công (Yes) và Luồng xử lý sự cố/từ chối (No).

### Bước 4: Viết Mô Tả Chi Tiết & Bảng Quy Tắc Nghiệp Vụ
1. Đánh số các bước hoạt động (Bước 1, Bước 2...).
2. Thiết lập bảng **Business Rules Matrix**: Mã hóa `BR-01, BR-02...` và gắn trực tiếp tới số bước thực thi.
3. Liệt kê các tình huống ngoại lệ tại bảng **Exceptions Matrix** (`EX-01, EX-02...`).

### Bước 5: Bổ Sung Vai Trò & Chỉ Số Đo Lường (Metrics)
1. Lập bảng phân quyền: `Role | Responsibility | Who Fulfills`.
2. Đưa ra ít nhất 2 chỉ số đo lường hiệu quả (Cycle time, SLA compliance rate).

### Bước 6: Xuất Bản Tài Liệu
1. Áp dụng template: `templates/business_process_template.md`.
2. Lưu tệp tại: `docs/process/PROCESS_[NAME].md`.
3. Hướng dẫn người dùng chuyển tiếp sang `Workflow 04: Soạn thảo Use Case chi tiết`.
