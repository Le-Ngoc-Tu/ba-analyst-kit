# KẾ HOẠCH THỰC THI LÁT CẮT PHASE 1: CHIẾT XUẤT TRI THỨC VÀ PHÂN TÍCH SÂU TÀI LIỆU
> **Đường dẫn**: `docs/plans/impl/IMPL_P1_EXTRACTION_SYNTHESIS.md`  
> **Dự án**: Bộ Skills Agent Kit cho Business Analyst (BA)  
> **Trạng thái**: Sẵn sàng thực thi | **Phương pháp**: Verification-Driven Planning  

---

### P1.1. Phân Tích Chuyên Sâu Scope Statement & Business Objectives

1. **Mục tiêu & Nhiệm vụ**:
   - Phân tích chi tiết toàn bộ nội dung từ `Scope-Statement-Template_v3.docx`.
   - Chuẩn hóa cấu trúc 10 phần cốt lõi: Document Info, Project Overview, Expected Benefits (định tính/định lượng), Capabilities & Subgroups, Assumptions, Constraints, Out of Scope, Visual Models, Open Issues, Revision History.
   - Trích xuất case study mẫu về hệ thống bảo hiểm bồi thường (Claims Mobile & Customer Service).
2. **Tệp tạo hoặc sửa đổi**:
   - `docs/research/01_SCOPE_STATEMENT_DEEP_DIVE.md` (tạo mới)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; p='docs/research/01_SCOPE_STATEMENT_DEEP_DIVE.md'; assert os.path.exists(p) and os.path.getsize(p) > 2000; print('P1.1 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng (Expected Artifact)**:
   - Tệp phân tích hoàn chỉnh, chứa toàn bộ cấu trúc trường bắt buộc, bảng biểu ma trận và hướng dẫn thực thi cho BA.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa tệp `docs/research/01_SCOPE_STATEMENT_DEEP_DIVE.md`.

---

### P1.2. Phân Tích Chuyên Sâu Mô Hình Hóa Quy Trình Nghiệp Vụ (Business Process)

1. **Mục tiêu & Nhiệm vụ**:
   - Phân tích toàn diện `Business-Process-Template_v3.docx`.
   - Chuẩn hóa cấu trúc: Cú pháp định nghĩa điểm bắt đầu và kết thúc ("Starts when... Ends when..."), Entry/Exit Criteria, Inputs/Outputs, Activity Descriptions, Exceptions, ma trận Business Rules liên kết với Activity Step, Roles & Responsibilities, và Metrics đo lường hiệu quả.
   - Xây dựng quy chuẩn ánh xạ quy trình công việc sang cú pháp sơ đồ Mermaid Flowchart & Swimlane.
2. **Tệp tạo hoặc sửa đổi**:
   - `docs/research/02_BUSINESS_PROCESS_DEEP_DIVE.md` (tạo mới)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; p='docs/research/02_BUSINESS_PROCESS_DEEP_DIVE.md'; assert os.path.exists(p) and os.path.getsize(p) > 2000; print('P1.2 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng (Expected Artifact)**:
   - Tệp phân tích hoàn chỉnh, có sẵn ví dụ quy trình "Make Job Offer" từ bản mẫu của Bridging The Gap và mẫu sơ đồ Mermaid Swimlane tương ứng.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa tệp `docs/research/02_BUSINESS_PROCESS_DEEP_DIVE.md`.

---

### P1.3. Phân Tích Chuyên Sâu Đặc Tả Use Case & Tích Hợp Agile User Stories

1. **Mục tiêu & Nhiệm vụ**:
   - Phân tích toàn diện `Use-Case-Template_v3.docx`.
   - Chuẩn hóa cấu trúc: Quy tắc đặt tên Use Case dạng Verb-Noun, Brief Description ("starts with / ends with"), Actors (Primary/Secondary/System), Pre-Conditions, Post-Conditions, Basic Flow (Happy Path đánh số), Alternate Flows (3a, 3b rẽ nhánh và quay lại), Exception Flows (xử lý lỗi).
   - Tích hợp thêm phần mở rộng Agile: Chuyển đổi Use Case sang User Stories và Tiêu chuẩn nghiệm thu định dạng Gherkin (`Given... When... Then...`).
2. **Tệp tạo hoặc sửa đổi**:
   - `docs/research/03_USE_CASE_SPEC_DEEP_DIVE.md` (tạo mới)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; p='docs/research/03_USE_CASE_SPEC_DEEP_DIVE.md'; assert os.path.exists(p) and os.path.getsize(p) > 2000; print('P1.3 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng (Expected Artifact)**:
   - Tệp phân tích hoàn chỉnh với quy chuẩn viết Use Case chuẩn quốc tế và cầu nối sang phát triển phần mềm linh hoạt (Agile).
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa tệp `docs/research/03_USE_CASE_SPEC_DEEP_DIVE.md`.

---

### P1.4. Phân Tích Chuyên Sâu Khung Khơi Gợi Yêu Cầu (Requirements Discovery Checklist)

1. **Mục tiêu & Nhiệm vụ**:
   - Phân tích chi tiết `ReqChecklist-SupportCustomers_v2.docx` (123 đoạn văn, 40+ câu hỏi cốt lõi).
   - Chiết xuất 5 trụ cột khơi gợi yêu cầu:
     1. Scope of Service (Phạm vi dịch vụ và đối tượng hỗ trợ).
     2. Triage & Routing (Phân loại, thẩm định và định tuyến yêu cầu).
     3. Addressing Requests (Quy trình xử lý, thẩm quyền, truyền thông và giải quyết).
     4. Monitoring & Metrics (Giám sát SLA, thời gian phản hồi, báo cáo quản trị).
     5. Customer Self-Service & Preemption (Cổng tự phục vụ và các biện pháp chặn trước vấn đề).
2. **Tệp tạo hoặc sửa đổi**:
   - `docs/research/04_REQUIREMENTS_CHECKLIST_DEEP_DIVE.md` (tạo mới)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; p='docs/research/04_REQUIREMENTS_CHECKLIST_DEEP_DIVE.md'; assert os.path.exists(p) and os.path.getsize(p) > 2500; print('P1.4 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng (Expected Artifact)**:
   - Bộ khung câu hỏi khơi gợi yêu cầu tương tác (Interactive Elicitation Questions) dùng làm kịch bản phỏng vấn stakeholder của Agent.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa tệp `docs/research/04_REQUIREMENTS_CHECKLIST_DEEP_DIVE.md`.

---

### P1.5. Phân Tích Phương Pháp Luận 8 Bước BA, Đánh Giá Kỹ Năng & Từ Điển Song Ngữ

1. **Mục tiêu & Nhiệm vụ**:
   - Phân tích 2 tệp PDF: `BA_Skills_Assessment2.pdf` và `BAJobInterviewPrepGuide.pdf`.
   - Chiết xuất quy trình 8 bước chuẩn của Laura Brandenburg:
     1. Get Oriented
     2. Discover Business Objectives
     3. Define Scope
     4. Formulate BA Plan
     5. Define Detailed Requirements
     6. Support Technical Implementation
     7. Help the Business Implement the Solution
     8. Assess the Value Created
   - Trích xuất 12 kỹ năng thực hành và thang đo năng lực 3 cấp độ (Novice - Intermediate - Expert).
   - Xây dựng bảng từ điển thuật ngữ BA đối chiếu chuẩn Anh - Việt (Bilingual BA Glossary) để đảm bảo tính nhất quán ngôn ngữ.
2. **Tệp tạo hoặc sửa đổi**:
   - `docs/research/05_BA_METHODOLOGY_AND_SKILLS_ASSESSMENT.md` (tạo mới)
   - `docs/research/06_BILINGUAL_BA_GLOSSARY.md` (tạo mới)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; assert all(os.path.exists(f'docs/research/{f}') for f in ['05_BA_METHODOLOGY_AND_SKILLS_ASSESSMENT.md', '06_BILINGUAL_BA_GLOSSARY.md']); print('P1.5 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng (Expected Artifact)**:
   - Hai tệp tài liệu phương pháp luận và từ điển hoàn chỉnh sẵn sàng nạp vào tri thức của Skill.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa các tệp tạo mới tương ứng trong `docs/research/`.
