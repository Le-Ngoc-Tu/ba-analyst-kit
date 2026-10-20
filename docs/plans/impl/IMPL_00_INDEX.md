# CHỈ MỤC CÁC LÁT CẮT THỰC THI (IMPL INDEX)
> **Đường dẫn**: `docs/plans/impl/IMPL_00_INDEX.md`  
> **Dự án**: Bộ Skills Agent Kit cho Business Analyst (BA)  
> **Phiên bản**: 1.0.0 | **Ngày lập**: 2026-10-19  

Tài liệu này đóng vai trò mục lục điều hướng chi tiết cho các kế hoạch thực thi lát cắt dọc (Vertical Slice Implementation Plans) của dự án. Mọi bước thực hiện phải tuân thủ chuẩn Khối Bước Chuẩn (Standard Step Block) và có lệnh kiểm chứng nguyên bản trả về Exit Code 0.

---

## DANH MỤC CÁC TỆP KẾ HOẠCH THỰC THI (IMPL PLANS)

| Tệp Thực Thi | Giai Đoạn Tương Ứng | Số Lượng Bước | Trạng Thái | Mô Tả Trọng Tâm |
| :--- | :--- | :--- | :--- | :--- |
| [IMPL_P1_EXTRACTION_SYNTHESIS.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/docs/plans/impl/IMPL_P1_EXTRACTION_SYNTHESIS.md) | Phase 1: Phân Tích Chuyên Sâu 6 Tài Liệu | 5 bước (`P1.1` $\to$ `P1.5`) | **ĐÃ HOÀN THÀNH (Gate Passed)** | Trích xuất toàn diện 100% cấu trúc, quy tắc, bảng biểu và rubric từ 6 tài liệu gốc thành các báo cáo tri thức chuẩn hóa |
| [IMPL_P2_SKILL_PACKAGING.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/docs/plans/impl/IMPL_P2_SKILL_PACKAGING.md) | Phase 2 & 3: Đóng Gói Bộ Skill BA Tiếng Việt | 4 bước (`P2.1` $\to$ `P2.4`) | **Sẵn sàng thực thi** | Xây dựng mã nguồn Skill, 5 Workflows, 4 Templates Markdown/Mermaid, và từ điển thuật ngữ BA song ngữ |
| [IMPL_P3_VERIFICATION_HARNESS.md](file:///C:/Users/NGOCTU/Downloads/BADeliverablesCollection-BridgingTheGap/docs/plans/impl/IMPL_P3_VERIFICATION_HARNESS.md) | Phase 4: Kiểm Thử Thực Nghiệm & Nghiệm Thu | 3 bước (`P3.1` $\to$ `P3.3`) | Đang chờ P2 Gate | Viết bộ script kiểm chứng độc lập (Schema Validator), sinh thử nghiệm bộ hồ sơ mẫu, và hoàn tất báo cáo nghiệm thu |

---

## NGUYÊN TẮC THI CÔNG BẤT BIẾN
1. **Tuần tự từng bước**: Không nhảy cóc bước thực thi khi bước trước đó chưa vượt qua lệnh kiểm chứng.
2. **Không nới lỏng kiểm tra**: Lệnh kiểm chứng phải chạy thật, không pipe giấu lỗi, không dùng mock dữ liệu giả khi đã có dữ liệu thực tế.
3. **Gắn vết commit**: Mỗi bước thực thi hoàn tất tương ứng với một commit theo quy ước Conventional Commits tiếng Việt.
