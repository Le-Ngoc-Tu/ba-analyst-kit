#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Specification & Wireframe Table Generator for Business Analysts
Standard: Senior Engineering Playbook (Build the Lever & Automation)
"""

import sys
import json
from pathlib import Path

# Configure UTF-8 encoding for Windows stdout
sys.stdout.reconfigure(encoding='utf-8')

VIETNAMESE_VALIDATION_RULES = {
    "phone_vn": {
        "regex": r"^0[3|5|7|8|9][0-9]{8}$",
        "description": "Số điện thoại di động Việt Nam 10 chữ số bắt đầu bằng 03, 05, 07, 08, 09",
        "error_msg": "Số điện thoại không đúng định dạng mạng di động Việt Nam (10 chữ số)"
    },
    "cccd_vn": {
        "regex": r"^[0-9]{12}$",
        "description": "Căn cước công dân gắn chip chuẩn 12 chữ số",
        "error_msg": "Số CCCD phải bao gồm đúng 12 chữ số"
    },
    "tax_id_vn": {
        "regex": r"^[0-9]{10}(-[0-9]{3})?$",
        "description": "Mã số thuế doanh nghiệp (10 số) hoặc chi nhánh (13 số)",
        "error_msg": "Mã số thuế không hợp lệ (gồm 10 hoặc 13 chữ số)"
    },
    "currency_vnd": {
        "description": "Số tiền Việt Nam Đồng (phân cách hàng nghìn bằng dấu chấm, không có số thập phân)",
        "error_msg": "Số tiền phải là số nguyên dương lớn hơn 0"
    }
}

def generate_ui_spec_markdown(screen_title, fields, description=""):
    """Generates a complete UI Specification section in Markdown."""
    md = []
    md.append(f"## ĐẶC TẢ GIAO DIỆN & MÀN HÌNH: {screen_title.upper()}")
    if description:
        md.append(f"> {description}\n")

    md.append("### 1. Bảng Chi Tiết Thành Phần Giao Diện (UI Component Matrix)\n")
    md.append("| STT | Tên Thành Phần (Label) | Kiểu Nhập (UI Type) | Bắt Buộc | Quy Tắc Ràng Buộc (Validation) | Thông Báo Lỗi Tiếng Việt |")
    md.append("| :---: | :--- | :---: | :---: | :--- | :--- |")

    for idx, f in enumerate(fields, 1):
        label = f.get("label", "")
        ui_type = f.get("type", "Text Input")
        required = "Có (**Required**)" if f.get("required", False) else "Không"
        rule = f.get("rule", "Không")
        error_msg = f.get("error_msg", "Vui lòng nhập trường này")
        md.append(f"| {idx} | **{label}** | `{ui_type}` | {required} | {rule} | *\"{error_msg}\"* |")

    md.append("\n### 2. Khung Bố Cục Trực Quan Phác Thảo (Ascii Wireframe Mockup)\n")
    md.append("```text")
    md.append("+----------------------------------------------------------------+")
    md.append(f"|  {screen_title.center(62)}  |")
    md.append("+----------------------------------------------------------------+")
    for f in fields:
        label = f.get("label", "")
        ui_type = f.get("type", "Text")
        req_mark = " (*)" if f.get("required", False) else ""
        if ui_type == "Button":
            md.append(f"|  [ {label.upper()} ]                                              |")
        elif ui_type in ["Dropdown", "Select"]:
            md.append(f"|  {label}{req_mark}: [ Vui lòng chọn ▼ ]                                 |")
        elif ui_type == "File Upload":
            md.append(f"|  {label}{req_mark}: [ Kéo và thả tệp ảnh/PDF vào đây ]                  |")
        else:
            md.append(f"|  {label}{req_mark}: [ ................................................ ] |")
    md.append("+----------------------------------------------------------------+")
    md.append("```\n")

    return "\n".join(md)

def run_sample():
    sample_fields = [
        {"label": "Họ và tên chủ xe", "type": "Text Input", "required": True, "rule": "Tối đa 100 ký tự", "error_msg": "Họ và tên không được để trống"},
        {"label": "Số CCCD", "type": "Text Input", "required": True, "rule": VIETNAMESE_VALIDATION_RULES["cccd_vn"]["description"], "error_msg": VIETNAMESE_VALIDATION_RULES["cccd_vn"]["error_msg"]},
        {"label": "Số điện thoại nhận OTP", "type": "Text Input", "required": True, "rule": VIETNAMESE_VALIDATION_RULES["phone_vn"]["description"], "error_msg": VIETNAMESE_VALIDATION_RULES["phone_vn"]["error_msg"]},
        {"label": "Loại tổn thất", "type": "Dropdown", "required": True, "rule": "Chọn 1 trong các giá trị danh mục", "error_msg": "Vui lòng chọn loại tổn thất"},
        {"label": "Ảnh chụp hiện trường", "type": "File Upload", "required": True, "rule": "Định dạng JPG/PNG, dung lượng <= 10MB", "error_msg": "Vui lòng chọn ảnh tổn thất rõ nét"},
        {"label": "Xác nhận gửi hồ sơ", "type": "Button", "required": False, "rule": "Kích hoạt khi toàn bộ form hợp lệ", "error_msg": ""}
    ]

    out_md = generate_ui_spec_markdown("Nộp Hồ Sơ Giám Định Trực Tuyến", sample_fields, "Màn hình dành cho khách hàng tự nộp hồ sơ giám định ban đầu qua Cổng thông tin web.")
    out_file = Path(__file__).resolve().parent.parent / "examples" / "claims_support_system" / "05_UI_SPEC_CLAIMS_FORM.md"
    out_file.write_text(out_md, encoding="utf-8")
    print(f"[SUCCESS] Generated UI Spec at: {out_file} ({out_file.stat().st_size:,} bytes)")
    return True

if __name__ == "__main__":
    run_sample()
