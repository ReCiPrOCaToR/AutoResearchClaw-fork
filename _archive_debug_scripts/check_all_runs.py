from pathlib import Path
import json

root = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
runs = sorted(root.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)

for run in runs:
    print(f"\n{'='*70}")
    print(f"RUN: {run.name}")
    print(f"Modified: {run.stat().st_mtime}")

    # Check key files
    checkpoint = run / "checkpoint.json"
    summary = run / "pipeline_summary.json"
    heartbeat = run / "heartbeat.json"
    deliverables = run / "deliverables"

    if checkpoint.exists():
        try:
            data = json.loads(checkpoint.read_text())
            print(f"Checkpoint: stage={data.get('stage_id', '?')} status={data.get('status', '?')}")
        except:
            print("Checkpoint: exists but unreadable")
    else:
        print("Checkpoint: not found")

    if summary.exists():
        try:
            data = json.loads(summary.read_text())
            stages = data.get('stages', [])
            print(f"Summary: {len(stages)} stages")
            completed = sum(1 for s in stages if s.get('status') == 'completed')
            failed = sum(1 for s in stages if s.get('status') == 'failed')
            print(f"  Completed: {completed}, Failed: {failed}")
        except:
            print("Summary: exists but unreadable")
    else:
        print("Summary: not found")

    if deliverables.exists():
        files = list(deliverables.iterdir())
        print(f"Deliverables: {len(files)} files")
        for f in files[:8]:
            print(f"  - {f.name}")
    else:
        print("Deliverables: not found")
