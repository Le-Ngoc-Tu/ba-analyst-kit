## ĐẶC TẢ GIAO DIỆN & MÀN HÌNH: NỘP HỒ SƠ GIÁM ĐỊNH TRỰC TUYẾN
> Màn hình dành cho khách hàng tự nộp hồ sơ giám định ban đầu qua Cổng thông tin web.

### 1. Bảng Chi Tiết Thành Phần Giao Diện (UI Component Matrix)

| STT | Tên Thành Phần (Label) | Kiểu Nhập (UI Type) | Bắt Buộc | Quy Tắc Ràng Buộc (Validation) | Thông Báo Lỗi Tiếng Việt |
| :---: | :--- | :---: | :---: | :--- | :--- |
| 1 | **Họ và tên chủ xe** | `Text Input` | Có (**Required**) | Tối đa 100 ký tự | *"Họ và tên không được để trống"* |
| 2 | **Số CCCD** | `Text Input` | Có (**Required**) | Căn cước công dân gắn chip chuẩn 12 chữ số | *"Số CCCD phải bao gồm đúng 12 chữ số"* |
| 3 | **Số điện thoại nhận OTP** | `Text Input` | Có (**Required**) | Số điện thoại di động Việt Nam 10 chữ số bắt đầu bằng 03, 05, 07, 08, 09 | *"Số điện thoại không đúng định dạng mạng di động Việt Nam (10 chữ số)"* |
| 4 | **Loại tổn thất** | `Dropdown` | Có (**Required**) | Chọn 1 trong các giá trị danh mục | *"Vui lòng chọn loại tổn thất"* |
| 5 | **Ảnh chụp hiện trường** | `File Upload` | Có (**Required**) | Định dạng JPG/PNG, dung lượng <= 10MB | *"Vui lòng chọn ảnh tổn thất rõ nét"* |
| 6 | **Xác nhận gửi hồ sơ** | `Button` | Không | Kích hoạt khi toàn bộ form hợp lệ | *""* |

### 2. Khung Bố Cục Trực Quan Phác Thảo (Ascii Wireframe Mockup)

```text
+----------------------------------------------------------------+
|                  Nộp Hồ Sơ Giám Định Trực Tuyến                  |
+----------------------------------------------------------------+
|  Họ và tên chủ xe (*): [ ................................................ ] |
|  Số CCCD (*): [ ................................................ ] |
|  Số điện thoại nhận OTP (*): [ ................................................ ] |
|  Loại tổn thất (*): [ Vui lòng chọn ▼ ]                                 |
|  Ảnh chụp hiện trường (*): [ Kéo và thả tệp ảnh/PDF vào đây ]                  |
|  [ XÁC NHẬN GỬI HỒ SƠ ]                                              |
+----------------------------------------------------------------+
```
