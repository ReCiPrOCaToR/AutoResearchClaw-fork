import time
from pathlib import Path

log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
if log_dir.exists():
    logs = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if logs:
        latest = logs[0]
        print(f"Latest log: {latest.name}")
        print(f"Size: {latest.stat().st_size} bytes")
        lines = latest.read_text(encoding='utf-8', errors='replace').split('\n')
        print(f"Lines: {len(lines)}")
        if len(lines) > 10:
            print("\nLast 10 lines:")
            for line in lines[-10:]:
                print(f"  {line}")
        else:
            print("\nFull content:")
            for line in lines:
                print(f"  {line}")
    else:
        print("No logs yet")
else:
    print("No logs directory")

# Check artifacts for new run
artifacts = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
if artifacts.exists():
    runs = sorted(artifacts.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"\nArtifact runs: {len(runs)}")
    for r in runs[:3]:
        files = list(r.rglob("*"))
        print(f"  {r.name}: {len(files)} files")
