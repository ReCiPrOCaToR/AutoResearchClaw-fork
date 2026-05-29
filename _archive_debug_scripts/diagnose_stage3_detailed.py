"""Diagnose why Stage 3 failed."""
from pathlib import Path
import traceback

workspace = Path(r"D:\My_Project\AutoResearchClaw")

# Check all logs
logs_dir = workspace / "logs"
print("=== All log files ===")
for log in sorted(logs_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True):
    print(f"\n--- {log.name} ---")
    try:
        lines = log.read_text(encoding='utf-8', errors='replace').split('\n')
        print(f"Lines: {len(lines)}")
        for line in lines:
            print(f"  {line}")
    except Exception as e:
        print(f"  Error reading: {e}")

# Check stage-03 directory
stage3 = workspace / "artifacts" / "rc-20260413-061550-03dfbf" / "stage-03"
print(f"\n=== Stage-03 directory ===")
if stage3.exists():
    items = list(stage3.iterdir())
    print(f"Items: {len(items)}")
    for item in items:
        print(f"  {item.name} (is_dir={item.is_dir()})")
else:
    print("Directory doesn't exist")

# Check for any .stderr files
artifacts = workspace / "artifacts" / "rc-20260413-061550-03dfbf"
print(f"\n=== All files in run directory ===")
for f in sorted(artifacts.rglob("*")):
    if f.is_file():
        size = f.stat().st_size
        print(f"  {f.relative_to(artifacts)} ({size} bytes)")
        if size < 1000 and (f.suffix in ('.json', '.txt', '.log', '.stderr', '.stdout')):
            try:
                content = f.read_text()
                if 'error' in content.lower() or 'exception' in content.lower():
                    print(f"    *** CONTAINS ERROR ***")
                    print(f"    {content[:500]}")
            except: pass

print("\n=== Done ===")
