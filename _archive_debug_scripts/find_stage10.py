from pathlib import Path
import re

root = Path(r"D:\My_Project\AutoResearchClaw")
# Search for code_generation stage
for f in root.rglob("*.py"):
    if "code_generation" in f.name.lower() or "stage-10" in str(f).lower():
        print(f"Found: {f.relative_to(root)}")

# Check stages directory
stages_dir = root / "researchclaw" / "stages"
if stages_dir.exists():
    print(f"\nStages directory: {stages_dir}")
    for f in sorted(stages_dir.iterdir()):
        print(f"  {f.name}")
