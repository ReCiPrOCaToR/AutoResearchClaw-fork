# List all stage directories in the latest run
from pathlib import Path

artifacts = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
runs = sorted(artifacts.glob("rc-*"), key=lambda p: p.stat().st_mtime, reverse=True)

if runs:
    latest = runs[0]
    print(f"Latest run: {latest.name}")
    print(f"All items:")
    for item in sorted(latest.iterdir()):
        if item.is_dir():
            sub_items = list(item.iterdir())
            print(f"  <DIR> {item.name}/  ({len(sub_items)} items)")
        else:
            print(f"  {item.name} ({item.stat().st_size} bytes)")
else:
    print("No runs")

# Also check for .stderr or .stdout files
print("\n--- Checking for error files ---")
for run in runs[:3]:
    for f in run.rglob("*.stderr"):
        print(f"  {f.relative_to(artifacts)}")
    for f in run.rglob("*.stdout"):
        print(f"  {f.relative_to(artifacts)}")
