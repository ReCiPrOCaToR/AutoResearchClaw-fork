from pathlib import Path
import json

# Check latest run (044520)
run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-044520-03dfbf")
print(f"Inspecting: {run.name}\n")

# List all files with sizes
all_files = list(run.rglob("*"))
all_files = [(f.relative_to(run), f.stat().st_size) for f in all_files if f.is_file()]
all_files.sort(key=lambda x: x[1], reverse=True)

print(f"Total files: {len(all_files)}")
for relpath, size in all_files[:20]:
    print(f"  {size:>8}  {relpath}")

# Read checkpoint if exists
ckpt = run / "checkpoint.json"
if ckpt.exists():
    data = json.loads(ckpt.read_text())
    print(f"\nCheckpoint: {json.dumps(data, indent=2)}")

# Read any error logs
errors = list(run.glob("*.log")) + list(run.glob("error*.txt"))
if errors:
    print("\nError logs found:")
    for err in errors:
        print(f"  {err.name}")
        print(err.read_text(encoding='utf-8', errors='replace')[:500])
