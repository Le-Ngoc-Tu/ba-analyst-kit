# MA TRẬN QUYẾT ĐỊNH, SAI LỆCH VÀ RỦI RO (DECISIONS & RISKS)
> **Đường dẫn**: `docs/plans/05_DECISIONS_AND_RISKS.md`  
> **Dự án**: Bộ Skills Agent Kit cho Business Analyst (BA)  
> **Phiên bản**: 1.0.0 | **Ngày cập nhật**: 2026-10-19  

Tài liệu này lưu trữ toàn bộ các điểm sai lệch thực tế, quyết định kỹ thuật, ma trận rủi ro và các quyết định do Người dùng (User) đã phê chuẩn trong phiên phỏng vấn Grill-Me. Nghiêm cấm bất kỳ Agent nào tự ý thay đổi hoặc đảo ngược các quyết định này khi chưa có sự đồng ý của User.

---

## BẢNG 1: MA TRẬN SAI LỆCH GIỮA TÀI LIỆU VÀ THỰC TẾ (DISCREPANCY MATRIX)

| Mã | Giả định / Dự đoán ban đầu | Thực tế kiểm chứng máy tính đo được | Hướng xử lý trong kế hoạch |
| :--- | :--- | :--- | :--- |
| **S1** | Bộ tài liệu BA chỉ bao gồm các file văn bản mô tả sơ lược hoặc lý thuyết chung chung | Thư mục chứa đúng 6 tệp chuẩn từ Laura Brandenburg (Bridging The Gap) gồm 4 file `.docx` mẫu nghiệp vụ chi tiết và 2 file `.pdf` quy chuẩn đánh giá kỹ năng | Khảo sát bám sát 100% cấu trúc của 6 tài liệu này để xây dựng Skill có tính thực chiến cao nhất |
| **S2** | Tệp `Use-Case-Template_v3.docx` không dùng Heading chuẩn của Word nên khó trích xuất tự động | Tiêu đề các mục dùng `Numeric Level 1 Heading` thay vì `Heading 1` thông thường | Parser tự động trong Python phải hỗ trợ cả các style tùy biến `Numeric Level 1 Heading` và `DocInfoHeading` |
| **S3** | Template chỉ thuần text, không có bảng dữ liệu | Cả 4 tệp DOCX đều chứa các bảng ma trận quan trọng (Document Information, Business Rules matrix, Roles & Responsibilities matrix, Revision History) | Schema của Skill phải hỗ trợ đầy đủ các bảng ma trận dạng Markdown tables tương thích 1:1 với mẫu DOCX gốc |
| **S4** | Tài liệu chỉ áp dụng cho quy trình Waterfall truyền thống | Tệp `BA_Skills_Assessment2.pdf` chỉ rõ phương pháp BA hiện đại kết hợp cả Use Cases cổ điển và Agile User Stories, Product Backlog, Wireframes | Thiết kế Skill kết hợp hài hòa cả Use Cases chi tiết và User Stories kèm tiêu chí nghiệm thu Gherkin (Given-When-Then) |

---

## BẢNG 2: MA TRẬN QUYẾT ĐỊNH KỸ THUẬT (TECHNICAL DECISIONS MATRIX)

| Mã | Quyết định đã chọn | Phương án thay thế bị loại | Lý do chọn phương án này |
| :--- | :--- | :--- | :--- |
| **D1** | Đóng gói thành 1 Skill Antigravity duy nhất (`ba-analyst-kit`) có chứa đầy đủ 5 use cases nghiệp vụ | Tách thành 4-8 micro-skills phân mảnh | Giữ ngữ cảnh liền mạch cho LLM, tránh tình trạng chuyển đổi ngữ cảnh liên tục, giúp BA sử dụng một lệnh duy nhất thực hiện trọn vẹn luồng công việc |
| **D2** | Sử dụng ngôn ngữ tiếng Việt làm ngôn ngữ chỉ dẫn, prompt, template và workflow chính | Viết hoàn toàn bằng tiếng Anh | Đáp ứng trực tiếp nhu cầu người dùng, giúp đội ngũ BA và Product Owner người Việt tiếp cận nhanh chóng, dễ hiểu và dễ ứng dụng ngay |
| **D3** | Định dạng sinh tài liệu sử dụng Markdown kết hợp sơ đồ Mermaid | Xuất trực tiếp ra định dạng binary Word (`.docx`) | Markdown + Mermaid thân thiện với Git versioning, nhẹ, dễ render trực tiếp trong IDE/CLI/Web, và có thể chuyển đổi tự động sang Word/PDF khi cần |
| **D4** | Xây dựng bộ script Python kiểm chứng độc lập (Schema & Content Validator) | Chỉ kiểm tra bằng mắt (Human Review) | Đảm bảo tính bất biến của nguyên lý Verification-Driven Planning; mọi tài liệu do Skill sinh ra phải vượt qua validator với Exit Code 0 |
| **D5** | Cấu trúc hóa các kỹ thuật biểu đồ sang Mermaid Flowchart & Swimlane chuẩn | Dùng ảnh chụp ngoài hoặc mô tả chay không có sơ đồ | Giúp Agent có thể tự động vẽ và cập nhật quy trình công việc (As-Is / To-Be) ngay trong văn bản mà không phụ thuộc vào công cụ vẽ bên ngoài |

