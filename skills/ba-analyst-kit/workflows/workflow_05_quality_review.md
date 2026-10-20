# WORKFLOW 05: KIỂM TOÁN CHẤT LƯỢNG TÀI LIỆU & ĐÁNH GIÁ NĂNG LỰC BA (QUALITY REVIEW & SKILLS ASSESSMENT)
> **Mã quy trình**: `WF-05` | **Mục tiêu**: Hướng dẫn Agent kiểm toán chất lượng tài liệu BA và đánh giá khoảng cách kỹ năng (Skills Gap).

---

## 1. ĐIỀU KIỆN KÍCH HOẠT (TRIGGER)
- Người dùng yêu cầu: "Hãy review tài liệu này...", "Kiểm tra chất lượng tài liệu BA...", "Đánh giá khoảng cách kỹ năng...", "Thẩm định tính đầy đủ của Scope/Process/Use Case...".

## 2. TRÌNH TỰ THỰC THI TỪNG BƯỚC CỦA AGENT

### Nhánh A: Kiểm Toán Chất Lượng Tài Liệu Nghiệp Vụ (Deliverables Quality Audit)

#### Bước A1: Quét Các Lỗi Phổ Biến (Anti-Patterns Check)
1. **Kiểm tra Scope Statement**:
   - Có bị nhầm lẫn giữa Lợi ích (Benefit) và Giải pháp kỹ thuật (Solution) không?
   - Có mục Out-of-Scope không? (Nếu thiếu $\to$ Cảnh báo nguy cơ Scope Creep).
   - Các Capability có được đánh mã A1, B1 rõ ràng không?
2. **Kiểm tra Business Process Document**:
   - Tiêu đề có tuân thủ quy tắc `Động từ + Danh từ` không?
   - Có phân biệt rõ Entry Criteria (Điều kiện) vs Inputs (Vật phẩm) không?
   - Sơ đồ Mermaid có điểm rẽ nhánh bị thiếu luồng thoát không?
   - Các Business Rules có gắn mã tới từng bước thực hiện không?
3. **Kiểm tra Use Case**:
   - Từng bước trong Basic Flow có chỉ rõ Actor thực hiện không?
   - Các Alternate Flows có chỉ rõ bước quay lại luồng chuẩn không?
   - Có kịch bản lỗi mạng, nhập sai định dạng hoặc tải nặng không?

#### Bước A2: Xuất Báo Cáo Kiểm Toán (Quality Audit Report)
1. Đánh giá theo thang điểm:
   - **Đạt (Pass)**: Đáp ứng đủ 100% tiêu chí bắt buộc.
   - **Cần hoàn thiện (Needs Revision)**: Thiếu luồng ngoại lệ, thiếu mã quy tắc, hoặc ranh giới mờ nhạt.
   - **Chưa đạt (Fail)**: Viết chung chung, thiếu sơ đồ trực quan, không có chỉ số đo lường.
2. Đưa ra danh sách hành động sửa chữa cụ thể (Surgical Action Items).

---

### Nhánh B: Đánh Giá Năng Lực & Khoảng Cách Kỹ Năng BA (Skills Gap Assessment)

#### Bước B1: Phỏng Vấn Thăm Dò Năng Lực Theo Rubric
1. Áp dụng bảng Rubric 3 cấp độ (Novice - Intermediate - Expert) từ tài liệu `references/ba_glossary.md` và `docs/research/05_BA_METHODOLOGY_AND_SKILLS_ASSESSMENT.md`.
2. Khảo sát qua 4 nhóm kỹ thuật:
   - Kỹ năng Mô hình hóa Quy trình (Process Models & As-Is/To-Be).
   - Kỹ năng Xác định Phạm vi & Khám phá Mục tiêu (Scope & Objectives).
   - Kỹ năng Đặc tả Yêu cầu Chi tiết (Use Cases & Agile User Stories).
   - Kỹ năng Khơi gợi & Điều phối Stakeholder (Elicitation & Discovery).

#### Bước B2: Đề Xuất Lộ Trình Phát Triển (Development Plan)
1. Chỉ ra điểm mạnh (Strengths) và các điểm khuyết (Skill Gaps).
2. Đưa ra lộ trình chuyển đổi từ làm việc theo kinh nghiệm tự phát (Informal) sang áp dụng chuẩn quốc tế chính quy (Formal Deliverables).
3. Gợi ý các mẫu biểu và kỹ thuật cần thực hành ngay trong dự án tiếp theo.
