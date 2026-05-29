# Check what's in stage-03 directory and why it's empty
from pathlib import Path

stage3 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-03")
print(f"Stage-03 directory contents:")
if stage3.exists():
    for item in sorted(stage3.iterdir()):
        if item.is_dir():
            print(f"  <DIR> {item.name}")
            for sub in item.iterdir():
                print(f"    {sub.name} ({sub.stat().st_size} bytes)")
        else:
            print(f"  {item.name} ({item.stat().st_size} bytes)")
            if item.suffix in ('.json', '.txt', '.yaml'):
                try:
                    content = item.read_text()
                    print(f"    Content: {content[:300]}")
                except: pass
else:
    print("  Directory does not exist")

# Check logs for errors
log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
log_files = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
if log_files:
    latest = log_files[0]
    print(f"\n=== Log: {latest.name} ===")
    lines = latest.read_text(encoding='utf-8', errors='replace').split('\n')
    # Find ERROR or FAIL lines
    for line in lines[-50:]:
        if any(kw in line.lower() for kw in ['error', 'fail', 'exception', 'traceback']):
            print(f"  {line}")
