"""Monitor pipeline progress - check stage-10 status."""
import time
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")
run_id = "rc-20260413-" + time.strftime("%y%m%d-%H%M%S")  # Will need actual run ID

# Wait a bit then check artifacts
print("Waiting 10s for pipeline to progress...")
time.sleep(10)

# List recent run directories
artifacts = workspace / "artifacts"
runs = sorted(artifacts.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
print(f"\nRecent runs:")
for run in runs[:5]:
    if run.is_dir():
        stage_dirs = sorted(run.iterdir())
        print(f"  {run.name}: {len(stage_dirs)} stage dirs")
        # Check stage-10 if exists
        stage10 = run / "stage-10"
        if stage10.exists():
            files = list(stage10.iterdir())
            print(f"    stage-10: {len(files)} files")
            for f in files:
                print(f"      {f.name} ({f.stat().st_size} bytes)")

print("\n✓ Check complete.")
