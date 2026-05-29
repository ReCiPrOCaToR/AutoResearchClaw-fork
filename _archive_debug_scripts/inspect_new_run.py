from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
print(f"Inspecting: {run.name}\n")

# List all files
all_files = list(run.rglob("*"))
all_files = [(f.relative_to(run), f.stat().st_size) for f in all_files if f.is_file()]
all_files.sort(key=lambda x: x[1], reverse=True)

print(f"Total files: {len(all_files)}")
for rel, size in all_files:
    print(f"  {size:>6}  {rel}")

# Check checkpoint
ckpt = run / "checkpoint.json"
if ckpt.exists():
    data = json.loads(ckpt.read_text())
    print(f"\nCheckpoint: stage {data.get('last_completed_stage','?')} - {data.get('last_completed_name','?')}")
    print(f"Timestamp: {data.get('timestamp','?')}")

# Check any stage directories
print("\nStage directories:")
stages = sorted([d for d in run.iterdir() if d.is_dir() and d.name.startswith('stage-')])
for stage in stages:
    files = list(stage.iterdir())
    print(f"  {stage.name}/ {len(files)} files")
    # Show stage health if exists
    health = stage / "stage_health.json"
    if health.exists():
        h = json.loads(health.read_text())
        print(f"    status: {h.get('status','?')}, duration: {h.get('duration_sec',0):.1f}s")
