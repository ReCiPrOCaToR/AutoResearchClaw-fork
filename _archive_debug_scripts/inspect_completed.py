from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-043320-03dfbf")
deliverables = run / "deliverables"

print("=== DELIVERABLES ===")
if deliverables.exists():
    for f in sorted(deliverables.iterdir()):
        print(f"  {f.name} ({f.stat().st_size} bytes)")

print("\n=== CHECKPOINT ===")
ckpt = run / "checkpoint.json"
if ckpt.exists():
    data = json.loads(ckpt.read_text())
    print(f"Last stage: {data.get('last_stage', 'unknown')}")
    print(f"Status: {data.get('status', 'unknown')}")
    print(f"Timestamp: {data.get('timestamp', 'unknown')}")

print("\n=== PIPELINE SUMMARY ===")
summary = run / "pipeline_summary.json"
if summary.exists():
    data = json.loads(summary.read_text())
    stages = data.get('stages', [])
    print(f"Total stages: {len(stages)}")
    for s in stages[:10]:
        print(f"  {s.get('stage_id', '?')}: {s.get('name', '?')} [{s.get('status', '?')}]")

print("\n=== HEARTBEAT ===")
hb = run / "heartbeat.json"
if hb.exists():
    data = json.loads(hb.read_text())
    print(f"Last update: {data.get('last_update', '?')}")
    print(f"Stage: {data.get('current_stage', '?')}")

print("\n=== EVOLUTION/LESSONS ===")
lessons = run / "evolution" / "lessons.jsonl"
if lessons.exists():
    lines = lessons.read_text().strip().split('\n')
    print(f"Lessons captured: {len(lines)}")
    for line in lines[:3]:
        entry = json.loads(line)
        print(f"  - {entry.get('type', '?')} at {entry.get('stage', '?')}: {str(entry.get('message', ''))[:80]}")
