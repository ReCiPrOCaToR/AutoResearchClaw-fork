import json
from pathlib import Path

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
decision = run / "stage-10" / "decision.json"

if decision.exists():
    data = json.loads(decision.read_text())
    print("=== DECISION.JSON ===")
    print(json.dumps(data, indent=2))

health = run / "stage-10" / "stage_health.json"
if health.exists():
    h = json.loads(health.read_text())
    print("\n=== STAGE_HEALTH.JSON ===")
    print(json.dumps(h, indent=2))

# Check logs in main directory
log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
if log_dir.exists():
    logs = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if logs:
        log = logs[0]
        content = log.read_text(encoding='utf-8', errors='replace')
        print(f"\n=== LATEST LOG ({log.name}) ===")
        print(content[-3000:])
