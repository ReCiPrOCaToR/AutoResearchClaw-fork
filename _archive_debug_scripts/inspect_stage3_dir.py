# Check stage-03 directory with all files including hidden
from pathlib import Path

stage3 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-03")
print(f"Stage-03 exists: {stage3.exists()}")
if stage3.exists():
    print(f"Contents (all):")
    for item in sorted(stage3.iterdir()):
        print(f"  {item.name}  size={item.stat().st_size}  is_dir={item.is_dir()}")
        # Read if small
        if item.is_file() and item.stat().st_size < 2000:
            try:
                content = item.read_text()
                print(f"    Content: {repr(content[:200])}")
            except Exception as e:
                print(f"    Error: {e}")

# Also check parent run directory for any error logs
run_dir = stage3.parent
print(f"\n=== Run directory root files ===")
for f in sorted(run_dir.iterdir()):
    print(f"  {f.name}  ({'dir' if f.is_dir() else 'file'})")
