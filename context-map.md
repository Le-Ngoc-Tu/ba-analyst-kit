# CONTEXT MAP — BỘ SKILLS AGENT KIT CHO BUSINESS ANALYST (BA)
> **Phiên bản**: 2.0.0 | **Ngày lập**: 2026-10-20 | **Trạng thái**: **COMPLETED (8 Use Cases & 320 Master Catalog)**
> **Giấy phép**: MIT License (Copyright (c) 2026 Le Ngoc Tu)

---

## VIỆC TIẾP THEO (đọc mục này đầu tiên)
Toàn bộ dự án đã hoàn thành và được nghiệm thu tự động 100% (Exit Code 0). 
Hành động sẵn sàng: Đã cài đặt vĩnh viễn vào hệ thống toàn cục tại [`~/.gemini/antigravity-cli/skills/ba-analyst-kit/SKILL.md`](file:///C:/Users/NGOCTU/.gemini/antigravity-cli/skills/ba-analyst-kit/SKILL.md), sẵn sàng sử dụng cho mọi dự án. Bản sao chép cục bộ lưu tại [skills/ba-analyst-kit/SKILL.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/SKILL.md). Đại từ điển 320 Use Cases tại [master_use_cases_catalog.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/skills/ba-analyst-kit/references/master_use_cases_catalog.md). Dự án mẫu tại [examples/claims_support_system/](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/examples/claims_support_system/).

---

## Architecture (Kiến Trúc Tổng Thể)

### 1. Mô hình Tổ chức Bộ Tài liệu Sống (Living Documents Architecture)
```text
ba-analyst-kit/
├── assets/                                 # Banner GIF hoạt họa và tài nguyên hình ảnh
├── context-map.md                          # [BẢN ĐỒ KIẾN TRÚC & ACTIVE CONTEXT]
├── LICENSE                                 # Giấy phép mã nguồn mở MIT License
├── README.md                               # Tài liệu hướng dẫn chính thức
├── docs/                                   # Hệ thống Living Documents & Báo cáo nghiên cứu
│   ├── research/                           # 8 Chuyên đề nghiên cứu sâu & Quy chuẩn phân tích
│   ├── plans/                              # Kế hoạch tổng thể và ma trận quản trị rủi ro
│   └── evidence/                           # Báo cáo nghiệm thu thực nghiệm
├── examples/                               # Dự án mẫu thực tế (Bảo hiểm, Flash Sale ECOMM-11, FIN-09)
├── scripts/                                # Công cụ tự động hóa & Test Runner kiểm chứng
└── skills/                                 # [NƠI CHỨA ARTIFACT SKILL KIT]
    └── ba-analyst-kit/
        ├── SKILL.md                        # Router 8 Phân hệ & 320 Use Cases
        ├── templates/                      # 7 Mẫu Markdown & Mermaid (Scope, Process, UC, Elicitation, UAT, Data Dict, Data Map)
        ├── workflows/                      # 6 Quy trình thực thi từ Elicitation đến UAT
        └── references/                     # 3 Thư viện: Thuật ngữ, 10 Core Cases, 320 Master Catalog
```

---

## Feature Index (8 Phân Hệ Nghiệp Vụ Của BA Skill v2.0.0)

| Mã Use Case | Tên Use Case | Nguồn Phương Pháp Luận | Đầu Ra Chuẩn Hóa |
| :--- | :--- | :--- | :--- |
| **UC-1** | Khơi gợi yêu cầu & Elicitation Sessions | Bridging The Gap Elicitation Framework | Bộ Checklist câu hỏi khơi gợi, bảng phân loại luồng thông tin, triage & routing matrix |
| **UC-2** | Định nghĩa Scope Statement & Business Objectives | Bridging The Gap Scope Framework | Tài liệu Scope Statement chuẩn: Drivers, Objectives, In/Out Scope, Capabilities, Constraints |
| **UC-3** | Thiết kế Quy trình nghiệp vụ (Business Process Modeling) | Bridging The Gap Process Modeling | Business Process Document: Entry/Exit, Activity Steps, Business Rules, Exceptions, Metrics, Sơ đồ Mermaid Swimlane |
| **UC-4** | Soạn thảo Use Case chi tiết & User Stories | Bridging The Gap Use Case Analysis | Use Case Document (Happy path, Alternate Flows 3a/3b, Exception Flows) kết hợp User Story & Gherkin Acceptance Criteria |
| **UC-5** | Đánh giá chất lượng tài liệu & Khoảng cách kỹ năng BA | Bridging The Gap Competency Model | Bảng kiểm toán chất lượng tài liệu (Gate Quality Audit) & Bảng tự đánh giá kỹ năng BA (Novice -> Expert) |
| **UC-6** | Quy chuẩn an toàn dữ liệu, sinh trắc & Nghiệm thu UAT | Quy chuẩn kiểm soát an toàn & bảo vệ dữ liệu | Biên bản nghiệm thu UAT chuẩn thể thức doanh nghiệp, Ma trận kiểm toán bảo vệ dữ liệu cá nhân & xác thực sinh trắc học |
| **UC-7** | Từ điển dữ liệu nghiệp vụ & Mô hình hóa ERD | Data Modeling & Architecture Standards | Bảng đặc tả thuộc tính dữ liệu, validation rules, chính sách Data Masking, sơ đồ Mermaid ERD |
| **UC-8** | Đặc tả tích hợp API & Ánh xạ dữ liệu (Data Mapping) | System Integration & API Architecture | Ma trận ánh xạ dữ liệu 2 chiều (Request/Response), Webhook đối soát, sơ đồ Mermaid System Context |
| **CATALOG** | Đại từ điển 320 Use Cases chuẩn hóa toàn ngành | Tổng hợp 12 Miền nghiệp vụ (Auth, Ecomm, Pay, Fin, CRM, CS, HRM, WMS, CMS, Notif, Data, Admin) | Thư viện 320 kịch bản có mã định danh, Actors, Pre-conditions, Happy path, Exceptions & Business Rules |

---

## Deliverables & Contracts (Quy Ước Hợp Đồng Đầu Ra)
1. **Ngôn ngữ Skill**: 100% tiếng Việt có dấu chuẩn xác cho hướng dẫn, giải thích, prompts và template; giữ nguyên các thuật ngữ kỹ thuật quốc tế chuẩn BA (Swimlane, Pre-condition, Post-condition, Happy path, Elicitation, Gherkin, Actor, Scope Statement, v.v.).
2. **Định dạng sinh tài liệu**: Markdown kết hợp Mermaid diagram trực quan (dễ render trên mọi nền tảng, Git-friendly, và tương thích mọi LLM).
3. **Quy chuẩn kiểm chứng (Verification)**: Mọi artifact tạo ra bởi Skill phải tuân thủ schema Markdown được định nghĩa trước, có script validator kiểm tra tính đầy đủ của các trường bắt buộc (Exit code 0).
