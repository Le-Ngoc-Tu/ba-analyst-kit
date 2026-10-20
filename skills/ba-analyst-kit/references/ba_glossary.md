# TỪ ĐIỂN THUẬT NGỮ BA SONG NGỮ ANH - VIỆT (BILINGUAL BA GLOSSARY)
> **Mã tài liệu**: `docs/research/06_BILINGUAL_BA_GLOSSARY.md`  
> **Nguồn chuẩn hóa**: Bộ tài liệu Bridging The Gap (Laura Brandenburg) & Chuẩn BABOK v3  
> **Áp dụng cho**: Toàn bộ Skill `ba-analyst-kit` và các Deliverables  
> **Phiên bản**: 1.0.0 | **Ngày lập**: 2026-10-19  

---

## 1. NGUYÊN TẮC CHUẨN HÓA THUẬT NGỮ CỦA SKILL

Để giải quyết triệt để rủi ro dịch thuật gượng gạo hoặc làm sai lệch ý nghĩa kỹ thuật:
1. **Bảo tồn thuật ngữ kỹ thuật cốt lõi (Core Technical Terms)**: Giữ nguyên các từ tiếng Anh chuẩn quốc tế đã trở thành tiêu chuẩn chung trong ngành CNTT (ví dụ: *Actor, Pre-condition, Post-condition, Happy path, Swimlane, Use Case, User Story, Gherkin, Scope Creep*).
2. **Dịch nghĩa chính xác theo ngữ cảnh nghiệp vụ**: Dịch rõ ràng và chuẩn mực các khái niệm mang tính vận hành doanh nghiệp (*Business Objective = Mục tiêu kinh doanh, Entry Criteria = Điều kiện kích hoạt, In-Scope = Trong phạm vi*).
3. **Cấu trúc hiển thị chuẩn**: Khi xuất hiện lần đầu trong tài liệu, hiển thị dưới dạng: `Thuật ngữ tiếng Việt (Thuật ngữ tiếng Anh)`.

---

## 2. BẢNG TRA CỨU THUẬT NGỮ SONG NGỮ CHI TIẾT

### 2.1. Nhóm Phạm Vi & Mục Tiêu Kinh Doanh (Scope & Business Objectives)

| Thuật Ngữ Tiếng Anh | Thuật Ngữ Tiếng Việt Chuẩn | Định Nghĩa Ngắn & Ngữ Cảnh Sử Dụng |
| :--- | :--- | :--- |
| **Business Analyst (BA)** | Chuyên viên Phân tích Nghiệp vụ | Người đóng vai trò cầu nối, chuyển hóa nhu cầu kinh doanh thành đặc tả giải pháp kỹ thuật. |
| **Business Sponsor** | Người bảo trợ dự án | Lãnh đạo cấp cao có thẩm quyền cao nhất phê duyệt phạm vi và ngân sách dự án. |
| **Stakeholder** | Các bên liên quan | Mọi cá nhân, phòng ban hoặc tổ chức có quyền lợi, nghĩa vụ hoặc chịu ảnh hưởng bởi dự án. |
| **Business Driver** | Động lực kinh doanh | Lý do căn bản hoặc áp lực thị trường thúc đẩy doanh nghiệp phải đầu tư vào dự án. |
| **Business Objective** | Mục tiêu kinh doanh | Kết quả cụ thể, đo lường được (%, chi phí, thời gian) mà doanh nghiệp mong muốn đạt được. |
| **Scope Statement** | Tuyên bố phạm vi dự án | Văn bản hợp đồng nghiệp vụ xác định ranh giới những gì được làm và không được làm. |
| **Scope Creep** | Hiện tượng trôi phạm vi | Việc dự án bị phình to tính năng không kiểm soát do không quản lý chặt ranh giới ban đầu. |
| **In-Scope** | Trong phạm vi | Các tính năng, nghiệp vụ cam kết sẽ hoàn thành và bàn giao trong giai đoạn hiện tại. |
| **Out-of-Scope** | Ngoài phạm vi | Các tính năng bị từ chối rõ ràng, không thực hiện trong giai đoạn này để bảo vệ ngân sách. |
| **Capabilities** | Năng lực giải pháp | Tập hợp các khả năng mà giải pháp mang lại cho người dùng và tổ chức. |
| **Assumption** | Giả định | Điều kiện được tin là đúng nhưng chưa có bằng chứng kiểm chứng độc lập. |
| **Constraint** | Ràng buộc | Giới hạn cứng bắt buộc phải tuân theo (ngân sách trần, thời hạn deadline, quy định pháp lý). |

