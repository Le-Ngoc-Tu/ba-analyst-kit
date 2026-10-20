#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Phase 1: Deep Research & Knowledge Extraction
Author: Senior AI Coding Agent
Standard: Senior Engineering Playbook (Verification-Driven & Build the Lever)
"""

import sys
from pathlib import Path

# Configure UTF-8 encoding for Windows stdout
sys.stdout.reconfigure(encoding='utf-8')

REQUIRED_DOCS = [
    ("01_SCOPE_STATEMENT_DEEP_DIVE.md", 2500, ["Project Overview", "Expected Benefits", "Capabilities", "Mermaid"]),
    ("02_BUSINESS_PROCESS_DEEP_DIVE.md", 2500, ["Entry Criteria", "Inputs", "Outputs", "Exit Criteria", "Mermaid"]),
    ("03_USE_CASE_SPEC_DEEP_DIVE.md", 2500, ["Basic Flow", "Alternate", "Exception", "Gherkin", "Scenario"]),
    ("04_REQUIREMENTS_CHECKLIST_DEEP_DIVE.md", 2500, ["Scope of Service", "Triage & Routing", "Addressing Requests", "Monitoring"]),
    ("05_BA_METHODOLOGY_AND_SKILLS_ASSESSMENT.md", 2500, ["Get Oriented", "Discover Business Objectives", "Define Scope", "Novice"]),
    ("06_BILINGUAL_BA_GLOSSARY.md", 2500, ["Scope Creep", "Happy Path", "Swimlane", "Acceptance Criteria"]),
    ("07_VIETNAM_BA_ECOSYSTEM_AND_REGULATIONS.md", 2500, ["bảo vệ dữ liệu cá nhân", "sinh trắc học", "chữ ký số", "thể thức văn bản"]),
    ("08_COMMON_USE_CASES_COMPREHENSIVE_CATALOG.md", 2500, ["UC-AUTH-01", "VietQR", "eKYC", "Audit Trail", "Gherkin"]),
]

def verify_phase1():
    base_dir = Path(__file__).resolve().parent.parent / "docs" / "research"
    print(f"=== VERIFYING PHASE 1 KNOWLEDGE ARTIFACTS IN: {base_dir} ===")
    
    if not base_dir.exists():
        print(f"[FAIL] Directory does not exist: {base_dir}")
        return 1

    total_bytes = 0
    passed_count = 0

    for filename, min_size, required_keywords in REQUIRED_DOCS:
        file_path = base_dir / filename
        if not file_path.exists():
            print(f"[FAIL] Missing file: {filename}")
            continue

        size = file_path.stat().st_size
        total_bytes += size

        if size < min_size:
            print(f"[FAIL] File too small ({size} < {min_size} bytes): {filename}")
            continue

        content = file_path.read_text(encoding="utf-8")
        missing_keywords = [kw for kw in required_keywords if kw.lower() not in content.lower()]
        
        if missing_keywords:
            print(f"[FAIL] File {filename} missing required keywords: {missing_keywords}")
            continue

        print(f"[PASS] {filename:<45} | Size: {size:>6} bytes | Keywords Verified")
        passed_count += 1

    print("-" * 75)
    print(f"Total Verified Documents: {passed_count}/{len(REQUIRED_DOCS)}")
    print(f"Total Knowledge Corpus Size: {total_bytes:,} bytes")

    if passed_count == len(REQUIRED_DOCS):
        print(">>> ALL PHASE 1 ARTIFACTS VERIFIED: EXIT CODE 0 <<<")
        return 0
    else:
        print(">>> SOME CHECKS FAILED: EXIT CODE 1 <<<")
        return 1

if __name__ == "__main__":
    sys.exit(verify_phase1())
