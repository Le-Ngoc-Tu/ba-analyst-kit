#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Script for BA Deliverables Example Implementation
Standard: Senior Engineering Playbook (Verification-Driven & Build the Lever)
"""

import sys
from pathlib import Path

# Configure UTF-8 encoding for Windows stdout
sys.stdout.reconfigure(encoding='utf-8')

DELIVERABLES = [
    ("01_SCOPE_STATEMENT_CLAIMS.md", 5000, ["Project Overview", "Expected Benefits", "Capabilities", "Mermaid", "Out of Scope"]),
    ("02_PROCESS_ONSITE_INSPECTION.md", 5000, ["Entry Criteria", "Inputs", "Outputs", "Exit Criteria", "Mermaid", "Business Rules"]),
    ("03_USE_CASE_UPLOAD_EVIDENCE.md", 5000, ["Basic Flow", "Alternate", "Exception", "Gherkin", "Scenario", "Mermaid"]),
    ("04_CHECKLIST_CLAIMS_SUPPORT.md", 4000, ["Scope of Service", "Triage & Routing", "Addressing Requests", "Monitoring", "Self-Service"]),
]

def validate_deliverables():
    base_dir = Path(__file__).resolve().parent.parent / "examples" / "claims_support_system"
    print(f"=== VALIDATING BA DELIVERABLES AT: {base_dir} ===")

    if not base_dir.exists():
        print(f"[FAIL] Directory does not exist: {base_dir}")
        return 1

    total_bytes = 0
    passed = 0

    for filename, min_size, keywords in DELIVERABLES:
        f_path = base_dir / filename
        if not f_path.exists():
            print(f"[FAIL] Missing deliverable: {filename}")
            continue

        size = f_path.stat().st_size
        total_bytes += size

        if size < min_size:
            print(f"[FAIL] File too small ({size} < {min_size} bytes): {filename}")
            continue

        text = f_path.read_text(encoding="utf-8")
        missing_kw = [kw for kw in keywords if kw.lower() not in text.lower()]
        if missing_kw:
            print(f"[FAIL] Deliverable {filename} missing keywords: {missing_kw}")
            continue

        print(f"[PASS] {filename:<38} | Size: {size:>6} bytes | Structure 100% Valid")
        passed += 1

    print("-" * 75)
    print(f"Total Verified Deliverables: {passed}/{len(DELIVERABLES)}")
    print(f"Total Example Project Size: {total_bytes:,} bytes")

    if passed == len(DELIVERABLES):
        print(">>> ALL DELIVERABLES VALIDATED SUCCESSFULLY: EXIT CODE 0 <<<")
        return 0
    else:
        print(">>> VALIDATION FAILED: EXIT CODE 1 <<<")
        return 1

if __name__ == "__main__":
    sys.exit(validate_deliverables())
