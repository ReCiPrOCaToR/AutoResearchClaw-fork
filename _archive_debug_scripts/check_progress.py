from pathlib import Path
import json
import time

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")

stages = sorted([d for d in run.iterdir() if d.is_dir() and d.name.startswith('stage-')])
print(f"[{time.strftime('%H:%M:%S')}] Checking {len(stages)} stages")

for s in stages:
    health = s / "stage_health.json"
    if health.exists():
        h = json.loads(health.read_text())
        print(f"  {s.name}: {h.get('status','?')}, {h.get('duration_sec',0):.1f}s")
    else:
        print(f"  {s.name}: running")

# Show checkpoint
ckpt = json.loads((run / "checkpoint.json").read_text())
print(f"\nCheckpoint: Stage {ckpt.get('last_completed_stage','?')} - {ckpt.get('last_completed_name','?')}")
print(f"Time: {ckpt.get('timestamp','?')}")

# Count files
total = len(list(run.rglob("*")))
print(f"Total files: {total}")
