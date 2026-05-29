from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
stage10 = run / "stage-10"

print("=== Stage 10 Detailed Inspection ===\n")

if stage10.exists():
    files = list(stage10.iterdir())
    print(f"Files in stage-10: {len(files)}")
    for f in sorted(files):
        print(f"\n--- {f.name} ---")
        content = f.read_text(encoding='utf-8', errors='replace')
        print(content[:2000])

# Check complexity analysis specifically
ca = stage10 / "complexity_analysis.json"
if ca.exists():
    print("\n=== COMPLEXITY ANALYSIS ===")
    print(json.dumps(json.loads(ca.read_text()), indent=2))

# Check if any code artifacts were generated
code_files = list(run.rglob("*.py")) + list(run.rglob("*.sh")) + list(run.rglob("*.R"))
print(f"\n=== CODE FILES ===")
print(f"Total code files: {len(code_files)}")
for cf in code_files:
    print(f"  {cf.relative_to(run)} ({cf.stat().st_size} bytes)")
