# KẾ HOẠCH THỰC THI LÁT CẮT PHASE 2 & 3: THIẾT KẾ & ĐÓNG GÓI BỘ SKILL BA TIẾNG VIỆT
> **Đường dẫn**: `docs/plans/impl/IMPL_P2_SKILL_PACKAGING.md`  
> **Dự án**: Bộ Skills Agent Kit cho Business Analyst (BA)  
> **Trạng thái**: Sẵn sàng thực thi (P1 Gate Passed)  
> **Phương pháp**: Verification-Driven Planning & Karpathy's Occam's Razor  

---

### P2.1. Khởi Tạo Cấu Trúc Thư Mục & Tổ Chức Gói Kỹ Năng

1. **Mục tiêu & Nhiệm vụ**:
   - Khởi tạo thư mục chuẩn Antigravity Skill tại `skills/ba-analyst-kit/`.
   - Phân cấp 4 thư mục con: `workflows/`, `templates/`, `references/`, `scripts/`.
2. **Tệp tạo hoặc sửa đổi**:
   - `skills/ba-analyst-kit/` (thư mục gốc)
   - `skills/ba-analyst-kit/references/ba_glossary.md` (chuyển giao từ P1.5)
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; assert all(os.path.exists(f'skills/ba-analyst-kit/{d}') for d in ['workflows', 'templates', 'references', 'scripts']); print('P2.1 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng**:
   - Thư mục được tạo với cấu trúc phân tầng rõ ràng, Zero-Dead-Code.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa thư mục `skills/ba-analyst-kit/`.

---

### P2.2. Xây Dựng Bộ 4 Templates Nghiệp Vụ Chuẩn Markdown & Mermaid

1. **Mục tiêu & Nhiệm vụ**:
   - Soạn thảo 4 mẫu biểu Markdown chuẩn hóa tương thích 1:1 với mẫu DOCX gốc của Bridging The Gap:
     1. `skills/ba-analyst-kit/templates/scope_statement_template.md` (10 mục chuẩn + System Context Diagram)
     2. `skills/ba-analyst-kit/templates/business_process_template.md` (Entry/Exit, Business Rules matrix, Mermaid Swimlane)
     3. `skills/ba-analyst-kit/templates/use_case_template.md` (Basic Flow, Alternate 3a/3b, Exception, Gherkin Scenarios)
     4. `skills/ba-analyst-kit/templates/elicitation_checklist_template.md` (5 trụ cột khơi gợi yêu cầu)
2. **Tệp tạo hoặc sửa đổi**:
   - 4 tệp trong `skills/ba-analyst-kit/templates/`.
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; ts=['scope_statement_template.md', 'business_process_template.md', 'use_case_template.md', 'elicitation_checklist_template.md']; assert all(os.path.exists(f'skills/ba-analyst-kit/templates/{t}') for t in ts); print('P2.2 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng**:
   - 4 tệp template tồn tại, có các trường placeholder tường minh `[Tên dự án]`, `[Mục tiêu kinh doanh]`, hướng dẫn chi tiết cho Agent.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa các tệp trong `skills/ba-analyst-kit/templates/`.

---

### P2.3. Xây Dựng 5 Workflows Từng Bước Cho 5 Use Cases Cốt Lõi

1. **Mục tiêu & Nhiệm vụ**:
   - Soạn thảo 5 quy trình thao tác từng bước (Step-by-Step Workflows) hoàn toàn bằng tiếng Việt có dấu:
     1. `skills/ba-analyst-kit/workflows/workflow_01_elicitation.md`
     2. `skills/ba-analyst-kit/workflows/workflow_02_scope_definition.md`
     3. `skills/ba-analyst-kit/workflows/workflow_03_process_modeling.md`
     4. `skills/ba-analyst-kit/workflows/workflow_04_use_case_authoring.md`
     5. `skills/ba-analyst-kit/workflows/workflow_05_quality_review.md`
2. **Tệp tạo hoặc sửa đổi**:
   - 5 tệp trong `skills/ba-analyst-kit/workflows/`.
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; ws=[f'workflow_0{i}_{n}.md' for i, n in [(1, 'elicitation'), (2, 'scope_definition'), (3, 'process_modeling'), (4, 'use_case_authoring'), (5, 'quality_review')]]; assert all(os.path.exists(f'skills/ba-analyst-kit/workflows/{w}') for w in ws); print('P2.3 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng**:
   - Mỗi workflow định rõ: Điều kiện kích hoạt, Đầu vào cần nạp, Trình tự tương tác với người dùng, Mẫu biểu áp dụng, và Tiêu chuẩn nghiệm thu đầu ra.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa các tệp trong `skills/ba-analyst-kit/workflows/`.

---

### P2.4. Soạn Thảo Tệp Điều Phối Chính `SKILL.md` (Single-Entry Router)

1. **Mục tiêu & Nhiệm vụ**:
   - Soạn thảo tệp `skills/ba-analyst-kit/SKILL.md` theo chuẩn Antigravity Skill format (YAML frontmatter với `name`, `description`).
   - Đóng vai trò là Router & Orchestrator: Tự động phát hiện ý định của người dùng và định tuyến sang workflow tương ứng trong 5 use cases.
   - Nhúng nguyên tắc phân tích, guardrails chống ảo giác và liên kết tài liệu.
2. **Tệp tạo hoặc sửa đổi**:
   - `skills/ba-analyst-kit/SKILL.md`
3. **Lệnh kiểm chứng (Deterministic Verification)**:
   - `python -c "import os; p='skills/ba-analyst-kit/SKILL.md'; assert os.path.exists(p) and os.path.getsize(p) > 2000; print('P2.4 Verified: Exit 0')"`
4. **Kết quả mong đợi & Bằng chứng**:
   - Tệp `SKILL.md` hoàn chỉnh, tiếng Việt chuẩn xác, cú pháp Markdown hợp lệ.
5. **Cách hoàn tác (Rollback Strategy)**:
   - Xóa tệp `skills/ba-analyst-kit/SKILL.md`.
