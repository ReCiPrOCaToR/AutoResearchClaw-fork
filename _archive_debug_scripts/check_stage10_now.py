"""Wait for Stage 10 to start and monitor progress."""
import time
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")
artifacts = workspace / "artifacts"

print("=== Monitoring Stage 10 Progress ===\n")

# Find latest run
runs = sorted(artifacts.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
if not runs:
    print("No runs found yet. Waiting...")
    time.sleep(10)
    runs = sorted(artifacts.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)

if runs:
    latest_run = runs[0]
    print(f"Latest run: {latest_run.name}")
    
    # Check stages completed
    stage_dirs = sorted([d for d in latest_run.iterdir() if d.is_dir()], key=lambda x: x.name)
    print(f"Stages completed: {len(stage_dirs)}")
    for stage in stage_dirs:
        files = list(stage.iterdir())
        print(f"  {stage.name}: {len(files)} files")
    
    # Specifically check stage-10
    stage10 = latest_run / "stage-10"
    if stage10.exists():
        print(f"\n✓ Stage-10 directory exists")
        files = list(stage10.iterdir())
        print(f"  Files: {[f.name for f in files]}")
        # Check for code generation outputs
        exp_dir = stage10 / "experiment"
        if exp_dir.exists():
            code_files = list(exp_dir.glob("*.py"))
            print(f"  Code files: {len(code_files)}")
            if code_files:
                print(f"  ✓ Code generation succeeded!")
                for f in code_files[:5]:
                    print(f"    {f.name} ({f.stat().st_size} bytes)")
        else:
            print(f"  ⚠ No experiment/ directory yet")
    else:
        print(f"\n✗ Stage-10 not started yet")
else:
    print("Still no runs found")

print("\n--- tail of pipeline log ---")
log_file = workspace / "logs" / "pipeline-fixed-20260413-141550.log"
if log_file.exists():
    lines = log_file.read_text(encoding='utf-8', errors='replace').split('\n')
    for line in lines[-20:]:
        print(f"  {line}")
