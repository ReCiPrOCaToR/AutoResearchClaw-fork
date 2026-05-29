from pathlib import Path

log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
if log_dir.exists():
    logs = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Found {len(logs)} log files")
    for log in logs[:3]:
        print(f"\n=== {log.name} ===")
        print(f"Size: {log.stat().st_size} bytes")
        # Show last 20 lines
        lines = log.read_text(encoding='utf-8', errors='replace').split('\n')
        print('\n'.join(lines[-20:]))
else:
    print("No logs directory yet")