---

### 2.2. Nhóm Quy Trình Nghiệp Vụ (Business Process & Workflow)

| Thuật Ngữ Tiếng Anh | Thuật Ngữ Tiếng Việt Chuẩn | Định Nghĩa Ngắn & Ngữ Cảnh Sử Dụng |
| :--- | :--- | :--- |
| **As-Is Process** | Quy trình hiện trạng | Cách thức doanh nghiệp đang vận hành thực tế tại thời điểm hiện tại (trước khi cải tiến). |
| **To-Be Process** | Quy trình tương lai | Quy trình đích đã được tinh gọn, tối ưu và số hóa phục vụ phát triển phần mềm. |
| **Swimlane Diagram** | Sơ đồ quy trình phân làn | Sơ đồ luồng công việc chia theo các cột/hàng tương ứng với từng vai trò hoặc phòng ban. |
| **Entry Criteria** | Điều kiện kích hoạt | Các điều kiện bắt buộc phải thỏa mãn trước khi quy trình được phép bắt đầu. |
| **Inputs** | Dữ liệu / Vật phẩm đầu vào | Các tài liệu, bản ghi hoặc dữ liệu hữu hình nhận được để thực hiện quy trình. |
| **Outputs** | Sản phẩm đầu ra | Các tài liệu, hóa đơn, hoặc dữ liệu hữu hình sinh ra sau khi quy trình hoàn thành. |
| **Exit Criteria** | Tiêu chuẩn kết thúc | Điều kiện để xác nhận quy trình đã hoàn tất thành công (là Entry Criteria cho quy trình sau). |
| **Business Rule** | Quy tắc nghiệp vụ | Chính sách, luật lệ kinh doanh định hướng hoặc ràng buộc hành vi thao tác của quy trình. |
| **Decision Point** | Điểm rẽ nhánh quyết định | Vị trí trong sơ đồ quy trình mà luồng công việc phân nhánh dựa trên điều kiện kiểm tra. |
| **Cycle Time** | Thời gian chu kỳ | Tổng thời gian tính từ lúc quy trình bắt đầu cho đến khi kết thúc trọn vẹn. |
| **Bottleneck** | Điểm nghẽn | Nút thắt trong quy trình gây ùn ứ công việc, làm giảm hiệu năng chung của toàn hệ thống. |

---

### 2.3. Nhóm Đặc Tả Yêu Cầu Phần Mềm (Software Requirements & Use Cases)