---

## BẢNG 3: MA TRẬN RỦI RO VÀ BIỆN PHÁP DỰ PHÒNG (RISK & MITIGATION MATRIX)

| Mã | Rủi ro tiềm ẩn | Mức độ | Biện pháp giảm thiểu & Phương án dự phòng (Fallback) |
| :--- | :--- | :--- | :--- |
| **R1** | Skill quá dài khiến vượt ngưỡng token context window của Agent | Trung bình | Tách các mẫu biểu chi tiết vào thư mục `templates/` và quy trình vào `workflows/`. Tệp `SKILL.md` chỉ đóng vai trò điều phối (Router & Orchestrator) |
| **R2** | Agent sinh ra các Business Rules hoặc Use Case bị thiếu trường quan trọng | Cao | Định nghĩa sẵn các Checklist bắt buộc (Mandatory Fields) trong từng template; script validator sẽ quét và bắt lỗi nếu thiếu trường |
| **R3** | Thuật ngữ tiếng Việt bị dịch gượng gạo, sai lệch so với chuẩn BA quốc tế | Trung bình | Ban hành từ điển thuật ngữ đối chiếu (Bilingual BA Glossary): giữ nguyên các từ kỹ thuật cốt lõi (Pre-condition, Post-condition, Swimlane, Elicitation, v.v.) kèm giải thích nghĩa tiếng Việt |
| **R4** | Người dùng cung cấp yêu cầu đầu vào quá mơ hồ, không đủ thông tin để viết Use Case | Cao | Tích hợp chế độ `interactive-elicitation` vào Skill: Agent sẽ chủ động đặt câu hỏi khơi gợi theo checklist trước khi bắt tay vào viết tài liệu |

---

## BẢNG 4: MA TRẬN QUYẾT ĐỊNH NGƯỜI DÙNG ĐÃ CHỐT (USER DECISIONS MATRIX - Q)

| Mã | Vấn đề đã thảo luận trong Grill-Me | Quyết định Người dùng đã chốt | Hệ quả kiến trúc & Kế hoạch |
| :--- | :--- | :--- | :--- |
| **Q1** | Nền tảng và định dạng của Agent Kit | **Bộ Antigravity Skills chuẩn** (`SKILL.md` kèm prompt, workflow, scripts và template chuẩn) dùng ngay trong Antigravity CLI/IDE | Đóng gói theo đúng cấu trúc tiêu chuẩn của Antigravity Skill, đặt tại `skills/ba-analyst-kit/` |
| **Q2** | Cấu trúc phân rã các kỹ năng trong Kit | **Một Skill duy nhất** có đầy đủ các use case phổ biến, viết bằng **tiếng Việt** để dễ sử dụng và dễ hiểu | Thiết kế `ba-analyst-kit` với kiến trúc điều hướng đa tác vụ (Multi-workflow single-entry skill) viết hoàn toàn bằng tiếng Việt |
| **Q3** | Hình thức lưu trữ kết quả nghiên cứu chuyên sâu | **Bộ 6 tài liệu sống chuẩn Senior Playbook** (`docs/plans/` + `context-map.md`) | Khởi tạo đầy đủ: `context-map.md`, `NEXT_STEPS.md`, `00_MASTER_PLAN.md`, `05_DECISIONS_AND_RISKS.md`, `IMPL_00_INDEX.md`, `HANDOFF.md` |
| **Q4** | Phạm vi các Use Case thực chiến cần bao quát | **Toàn diện 5 use cases nghiệp vụ chính**: 1) Khơi gợi yêu cầu (Checklists), 2) Định nghĩa Scope Statement, 3) Thiết kế Quy trình nghiệp vụ, 4) Soạn thảo Use Case/User Story, 5) Đánh giá/Review tài liệu BA | Kế hoạch nghiên cứu và gói kỹ năng sẽ phân bổ đồng đều trọng số nghiên cứu cho cả 5 trụ cột nghiệp vụ này |
| **Q5** | Bản địa hóa thị trường Việt Nam & Công cụ tự động hóa viết tài liệu | Nghiên cứu sâu thực tiễn BA Việt Nam (Nghị định 13/2023, Quyết định 2345/QĐ-NHNN, thể thức Nghị định 30/2020) và xây dựng bộ tool xuất bản Word `.docx` tự động | Bổ sung `workflow_06_vietnam_compliance_and_uat.md`, `vietnam_uat_signoff_template.md`, script `export_ba_docx.py`, và `generate_ui_spec.py` |

