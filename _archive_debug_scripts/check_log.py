from pathlib import Path

log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
if log_dir.exists():
    logs = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if logs:
        log = logs[0]
        content = log.read_text(encoding='utf-8', errors='replace')
        lines = content.split('\n')
        print(f"Log: {log.name} ({len(lines)} lines, {log.stat().st_size} bytes)")
        # Find last non-empty line
        non_empty = [l for l in lines if l.strip()]
        if non_empty:
            print(f"\nLast line: {non_empty[-1][:150]}")
            print(f"\nLast 5 non-empty lines:")
            for line in non_empty[-5:]:
                print(f"  {line[:150]}")
        # Search for stage transitions
        stage_starts = [l for l in lines if 'stage' in l.lower() and ('start' in l.lower() or 'begin' in l.lower())]
        if stage_starts:
            print(f"\nRecent stage starts:")
            for s in stage_starts[-5:]:
                print(f"  {s[:120]}")
    else:
        print("No logs yet")
else:
    print("No logs dir")
