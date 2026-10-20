# CONTEXT MAP — BỘ SKILLS AGENT KIT CHO BUSINESS ANALYST (BA)
> **Phiên bản**: 2.0.0 | **Ngày lập**: 2026-10-20 | **Trạng thái**: **COMPLETED (8 Use Cases & 320 Master Catalog)**

---

## VIỆC TIẾP THEO (đọc mục này đầu tiên)
Toàn bộ dự án đã hoàn thành và được nghiệm thu tự động 100% (Báo cáo tại `docs/evidence/REPORT.md`, Exit Code 0). 
Hành động sẵn sàng: Đã cài đặt vĩnh viễn vào hệ thống toàn cục tại [`~/.gemini/antigravity-cli/skills/ba-analyst-kit/SKILL.md`](file:///C:/Users/NGOCTU/.gemini/antigravity-cli/skills/ba-analyst-kit/SKILL.md), sẵn sàng sử dụng cho mọi dự án. Bản sao chép cục bộ lưu tại [skills/ba-analyst-kit/SKILL.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/SKILL.md). Đại từ điển 320 Use Cases tại [master_use_cases_catalog.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/master_use_cases_catalog.md). Dự án mẫu tại [examples/claims_support_system/](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/examples/claims_support_system/).

---

## Architecture (Kiến Trúc Tổng Thể)

### 1. Mô hình Tổ chức Bộ Tài liệu Sống (Living Documents Architecture)
```text
BADeliverablesCollection-BridgingTheGap/
├── context-map.md                          # [BẢN ĐỒ KIẾN TRÚC & ACTIVE CONTEXT]
├── extracted_docs_summary.json             # Dữ liệu trích xuất cấu trúc thô từ 6 tài liệu gốc
├── docs/
│   ├── NEXT_STEPS.md                       # [HƯỚNG DẪN TIẾP QUẢN & RUNBOOK THỰC THI]
│   ├── HANDOFF.md                          # [NHẬT KÝ BÀN GIAO, NGHIỆM THU & NỢ KỸ THUẬT]
│   └── plans/                              # [KẾ HOẠCH & BỘ 4 BẢNG MA TRẬN QUẢN TRỊ]
├── dist/docx/                              # [14 FILE WORD CHUẨN THỂ THỨC NGHỊ ĐỊNH 30]
└── skills/                                 # [NƠI CHỨA ARTIFACT SKILL KIT]
    └── ba-analyst-kit/
        ├── SKILL.md                        # Router 8 Phân hệ & 320 Use Cases
        ├── templates/                      # 7 Mẫu Markdown & Mermaid (Scope, Process, UC, Elicitation, UAT, Data Dict, Data Map)
        ├── workflows/                      # 6 Quy trình thực thi từ Elicitation đến UAT
        ├── references/                     # 3 Thư viện: Thuật ngữ, 10 Core Cases, 320 Master Catalog
        └── scripts/                        # Automation xuất Word (.docx) & UI Wireframe
```

---

## Feature Index (8 Phân Hệ Nghiệp Vụ Của BA Skill v2.0.0)

| Mã Use Case | Tên Use Case | Nguồn Tài Liệu Gốc | Đầu Ra Chuẩn Hóa |
| :--- | :--- | :--- | :--- |
| **UC-1** | Khơi gợi yêu cầu & Elicitation Sessions | `ReqChecklist-SupportCustomers_v2.docx`, `BA_Skills_Assessment2.pdf` | Bộ Checklist câu hỏi khơi gợi, bảng phân loại luồng thông tin, triage & routing matrix |
| **UC-2** | Định nghĩa Scope Statement & Business Objectives | `Scope-Statement-Template_v3.docx`, `BA_Skills_Assessment2.pdf` (Steps 2-3) | Tài liệu Scope Statement chuẩn: Drivers, Objectives, In/Out Scope, Capabilities, Constraints |
| **UC-3** | Thiết kế Quy trình nghiệp vụ (Business Process Modeling) | `Business-Process-Template_v3.docx` | Business Process Document: Entry/Exit, Activity Steps, Business Rules, Exceptions, Metrics, Sơ đồ Mermaid Swimlane |
| **UC-4** | Soạn thảo Use Case chi tiết & User Stories | `Use-Case-Template_v3.docx` | Use Case Document (Happy path, Alternate Flows 3a/3b, Exception Flows) kết hợp User Story & Gherkin Acceptance Criteria |
| **UC-5** | Đánh giá chất lượng tài liệu & Khoảng cách kỹ năng BA | `BA_Skills_Assessment2.pdf`, `BAJobInterviewPrepGuide.pdf` | Bảng kiểm toán chất lượng tài liệu (Gate Quality Audit) & Bảng tự đánh giá kỹ năng BA (Novice -> Expert) |
| **UC-6** | Tuân thủ pháp lý Việt Nam & Nghiệm thu UAT | `NĐ 13/2023, QĐ 2345/QĐ-NHNN, Luật GDĐT, NĐ 30/2020` | Biên bản nghiệm thu UAT chuẩn thể thức Việt Nam, Ma trận kiểm toán tuân thủ bảo vệ dữ liệu cá nhân & sinh trắc học |
| **UC-7** | Từ điển dữ liệu nghiệp vụ & Mô hình hóa ERD | `BA_Skills_Assessment2.pdf` (Page 3-4, ERD & Data Dictionary) | Bảng đặc tả thuộc tính dữ liệu, validation rules, chính sách Data Masking NĐ 13, sơ đồ Mermaid ERD |
| **UC-8** | Đặc tả tích hợp API & Ánh xạ dữ liệu (Data Mapping) | `BA_Skills_Assessment2.pdf` (Page 4, Data Mapping & API Spec) | Ma trận ánh xạ dữ liệu 2 chiều (Request/Response), Webhook đối soát, sơ đồ Mermaid System Context |
| **CATALOG** | Đại từ điển 320 Use Cases chuẩn hóa toàn ngành | Tổng hợp 12 Miền nghiệp vụ (Auth, Ecomm, Pay, Fin, CRM, CS, HRM, WMS, CMS, Notif, Data, Admin) | Thư viện 320 kịch bản có mã định danh, Actors, Pre-conditions, Happy path, Exceptions & Business Rules |

---

## Deliverables & Contracts (Quy Ước Hợp Đồng Đầu Ra)
1. **Ngôn ngữ Skill**: 100% tiếng Việt có dấu chuẩn xác cho hướng dẫn, giải thích, prompts và template; giữ nguyên các thuật ngữ kỹ thuật quốc tế chuẩn BA (Swimlane, Pre-condition, Post-condition, Happy path, Elicitation, Gherkin, Actor, Scope Statement, v.v.).
2. **Định dạng sinh tài liệu**: Markdown kết hợp Mermaid diagram trực quan (dễ render trên mọi nền tảng, Git-friendly, và có thể chuyển đổi sang Word/PDF).
3. **Quy chuẩn kiểm chứng (Verification)**: Mọi artifact tạo ra bởi Skill phải tuân thủ schema Markdown được định nghĩa trước, có script validator kiểm tra tính đầy đủ của các trường bắt buộc (Exit code 0).
