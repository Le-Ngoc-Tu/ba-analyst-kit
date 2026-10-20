# DANH MỤC KHƠI GỢI YÊU CẦU: HỖ TRỢ & TRA CỨU TIẾN ĐỘ BỒI THƯỜNG (REQUIREMENTS CHECKLIST)
> **Mã tài liệu**: `CHK-CLAIMS-01`  
> **Trạng thái**: Completed  
> **Áp dụng chuẩn**: Bridging The Gap (Laura Brandenburg, CBAP)  

---

## 1. TỔNG QUAN TÍNH NĂNG & MỤC TIÊU KHƠI GỢI

| Mục | Nội Dung Đặc Tả |
| :--- | :--- |
| **Tính năng cần khám phá** | Cổng tự phục vụ tra cứu tiến độ bồi thường & Hỗ trợ khách hàng đa kênh |
| **Lĩnh vực áp dụng** | Bảo hiểm tài sản, nhà cửa và xe cơ giới (Property & Casualty Insurance) |
| **Lợi ích kinh doanh kỳ vọng** | Giảm 50% cuộc gọi thắc mắc của chủ nhà và nhà thầu; tăng độ hài lòng khách hàng |
| **Các bên liên quan đã tham vấn** | Trưởng phòng Giám định bồi thường, Đội ngũ CSKH tổng đài, Đại diện Hội chủ nhà, Đối tác gara liên kết |

---

## 2. KẾT QUẢ KHƠI GỢI THEO 5 TRỤ CỘT NGHIỆP VỤ

### Trụ Cột 1: Ranh Giới Dịch Vụ (Scope of Service)
- [x] **1.1. Đối tượng phục vụ**: Chủ sở hữu hợp đồng bảo hiểm đã có hồ sơ bồi thường phát sinh và các nhà thầu/gara được ủy quyền sửa chữa.
- [x] **1.2. Yêu cầu được xử lý**: Tra cứu trạng thái hồ sơ theo thời gian thực (Đang giám định, Đang thẩm định, Đã duyệt chi trả, Đã thanh toán); Tải lên hóa đơn bổ trợ; Gửi thắc mắc trực tuyến.
- [x] **1.3. Yêu cầu từ chối**: Khiếu nại đòi thay đổi điều khoản hợp đồng gốc (chuyển sang Bộ phận Pháp chế); Yêu cầu tạm ứng tiền mặt tại chỗ.
- [x] **1.4. Kênh tiếp nhận**: Cổng web tự phục vụ (Self-service Web), Ứng dụng di động, và Zalo Mini App.
- [x] **1.5. Thời gian & SLA**: Cổng tra cứu hoạt động 24/7/365. Thời gian giải đáp thắc mắc gửi qua cổng trực tuyến là tối đa 2 giờ làm việc.

---

### Trụ Cột 2: Phân Loại & Định Tuyến (Triage & Routing)
- [x] **2.1. Nhận diện loại yêu cầu**: Hệ thống nhận diện tự động qua Mã hồ sơ bồi thường (Claim ID). Yêu cầu bổ sung chứng từ được gắn nhãn tự động là `DOC_SUPPLEMENT`.
- [x] **2.2. Thẩm định quyền lợi (Eligibility)**: Kiểm tra trạng thái hiệu lực của hợp đồng bảo hiểm và số điện thoại nhận mã OTP xác thực.
- [x] **2.3. Cơ chế định tuyến**: Định tuyến trực tiếp về Giám định viên đang thụ lý chính hồ sơ đó. Nếu là thắc mắc chung về chính sách thì định tuyến vào Hàng đợi chung (Queue) của phòng CSKH.
- [x] **2.4. Phương án dự phòng (Failover)**: Nếu Giám định viên không phản hồi câu hỏi sau 4 giờ làm việc, hệ thống tự động chuyển tiếp cảnh báo (Escalate) cho Trưởng nhóm giám định khu vực.

---

### Trụ Cột 3: Quy Trình Xử Lý & Giải Quyết (Addressing Requests)
- [x] **3.1. Tiêu chuẩn dứt điểm**: Yêu cầu tra cứu được xem là hoàn tất khi khách hàng xem được trạng thái mới nhất; Yêu cầu nộp chứng từ hoàn tất khi chứng từ được phê duyệt hoặc yêu cầu chụp lại có lý do cụ thể.
- [x] **3.2. Luồng truyền thông**: Tự động gửi tin nhắn SMS và thông báo qua App mỗi khi hồ sơ chuyển bước (Ví dụ: "Hồ sơ của bạn đã được duyệt chi trả số tiền X triệu đồng").
- [x] **3.3. Dữ liệu cần tra cứu**: Giám định viên xem được toàn bộ lịch sử trao đổi, thời gian khách hàng tải hóa đơn và biên bản hiện trường gốc.
- [x] **3.4. Kiểm toán (Audit Trail)**: Mọi thao tác tải tệp, duyệt hoặc từ chối chứng từ đều được ghi log bất biến với Timestamp và IP/User ID.

---

### Trụ Cột 4: Giám Sát, Cảnh Báo & Đo Lường (Monitoring & SLAs)
- [x] **4.1. Chỉ số đo lường then chốt (KPIs)**:
  - Tỷ lệ khách hàng tự tra cứu thành công không cần gọi tổng đài: $\ge 70\%$.
  - Thời gian phản hồi thắc mắc trực tuyến (MTTR): Dưới 1.5 giờ.
  - Điểm đánh giá trải nghiệm bồi thường (CSAT): $\ge 4.5/5.0$ sao.
- [x] **4.2. Cảnh báo vi phạm SLA**: Cảnh báo màu vàng cho Giám định viên sau 2 giờ chưa duyệt chứng từ mới nộp; cảnh báo đỏ gửi cho Trưởng phòng sau 6 giờ.

---

### Trụ Cột 5: Tự Phục Vụ & Chặn Trước Vấn Đề (Self-Service & Preemption)
- [x] **5.1. Câu hỏi thường gặp nhất (Top FAQs)**:
  - "Hồ sơ của tôi đang ở bước nào và khi nào thì nhận được tiền?" $\to$ Giải quyết bằng thanh tiến trình trực quan 5 bước trên màn hình chính của Cổng thông tin.
  - "Hóa đơn sửa chữa cần ghi thông tin gì để hợp lệ?" $\to$ Giải quyết bằng cách hiển thị mẫu hóa đơn VAT hợp lệ kèm ghi chú hướng dẫn ngay tại khung upload.
- [x] **5.2. Chặn lỗi từ đầu nguồn**: Nhắn tin hướng dẫn chủ nhà chuẩn bị sẵn giấy đăng kiểm xe ngay khi tai nạn được ghi nhận, giúp tiết kiệm 30 phút chờ đợi tại hiện trường.

---

## 3. BẢNG TỔNG HỢP KẾT QUẢ & CHUYỂN GIAO THIẾT KẾ

| Kết Luận Khơi Gợi | Tác Động Trực Tiếp Đến Hồ Sơ Phân Tích |
| :--- | :--- |
| Cần hỗ trợ tra cứu không cần tạo tài khoản mật khẩu phức tạp | Thiết kế cơ chế xác thực đăng nhập một chạm qua Claim ID + OTP |
| Khách hàng hay gửi ảnh hóa đơn mờ hoặc mất góc | Thêm tính năng tự động nhận diện góc và kiểm tra độ nét ảnh trên App |
| Nhà thầu cần tài khoản phân quyền riêng biệt với chủ nhà | Tách phân quyền Role `Contractor` trong Scope Statement và Bảng phân quyền |
