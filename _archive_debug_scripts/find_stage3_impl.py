# Diagnose Stage 3 failure
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")

# 1. Find stage-03 implementation
stage_impls = workspace / "researchclaw" / "pipeline" / "stage_impls"
print("=== Stage implementation files ===")
for f in sorted(stage_impls.iterdir()):
    print(f"  {f.name}")

# 2. Find stage mapping
stages_py = workspace / "researchclaw" / "pipeline" / "stages.py"
print(f"\n=== stages.py (excerpt) ===")
content = stages_py.read_text()
lines = content.split('\n')
for i, line in enumerate(lines):
    if '03' in line or 'PROBLEM_DECOMPOSE' in line.upper():
        print(f"  Line {i+1}: {line}")

# 3. Check if stage-03 executor is defined
print(f"\n=== Stage 03 executor ===")
for i, line in enumerate(lines):
    if 'Stage.PROBLEM_DECOMPOSE' in line or 'PROBLEM_DECOMPOSE' in line:
        # Show context
        start = max(0, i-2)
        end = min(len(lines), i+5)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j]}")
