---
name: ba-analyst-kit
description: Bộ công cụ kỹ năng toàn diện dành cho Business Analyst (BA) theo chuẩn quốc tế Bridging The Gap (Laura Brandenburg, CBAP) kết hợp Senior Architecture & Quy chuẩn nghiệp vụ thực chiến. Tích hợp trọn vòng đời 8 use cases nghiệp vụ & kiến trúc dữ liệu (Checklist, Scope Statement, Business Process, Use Case, Quality Audit, Enterprise UAT Sign-off, Data Dictionary/ERD, Data Mapping/API) cùng Đại từ điển 320 Use Cases chuẩn hóa toàn ngành.
---

# BỘ KỸ NĂNG CHUYÊN GIA PHÂN TÍCH NGHIỆP VỤ (BA ANALYST KIT)
> **Chuẩn phương pháp luận**: Bridging The Gap (Laura Brandenburg, CBAP) kết hợp Data Architecture  
> **Ngôn ngữ thực thi**: 100% Tiếng Việt có dấu, thuật ngữ kỹ thuật quốc tế chuẩn xác.  
> **Phiên bản**: 2.0.0 | **Quy mô**: 8 Phân hệ & 320 Use Cases chuẩn hóa  

---

## 1. BẢNG ĐIỀU HƯỚNG TÁC VỤ THỰC CHIẾN (ROUTER & DISPATCHER)

Khi nhận yêu cầu từ người dùng, Agent hãy nhận diện ý định và kích hoạt workflow/template tương ứng:

| Ý Định / Yêu Cầu Của Người Dùng | Use Case Áp Dụng | Workflow / Nguồn Tri Thức | Template Mẫu Áp Dụng |
| :--- | :---: | :--- | :--- |
| "Phỏng vấn lấy yêu cầu", "Làm rõ bài toán", "Khơi gợi tính năng mới", "Checklist yêu cầu" | **UC-1** | [workflow_01_elicitation.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_01_elicitation.md) | [elicitation_checklist_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/elicitation_checklist_template.md) |
| "Viết Scope Statement", "Định nghĩa phạm vi", "Mục tiêu kinh doanh", "Xác định In-Scope/Out-of-Scope" | **UC-2** | [workflow_02_scope_definition.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_02_scope_definition.md) | [scope_statement_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/scope_statement_template.md) |
| "Thiết kế quy trình", "Vẽ sơ đồ quy trình", "Quy trình As-Is / To-Be", "Mô tả các bước nghiệp vụ" | **UC-3** | [workflow_03_process_modeling.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_03_process_modeling.md) | [business_process_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/business_process_template.md) |
| "Viết Use Case", "Đặc tả chức năng", "Viết User Story", "Viết tiêu chí nghiệm thu Gherkin" | **UC-4** | [workflow_04_use_case_authoring.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_04_use_case_authoring.md) | [use_case_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/use_case_template.md) |
| "Review tài liệu BA", "Kiểm tra chất lượng Scope/Use Case", "Đánh giá kỹ năng BA", "Audit tài liệu" | **UC-5** | [workflow_05_quality_review.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_05_quality_review.md) | [ba_glossary.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/ba_glossary.md) |
| "Quy chuẩn an toàn dữ liệu & UAT", "Xác thực sinh trắc học", "Bảo vệ dữ liệu cá nhân", "Biên bản nghiệm thu UAT", "Ký duyệt bàn giao" | **UC-6** | [workflow_06_vietnam_compliance_and_uat.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_06_vietnam_compliance_and_uat.md) | [vietnam_uat_signoff_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/vietnam_uat_signoff_template.md) |
| "Từ điển dữ liệu", "Thiết kế CSDL", "Vẽ sơ đồ ERD", "Đặc tả thuộc tính trường", "Data Dictionary" | **UC-7** | [data_dictionary_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_dictionary_template.md) | [data_dictionary_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_dictionary_template.md) |
| "Ánh xạ API", "Tích hợp hệ thống", "Data Mapping", "Đặc tả Webhook", "Chuyển đổi dữ liệu" | **UC-8** | [data_mapping_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_mapping_template.md) | [data_mapping_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_mapping_template.md) |
| "Tra cứu use case mẫu", "Lấy case kinh điển", "Tìm kịch bản mẫu", "Tra cứu danh mục use case" | **CATALOG** | [master_use_cases_catalog.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/master_use_cases_catalog.md) | [common_use_cases_library.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/common_use_cases_library.md) |

---

## 2. NGUYÊN TẮC PHÂN TÍCH BẤT BIẾN (CORE BA PRINCIPLES)

1. **Ranh Giới Bất Biến (Boundary Invariants)**:
   - Mọi tài liệu phạm vi bắt buộc phải có mục **Out-of-Scope**. Không có Out-of-Scope là dự án cầm chắc thất bại vì Scope Creep.
   - Mọi quy trình bắt buộc phải có câu định vị: *"Quy trình này bắt đầu khi... và kết thúc khi..."*.
2. **Lợi Ích Trước, Tính Năng Sau (Outcomes over Outputs)**:
   - Không nhầm lẫn giữa Lợi ích kinh doanh (Expected Benefits) và Tính năng phần mềm (Features). Lợi ích là mục tiêu đo lường được (%, chi phí, thời gian); tính năng là công cụ phục vụ lợi ích đó.
3. **Quy Tắc Động Từ - Danh Từ (Verb-Noun Phrasing)**:
   - Mọi tiêu đề quy trình nghiệp vụ và tên Use Case bắt buộc phải đặt theo cú pháp `Động từ + Danh từ` (Ví dụ: *"Nộp hồ sơ bồi thường"*, *"Tiếp nhận khiếu nại"*, *"Xác thực tài khoản"*). Cấm đặt tên chung chung như *"Module bồi thường"* hay *"Hệ thống đăng ký"*.
