# Read all logs to find the actual error
from pathlib import Path

logs_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
print("=== All log files ===")
for log in sorted(logs_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True):
    print(f"\n--- {log.name} ---")
    lines = log.read_text(encoding='utf-8', errors='replace').split('\n')
    print(f"Lines: {len(lines)}")
    # Show full content
    for line in lines:
        print(f"  {line}")
