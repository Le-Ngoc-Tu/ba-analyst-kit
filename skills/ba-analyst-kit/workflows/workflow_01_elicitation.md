# WORKFLOW 01: KHƠI GỢI YÊU CẦU & PHỎNG VẤN TƯƠNG TÁC (REQUIREMENTS ELICITATION)
> **Mã quy trình**: `WF-01` | **Mục tiêu**: Hướng dẫn Agent dẫn dắt phiên khám phá yêu cầu với người dùng.

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng nói: "Tôi muốn làm rõ yêu cầu cho dự án...", "Hãy giúp tôi phỏng vấn lấy yêu cầu...", hoặc đưa ra một ý tưởng kinh doanh mơ hồ.

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### Bước 1: Xác Định Ngữ Cảnh & Phân Loại Ban Đầu
1. Quét thông tin ban đầu từ người dùng.
2. Nếu người dùng chỉ nói 1 câu ngắn, đặt ngay **2 câu hỏi định vị**:
   - Lĩnh vực kinh doanh là gì (Fintech, E-commerce, Y tế, Quản lý nội bộ...)?
   - Tác nhân thụ hưởng chính là ai (Khách hàng bên ngoài hay Nhân viên nội bộ)?

### Bước 2: Dẫn Dắt 5 Trụ Cột Khơi Gợi
1. Áp dụng mẫu câu hỏi từ `templates/elicitation_checklist_template.md`.
2. Không hỏi dồn dập toàn bộ 40 câu hỏi. Nhóm thành **3 lượt phỏng vấn**:
   - **Lượt 1 (Phạm vi & Kênh)**: Đối tượng, loại yêu cầu phục vụ, kênh tiếp nhận, SLA.
   - **Lượt 2 (Quy trình & Định tuyến)**: Phân loại, tiêu chuẩn thẩm định, cách chuyển giao.
   - **Lượt 3 (Xử lý & Tự phục vụ)**: Cách giải quyết dứt điểm, câu hỏi thường gặp, cơ chế tự tra cứu.
3. Luôn đưa ra gợi ý trắc nghiệm a/b/c inline kèm 1 phương án mặc định khuyến nghị để người dùng duyệt nhanh.

### Bước 3: Tổng Hợp & Đóng Gói Đầu Ra
1. Xuất ra tài liệu: `docs/requirements/ELICITATION_SUMMARY_[PROJECT].md`.
2. Chốt rõ bảng:
   - Danh sách In-Scope (Cam kết xử lý).
   - Danh sách Out-of-Scope (Từ chối / Hoãn lại).
   - Các điểm nghẽn cần người dùng quyết định thêm.
3. Hướng dẫn người dùng chuyển sang `Workflow 02: Định nghĩa Scope Statement`.
