# DANH MỤC KHƠI GỢI YÊU CẦU: [TÊN TÍNH NĂNG / PHÂN HỆ] (REQUIREMENTS CHECKLIST)
> **Mã tài liệu**: `CHK-ELICIT-001`  
> **Trạng thái**: [Draft / In Progress / Completed]  
> **Áp dụng chuẩn**: Bridging The Gap (Laura Brandenburg, CBAP)  

---

## 1. TỔNG QUAN TÍNH NĂNG & MỤC TIÊU KHƠI GỢI

| Mục | Nội Dung Đặc Tả |
| :--- | :--- |
| **Tính năng cần khám phá** | [Tên tính năng — Ví dụ: Tiếp nhận & Hỗ trợ khách hàng đa kênh] |
| **Lĩnh vực áp dụng** | [E-commerce / Fintech / Bảo hiểm / Logistics / CRM] |
| **Lợi ích kinh doanh kỳ vọng** | [Giảm chi phí vận hành, tăng mức độ giữ chân khách hàng, giảm khiếu nại] |
| **Các bên liên quan cần phỏng vấn** | [Chăm sóc khách hàng, Trưởng phòng vận hành, Kỹ sư IT, Khách hàng đại diện] |

---

## 2. MA TRẬN CÂU HỎI KHƠI GỢI THEO 5 TRỤ CỘT NGHIỆP VỤ

### Trụ Cột 1: Ranh Giới Dịch Vụ (Scope of Service)
- [ ] **1.1. Đối tượng thụ hưởng**: Chúng ta cung cấp tính năng này cho ai? (Khách hàng vãng lai, tài khoản VIP, đối tác, hay nội bộ?)
- [ ] **1.2. Loại yêu cầu được xử lý**: Những tình huống nào hệ thống bắt buộc phải giải quyết?
- [ ] **1.3. Loại yêu cầu từ chối**: Những tình huống nào hệ thống dứt khoát không tiếp nhận hoặc chuyển sang kênh khác?
- [ ] **1.4. Kênh tiếp nhận**: Yêu cầu đi vào qua kênh nào? (Web, Mobile App, Email, Hotline, Trực tiếp?)
- [ ] **1.5. Thời gian & SLA**: Giờ phục vụ là gì (Giờ hành chính hay 24/7)? Cam kết thời gian phản hồi đầu tiên (FRT) là bao lâu?

---

### Trụ Cột 2: Phân Loại & Định Tuyến (Triage & Routing)
- [ ] **2.1. Nhận diện loại yêu cầu**: Tiêu chí nào giúp phân loại yêu cầu (Form danh mục, AI/NLP, hay nhân sự phân loại thủ công)?
- [ ] **2.2. Thẩm định quyền lợi (Eligibility)**: Kiểm tra thông tin nào để xác thực người yêu cầu đủ điều kiện hỗ trợ?
- [ ] **2.3. Cơ chế định tuyến**: Chuyển yêu cầu đến Cá nhân hay Đội nhóm (Round-Robin, Hàng đợi chung, hay Phân bổ theo kỹ năng)?
- [ ] **2.4. Phương án dự phòng (Failover)**: Nếu người nhận vắng mặt hoặc quá tải, luồng chuyển giao (Escalation) diễn ra như thế nào?

---

### Trụ Cột 3: Quy Trình Xử Lý & Giải Quyết (Addressing Requests)
- [ ] **3.1. Tiêu chuẩn dứt điểm**: Khi nào một yêu cầu được coi là đã giải quyết hoàn tất thành công?
- [ ] **3.2. Luồng truyền thông**: Khách hàng được cập nhật tiến độ qua kênh nào (SMS, Email, Push Notification)?
- [ ] **3.3. Dữ liệu cần tra cứu**: Nhân viên xử lý cần những tài liệu, thông tin lịch sử nào để ra quyết định?
- [ ] **3.4. Kiểm toán & Nhật ký**: Cơ chế ghi nhận lịch sử trao đổi, thời gian xử lý và chữ ký xác nhận như thế nào?

---

### Trụ Cột 4: Giám Sát, Cảnh Báo & Đo Lường (Monitoring & SLAs)
- [ ] **4.1. Chỉ số then chốt (KPIs)**: Đo lường bằng chỉ số nào (FCR - Tỷ lệ giải quyết lần đầu, MTTR - Thời gian xử lý trung bình, CSAT)?
- [ ] **4.2. Cảnh báo vi phạm SLA**: Khi nào hệ thống gửi cảnh báo (khi đạt 75% thời hạn SLA hay khi đã vượt ngưỡng)? Ai nhận cảnh báo?

---

### Trụ Cột 5: Tự Phục Vụ & Chặn Trước Vấn Đề (Self-Service & Preemption)
- [ ] **5.1. Câu hỏi thường gặp nhất (Top 20% FAQs)**: Vấn đề gì khách hàng hay hỏi nhất? Có thể đưa lên cổng tra cứu tự động không?
- [ ] **5.2. Chặn lỗi từ đầu nguồn**: Điểm nào trong quy trình trước đó khiến người dùng hiểu nhầm? Cần sửa gì ở giao diện/hướng dẫn ban đầu để người dùng không cần phải hỏi?

---

## 3. BẢNG TỔNG HỢP KẾT QUẢ KHƠI GỢI (ELICITATION SYNTHESIS)

| Vấn Đề Khám Phá | Kết Luận Thống Nhất | Tác Động Đến Thiết Kế (Hệ Quả) |
| :--- | :--- | :--- |
| **Kênh tiếp nhận chính** | Cổng Web Portal và Ứng dụng Di động | Cần viết Use Case cho Web & Mobile |
| **Cam kết thời gian SLA** | Phản hồi trong 2 giờ làm việc | Cần cài đặt đồng hồ đếm ngược SLA trên giao diện nhân viên |
| **Tự phục vụ** | Cho phép khách hàng tự tra cứu trạng thái đơn hàng | Bổ sung màn hình Tra cứu không cần đăng nhập |
