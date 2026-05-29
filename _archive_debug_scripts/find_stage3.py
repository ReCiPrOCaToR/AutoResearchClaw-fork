# Find stage-03 implementation
from pathlib import Path

pipeline_dir = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline")
stage_impls = pipeline_dir / "stage_impls"

print("=== Files in stage_impls ===")
for f in sorted(stage_impls.iterdir()):
    print(f"  {f.name}")

# Find stage-03 mapping
stages_file = pipeline_dir / "stages.py"
if stages_file.exists():
    print(f"\n=== stages.py ===")
    content = stages_file.read_text()
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '03' in line or 'PROBLEM_DECOMPOSE' in line or 'problem_decompose' in line.lower():
            print(f"Line {i+1}: {line}")
