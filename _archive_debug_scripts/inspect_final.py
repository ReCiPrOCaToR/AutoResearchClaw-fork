from pathlib import Path
import json

# Check the latest run that just finished
runs = sorted(Path(r"D:\My_Project\AutoResearchClaw\artifacts").glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
run = runs[0]  # Most recent

print(f"Inspecting latest run: {run.name}\n")
print("="*70)

# Read all key files
files_to_check = {
    "checkpoint.json": "Checkpoint",
    "pipeline_summary.json": "Pipeline Summary",
    "heartbeat.json": "Heartbeat",
    "deliverables/manifest.json": "Manifest"
}

for file_path, label in files_to_check.items():
    full_path = run / file_path
    if full_path.exists():
        print(f"\n=== {label} ({file_path}) ===")
        try:
            data = json.loads(full_path.read_text())
            print(json.dumps(data, indent=2)[:1000])
        except Exception as e:
            raw = full_path.read_text()
            print(f"Raw ({len(raw)} chars): {raw[:500]}")
    else:
        print(f"\n=== {label}: NOT FOUND ===")

# List all deliverables
deliverables = run / "deliverables"
if deliverables.exists():
    print("\n\n=== DELIVERABLES ===")
    for f in sorted(deliverables.iterdir()):
        size = f.stat().st_size
        print(f"  [{size:>8} bytes] {f.name}")

# Look for any error logs or stage outputs
print("\n\n=== STAGE ARTIFACTS ===")
stage_dirs = sorted([d for d in run.iterdir() if d.is_dir() and d.name.startswith('stage-')])
for stage in stage_dirs[-5:]:  # Last 5 stages
    files = list(stage.iterdir())
    print(f"\n  {stage.name}/ ({len(files)} files):")
    for f in files[:5]:
        print(f"    {f.name}")