4. **Phân Biệt Rạch Ròi Cặp Đôi Điều Kiện vs Vật Phẩm**:
   - `Entry Criteria` (Điều kiện tiên quyết) $\neq$ `Inputs` (Vật phẩm/dữ liệu cụ thể nhận được).
   - `Outputs` (Sản phẩm hữu hình sinh ra) $\neq$ `Exit Criteria` (Tiêu chuẩn công nhận hoàn tất).
5. **Cầu Nối 2 Chiều Giữa Waterfall & Agile**:
   - Đặc tả chặt chẽ từng luồng rẽ nhánh và ngoại lệ (Alternate Flows 3a, 3b, Exception Flows).
   - Đồng thời bẻ nhỏ thành các Agile User Stories có tiêu chí nghiệm thu định dạng **Gherkin (`Given... When... Then...`)**.
6. **Kiến Trúc Dữ Liệu Tường Minh (Data Modeling Discipline)**:
   - Trước khi lập trình, bắt buộc phải có Từ điển dữ liệu (`Data Dictionary`) chuẩn hóa kiểu dữ liệu, ràng buộc validation, và chính sách che giấu dữ liệu nhạy cảm (Data Masking & Bảo vệ dữ liệu nhạy cảm).

---

## 3. HƯỚNG DẪN TƯƠNG TÁC VỚI NGƯỜI DÙNG (INTERACTIVE GUIDELINES)

Khi người dùng đưa ra một yêu cầu hoặc bài toán mới:
1. **Không hỏi dồn dập**: Tránh gửi một danh sách 20 câu hỏi một lúc khiến người dùng bị quá tải nhận thức.
2. **Gợi ý lựa chọn inline**: Mỗi câu hỏi cần kèm các phương án gợi ý thực tế `a/b/c` và đề xuất sẵn 1 phương án mặc định `(Khuyến nghị)` để người dùng có thể duyệt nhanh bằng 1 dòng tin nhắn.
3. **Trực quan hóa bằng Mermaid**: Luôn tự động vẽ sơ đồ trực quan (System Context Diagram, Swimlane Flowchart, ERD, Sequence Diagram) bằng khối mã Mermaid đi kèm tài liệu phân tích.

---

## 4. BẢO TỒN THUẬT NGỮ CHUẨN (BILINGUAL GLOSSARY REFERENCE)

Tham khảo bảng tra cứu chi tiết tại: [ba_glossary.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/ba_glossary.md).
- **Giữ nguyên thuật ngữ tiếng Anh cốt lõi**: *Actor, Pre-condition, Post-condition, Happy path, Alternate flow, Exception flow, Swimlane, Scope Creep, User Story, Acceptance Criteria, Gherkin, Data Dictionary, Data Mapping, ERD*.
- **Viết tiếng Việt chuẩn xác cho mô tả nghiệp vụ**: Quy tắc nghiệp vụ, Mục tiêu kinh doanh, Điều kiện kích hoạt, Tiêu chuẩn kết thúc, Ngoài phạm vi.

---

## 5. THƯ MỤC TÀI LIỆU & MẪU BIỂU LIÊN KẾT

- 📂 **Templates chuẩn Markdown & Mermaid (7 Mẫu)**:
  - [scope_statement_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/scope_statement_template.md)
  - [business_process_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/business_process_template.md)
  - [use_case_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/use_case_template.md)
  - [elicitation_checklist_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/elicitation_checklist_template.md)
  - [vietnam_uat_signoff_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/vietnam_uat_signoff_template.md) *(Mẫu biên bản nghiệm thu chuẩn thể thức doanh nghiệp)*
  - [data_dictionary_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_dictionary_template.md) *(Mẫu Từ điển dữ liệu & ERD)*
  - [data_mapping_template.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/templates/data_mapping_template.md) *(Mẫu Đặc tả tích hợp API & Ánh xạ dữ liệu)*
- 📂 **Workflows chi tiết (6 Quy trình)**:
  - [workflow_01_elicitation.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_01_elicitation.md)
  - [workflow_02_scope_definition.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_02_scope_definition.md)
  - [workflow_03_process_modeling.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_03_process_modeling.md)
  - [workflow_04_use_case_authoring.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_04_use_case_authoring.md)
  - [workflow_05_quality_review.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_05_quality_review.md)
  - [workflow_06_vietnam_compliance_and_uat.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/workflows/workflow_06_vietnam_compliance_and_uat.md) *(Quy chuẩn an toàn dữ liệu, xác thực & Ký UAT)*
- 📂 **Thư viện tri thức tham chiếu (3 Nguồn)**:
  - [ba_glossary.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/ba_glossary.md): Từ điển đối chiếu thuật ngữ Anh - Việt.
  - [common_use_cases_library.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/common_use_cases_library.md): Thư viện chi tiết Top 10 Use Cases kiến trúc nền tảng.
  - [master_use_cases_catalog.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/master_use_cases_catalog.md): Đại từ điển 320 Use Cases chuẩn hóa toàn ngành phần mềm.

---

## 6. BỘ CÔNG CỤ TỰ ĐỘNG HÓA SOẠN THẢO & KIỂM ĐỊNH (AUTOMATION & VERIFICATION TOOLS)

Agent và BA có thể gọi thực thi trực tiếp các script tự động hóa sau trong terminal:

1. **Sinh đặc tả giao diện UI & Wireframe Layout kèm validation Việt Nam (CCCD, SĐT, MST, VNĐ)**:
   ```powershell
   python scripts/generate_ui_spec.py
   ```
2. **Kiểm tra tính toàn vẹn và hợp chuẩn của bộ công cụ BA**:
   ```powershell
   python scripts/run_full_verification.py
   ```
