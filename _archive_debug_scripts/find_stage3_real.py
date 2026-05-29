# Find the actual Stage 3 implementation
from pathlib import Path

pipeline_dir = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline")
stage_impls = pipeline_dir / "stage_impls"

print("=== All files in stage_impls ===")
for f in sorted(stage_impls.iterdir()):
    print(f"  {f.name}")

# Find stage mapping
stages_file = pipeline_dir / "stages.py"
if stages_file.exists():
    print(f"\n=== Stage 03 mapping ===")
    content = stages_file.read_text()
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'PROBLEM_DECOMPOSE' in line or '03' in line and 'Stage' in line:
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+3)
            for j in range(start, end):
                print(f"  {j+1}: {lines[j]}")

# Also check what _problem_decomposition might be named
print("\n=== Files containing 'problem' ===")
for f in stage_impls.iterdir():
    if 'problem' in f.name.lower():
        print(f"  {f.name}")
