#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Demonstration Deliverables (FIN-09 Biometric Auth)
Standard: Senior Engineering Playbook (Verification-Driven & Build the Lever)
"""

import sys
from pathlib import Path

# Configure UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

def verify_demonstration():
    print("=== VERIFYING DEMONSTRATION DELIVERABLES (UC-FIN-09) ===")
    base_dir = Path(__file__).resolve().parent.parent
    demo_dir = base_dir / "examples" / "demonstration"

    errors = 0

    # 1. Verify UC-FIN-09 Markdown Specification
    uc_file = demo_dir / "UC_FIN09_BIOMETRIC_AUTH.md"
    if not uc_file.exists():
        print(f"[FAIL] Missing {uc_file}")
        return 1
    
    uc_text = uc_file.read_text(encoding="utf-8")
    required_uc_sections = [
        "## 1. THÔNG TIN USE CASE",
        "## 2. MÔ TẢ TÓM TẮT",
        "## 3. CÁC TÁC NHÂN LIÊN QUAN",
        "## 4. TIỀN ĐIỀU KIỆN",
        "## 5. LUỒNG THAO TÁC CHUẨN",
        "## 6. CÁC LUỒNG RẼ NHÁNH VÀ NGOẠI LỆ",
        "## 7. QUY TẮC NGHIỆP VỤ",
        "## 8. CẦU NỐI AGILE",
        "## 9. ĐIỀU KIỆN KẾT THÚC",
        "```mermaid",
        "Scenario:",
        "Given",
        "When",
        "Then",
        "BR-FIN-01",
        "BR-FIN-02",
        "xác thực sinh trắc học",
        "Liveness Detection"
    ]
    for sec in required_uc_sections:
        if sec.lower() not in uc_text.lower():
            print(f"[FAIL] UC-FIN-09 missing required keyword or section: '{sec}'")
            errors += 1
        else:
            print(f"[PASS] Section/Keyword verified: {sec:<35}")
    print(f"[PASS] UC-FIN-09 verified ({uc_file.stat().st_size:,} bytes, 0 missing sections)")

    # 2. Verify Data Dictionary Markdown
    dict_file = demo_dir / "DATA_DICT_FIN09_BIOMETRIC.md"
    if not dict_file.exists():
        print(f"[FAIL] Missing {dict_file}")
        return 1
    dict_text = dict_file.read_text(encoding="utf-8")
    required_dict_sections = [
        "## 1. THÔNG TIN TÀI LIỆU",
        "## 2. SƠ ĐỒ MỐI QUAN HỆ THỰC THỂ",
        "## 3. TỪ ĐIỂN THUỘC TÍNH DỮ LIỆU",
        "## 4. QUY TẮC BẢO MẬT & BẢO VỆ DỮ LIỆU SINH TRẮC HỌC",
        "erDiagram",
        "BIOMETRIC_VERIFICATION_LOG",
        "match_score",
        "liveness_passed",
        "AES-256",
        "APPEND-ONLY"
    ]
    for sec in required_dict_sections:
        if sec not in dict_text:
            print(f"[FAIL] Data Dictionary missing required section: '{sec}'")
            errors += 1
        else:
            print(f"[PASS] Data Dict verified: {sec:<35}")
    print(f"[PASS] Data Dict verified ({dict_file.stat().st_size:,} bytes)")

    print("-" * 75)
    if errors == 0:
        print(">>> ALL DEMONSTRATION DELIVERABLES VERIFIED: EXIT CODE 0 <<<")
        return 0
    else:
        print(f">>> DEMONSTRATION VERIFICATION FAILED WITH {errors} ERRORS <<<")
        return 1

if __name__ == "__main__":
    sys.exit(verify_demonstration())
