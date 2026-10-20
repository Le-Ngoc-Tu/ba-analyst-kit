#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for BA Analyst Kit Skill Package
Standard: Senior Engineering Playbook (Verification-Driven & Build the Lever)
"""

import sys
import re
from pathlib import Path

# Configure UTF-8 encoding for Windows stdout
sys.stdout.reconfigure(encoding='utf-8')

def verify_skill():
    base_dir = Path(__file__).resolve().parent.parent / "skills" / "ba-analyst-kit"
    print(f"=== VERIFYING BA SKILL PACKAGE INTEGRITY IN: {base_dir} ===")

    if not base_dir.exists():
        print(f"[FAIL] Base directory does not exist: {base_dir}")
        return 1

    # 1. Verify SKILL.md
    skill_file = base_dir / "SKILL.md"
    if not skill_file.exists():
        print("[FAIL] Missing SKILL.md")
        return 1
    
    skill_text = skill_file.read_text(encoding="utf-8")
    if not skill_text.startswith("---") or "name: ba-analyst-kit" not in skill_text:
        print("[FAIL] SKILL.md missing valid YAML frontmatter")
        return 1
    print(f"[PASS] SKILL.md verified ({skill_file.stat().st_size:,} bytes, valid YAML frontmatter)")

    # 2. Verify 7 Templates
    templates = [
        "scope_statement_template.md",
        "business_process_template.md",
        "use_case_template.md",
        "elicitation_checklist_template.md",
        "vietnam_uat_signoff_template.md",
        "data_dictionary_template.md",
        "data_mapping_template.md"
    ]
    for t in templates:
        t_path = base_dir / "templates" / t
        if not t_path.exists() or t_path.stat().st_size < 1000:
            print(f"[FAIL] Invalid or missing template: {t}")
            return 1
        print(f"[PASS] Template verified: {t:<35} | {t_path.stat().st_size:>5} bytes")

    # 3. Verify 6 Workflows
    workflows = [
        "workflow_01_elicitation.md",
        "workflow_02_scope_definition.md",
        "workflow_03_process_modeling.md",
        "workflow_04_use_case_authoring.md",
        "workflow_05_quality_review.md",
        "workflow_06_vietnam_compliance_and_uat.md"
    ]
    for w in workflows:
        w_path = base_dir / "workflows" / w
        if not w_path.exists() or w_path.stat().st_size < 800:
            print(f"[FAIL] Invalid or missing workflow: {w}")
            return 1
        print(f"[PASS] Workflow verified: {w:<35} | {w_path.stat().st_size:>5} bytes")

    # 4. Verify Reference Files
    for ref_file in ["ba_glossary.md", "common_use_cases_library.md", "master_use_cases_catalog.md"]:
        ref_path = base_dir / "references" / ref_file
        if not ref_path.exists() or ref_path.stat().st_size < 1000:
            print(f"[FAIL] Invalid or missing references/{ref_file}")
            return 1
        print(f"[PASS] Reference verified: {ref_file:<35} | {ref_path.stat().st_size:,} bytes")

    # 5. Verify Internal Links in SKILL.md
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', skill_text)
    broken_links = 0
    for text, link in links:
        if link.startswith("file:///"):
            clean_path = link.replace("file:///", "").replace("/", "\\")
            if not Path(clean_path).exists():
                print(f"[FAIL] Broken link detected in SKILL.md: {link}")
                broken_links += 1
    
    if broken_links > 0:
        print(f"[FAIL] Found {broken_links} broken links!")
        return 1

    print("-" * 75)
    print(">>> ALL BA SKILL PACKAGE COMPONENTS VERIFIED: EXIT CODE 0 <<<")
    return 0

if __name__ == "__main__":
    sys.exit(verify_skill())
