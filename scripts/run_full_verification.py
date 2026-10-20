#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Verification Runner for Entire BA Skill Kit & Knowledge Base
Standard: Senior Engineering Playbook (Verification-Driven & Build the Lever)
"""

import sys
import subprocess
from pathlib import Path

# Configure UTF-8 encoding for Windows stdout
sys.stdout.reconfigure(encoding='utf-8')

SCRIPTS = [
    ("Phase 1: Knowledge Corpus Verification", "scripts/verify_phase1_knowledge.py"),
    ("Phase 2 & 3: BA Skill Package Integrity", "scripts/verify_skill_package.py"),
    ("Phase 4: Sample Project Deliverables Validation", "scripts/validate_ba_deliverables.py"),
    ("Phase 5: Live Demonstration Validation (FIN-09)", "scripts/verify_demonstration.py"),
    ("Phase 6: Multi-Agent Cross-Validation (ECOMM-11)", "scripts/verify_ecomm11_qc.py"),
]

def run_all():
    base_dir = Path(__file__).resolve().parent.parent
    print("=" * 80)
    print(" MASTER VERIFICATION RUNNER — BA AGENT SKILLS KIT")
    print(" Standard: Senior Engineering & Planning Playbooks")
    print("=" * 80)

    all_passed = True
    for name, script in SCRIPTS:
        print(f"\n>>> RUNNING: {name} ({script})")
        full_path = base_dir / script
        res = subprocess.run([sys.executable, str(full_path)], cwd=str(base_dir))
        if res.returncode != 0:
            print(f"[FAIL] {name} exited with code {res.returncode}")
            all_passed = False
            break
        print(f"[SUCCESS] {name} passed with Exit Code 0.")

    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 ALL GATES AND VERIFICATION SUITES PASSED: 100% GREEN (EXIT CODE 0)")
        print("=" * 80)
        return 0
    else:
        print("❌ ONE OR MORE SUITES FAILED")
        print("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(run_all())
