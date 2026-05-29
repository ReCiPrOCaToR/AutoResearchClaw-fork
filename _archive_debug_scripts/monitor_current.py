from pathlib import Path
import json
import time

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")

print(f"=== Monitoring {run.name} ===\n")

# Check checkpoint
ckpt = json.loads((run / "checkpoint.json").read_text())
print(f"Last completed: Stage {ckpt.get('last_completed_stage','?')} - {ckpt.get('last_completed_name','?')}")
print(f"Timestamp: {ckpt.get('timestamp','?')}\n")

# List stage dirs
stages = sorted([d for d in run.iterdir() if d.is_dir() and d.name.startswith('stage-')])
print(f"Stages found: {len(stages)}")
for stage in stages:
    files = list(stage.iterdir())
    print(f"  {stage.name}: {len(files)} files")
    health = stage / "stage_health.json"
    if health.exists():
        h = json.loads(health.read_text())
        print(f"    status={h.get('status')}, duration={h.get('duration_sec',0):.1f}s, error={h.get('error')}")
    decision = stage / "decision.json"
    if decision.exists():
        d = json.loads(decision.read_text())
        print(f"    decision={d.get('decision','?')}")

# Show latest log lines if any
log_dir = Path(r"D:\My_Project\AutoResearchClaw\logs")
if log_dir.exists():
    logs = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if logs:
        log = logs[0]
        lines = log.read_text(encoding='utf-8', errors='replace').split('\n')
        print(f"\nLog ({log.name}): {len(lines)} lines total")
        print("Last 10 lines:")
        for line in lines[-10:]:
            print(f"  {line}")
