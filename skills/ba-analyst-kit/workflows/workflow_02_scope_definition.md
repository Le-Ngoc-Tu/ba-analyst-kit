# WORKFLOW 02: ĐỊNH NGHĨA PHẠM VI DỰ ÁN & MỤC TIÊU KINH DOANH (SCOPE DEFINITION)
> **Mã quy trình**: `WF-02` | **Mục tiêu**: Hướng dẫn Agent tạo lập tài liệu Scope Statement chuẩn hóa.

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng yêu cầu: "Hãy viết Scope Statement cho dự án...", "Xác định phạm vi dự án...", hoặc "Lập ranh giới hệ thống...".

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### Bước 1: Nạp Dữ Liệu Đầu Vào
1. Đọc tệp tóm tắt khơi gợi từ `Workflow 01` (nếu có) hoặc yêu cầu người dùng cung cấp:
   - Tên dự án & Business Sponsor.
   - Vấn đề cốt lõi cần giải quyết (Business Driver).

### Bước 2: Thiết Lập Mục Tiêu Kinh Doanh Đo Lường Được (Expected Benefits)
1. Viết từ 2 đến 4 mục tiêu kinh doanh (Outcomes).
2. **Quy tắc kiểm tra**: Mỗi mục tiêu phải gắn với con số đo lường (%, giờ làm việc, chi phí, tỷ lệ giảm cuộc gọi khiếu nại). Tuyệt đối cấm viết mục tiêu chung chung như "Làm app hiện đại".

### Bước 3: Phân Rã Năng Lực Giải Pháp (Capabilities Subgroups)
1. Tạo bảng năng lực theo các nhóm `Subgroup A`, `Subgroup B`...
2. Gán mã định danh duy nhất: `A1, A2... B1, B2...`.
3. Câu mô tả chuẩn: `"[Chủ thể] có thể [Hành động] [Đối tượng] để [Mục đích]"`.

### Bước 4: Thiết Lập Ranh Giới Bất Biến (In-Scope vs Out-of-Scope)
1. Đưa các tính năng cam kết vào In-Scope.
2. Liệt kê tối thiểu 2 - 3 mục vào Out-of-Scope kèm lý do từ chối (bảo vệ ngân sách và thời hạn).

### Bước 5: Dựng Sơ Đồ Ngữ Cảnh Mermaid (System Context Diagram)
1. Vẽ sơ đồ ngữ cảnh 1 trang phân định rõ:
   - Các nhóm người dùng (External Users).
   - Ranh giới hệ thống đang xây dựng (System Boundary).
   - Các hệ thống ngoại vi kết nối (External Systems / APIs).

### Bước 6: Xuất Bản Tài Liệu & Kiểm Tra
1. Sử dụng template: `templates/scope_statement_template.md`.
2. Lưu tệp tại: `docs/scope/SCOPE_STATEMENT_[PROJECT].md`.
3. Hướng dẫn người dùng chuyển tiếp sang `Workflow 03: Thiết kế Quy trình nghiệp vụ`.
