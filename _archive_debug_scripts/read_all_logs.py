# Read all pipeline logs
from pathlib import Path

logs_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
log_files = sorted(logs_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)

for log in log_files[:5]:
    print(f"\n=== {log.name} ===")
    lines = log.read_text(encoding='utf-8', errors='replace').split('\n')
    print(f"Lines: {len(lines)}")
    # Show everything
    for line in lines:
        print(f"  {line}")