| Thuật Ngữ Tiếng Anh | Thuật Ngữ Tiếng Việt Chuẩn | Định Nghĩa Ngắn & Ngữ Cảnh Sử Dụng |
| :--- | :--- | :--- |
| **Use Case** | Trường hợp sử dụng | Văn bản mô tả chuỗi tương tác giữa Actor và Phần mềm nhằm đạt được mục tiêu cụ thể. |
| **Actor** | Tác nhân | Con người (người dùng cuối, quản trị viên) hoặc hệ thống bên ngoài tương tác với phần mềm. |
| **Primary Actor** | Tác nhân chính | Đối tượng trực tiếp khởi xướng và hưởng lợi từ mục tiêu của Use Case. |
| **Secondary Actor** | Tác nhân phụ | Đối tượng hoặc hệ thống hỗ trợ hệ thống chính hoàn thành Use Case. |
| **Pre-Condition** | Tiền điều kiện | Trạng thái hệ thống bắt buộc phải đúng trước khi Use Case có thể bắt đầu. |
| **Post-Condition** | Hậu điều kiện | Trạng thái dữ liệu và hệ thống sau khi Use Case hoàn thành thành công. |
| **Basic Flow / Happy Path** | Luồng thao tác chuẩn | Chuỗi các bước diễn ra bình thường và thuận lợi nhất trong hầu hết thời gian. |
| **Alternate Flow** | Luồng rẽ nhánh thay thế | Nhánh đi khác luồng chuẩn nhưng vẫn đạt được mục tiêu và quay trở lại luồng chuẩn. |
| **Exception Flow** | Luồng ngoại lệ / Luồng lỗi | Tình huống lỗi phát sinh ngăn cản việc hoàn thành mục tiêu của Use Case. |
| **User Story** | Câu chuyện người dùng | Định dạng yêu cầu Agile: *"Là một [Ai]... Tôi muốn [Gì]... Để [Lợi ích]"*. |
| **Acceptance Criteria (AC)** | Tiêu chí nghiệm thu | Các điều kiện kiểm thử cần đạt được để coi một User Story đã hoàn tất (Definition of Done). |
| **Gherkin Syntax** | Cú pháp Gherkin | Cú pháp viết tiêu chí nghiệm thu chuẩn hóa dạng: Given (Giả sử) - When (Khi) - Then (Thì). |
| **Wireframe / Mockup** | Bản vẽ phác thảo giao diện | Bản vẽ bố cục màn hình hiển thị trực quan các thành phần UI để kiểm chứng luồng tương tác. |

---

### 2.4. Nhóm Khơi Gợi Yêu Cầu & Kiến Trúc Dữ Liệu (Elicitation & Data Modeling)

| Thuật Ngữ Tiếng Anh | Thuật Ngữ Tiếng Việt Chuẩn | Định Nghĩa Ngắn & Ngữ Cảnh Sử Dụng |
| :--- | :--- | :--- |
| **Requirements Elicitation**| Khơi gợi yêu cầu | Quá trình chủ động phỏng vấn, điều phối và khám phá nhu cầu từ các bên liên quan. |
| **Discovery Session** | Phiên làm việc khám phá | Cuộc họp tập trung chuyên sâu giữa BA và các phòng ban để làm rõ quy trình và yêu cầu. |
| **Triage & Routing** | Phân loại và định tuyến | Quy trình thẩm định loại yêu cầu và chuyển giao tự động tới đúng người xử lý. |
| **Service Level Agreement (SLA)** | Cam kết chất lượng dịch vụ | Thỏa thuận mức thời gian phản hồi và xử lý tối đa giữa đơn vị cung cấp và khách hàng. |
| **First Contact Resolution (FCR)** | Tỷ lệ giải quyết lần đầu | Tỷ lệ phần trăm các yêu cầu được giải quyết dứt điểm ngay tại lần liên hệ đầu tiên. |
| **Entity Relationship Diagram (ERD)** | Sơ đồ thực thể quan hệ | Sơ đồ biểu diễn các thực thể dữ liệu nghiệp vụ và mối quan hệ giữa chúng. |
| **Data Dictionary** | Từ điển dữ liệu | Bảng đặc tả các thuộc tính của thực thể (tên trường, kiểu dữ liệu, bắt buộc, quy tắc). |
| **Data Mapping** | Ánh xạ dữ liệu | Bảng định nghĩa tương ứng giữa dữ liệu nguồn và dữ liệu đích trong tích hợp API hoặc di chuyển dữ liệu. |
| **System Context Diagram**| Sơ đồ ngữ cảnh hệ thống | Sơ đồ biểu diễn hệ thống trung tâm và các luồng thông tin kết nối với các hệ thống ngoại vi. |
