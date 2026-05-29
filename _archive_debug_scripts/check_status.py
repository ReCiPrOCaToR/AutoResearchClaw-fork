"""Check pipeline status - latest run and stage progress."""
import subprocess, sys
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")
artifacts = workspace / "artifacts"

# Find all runs
runs = sorted(artifacts.glob("rc-*"), key=lambda p: p.stat().st_mtime, reverse=True)
print(f"Found {len(runs)} runs")

if runs:
    latest = runs[0]
    print(f"\nLatest: {latest.name}")
    
    stages = sorted([d for d in latest.iterdir() if d.is_dir()], key=lambda x: x.name)
    print(f"Stages: {[s.name for s in stages]}")
    
    stage10 = latest / "stage-10"
    if stage10.exists():
        files = list(stage10.iterdir())
        print(f"\n✓ Stage-10 exists with {len(files)} files:")
        for f in sorted(files, key=lambda x: x.stat().st_mtime, reverse=True):
            size = f.stat().st_size
            print(f"  {f.name} ({size} bytes)")
            if f.is_file() and size < 2000:
                try:
                    print(f"    Content: {f.read_text()[:200]}")
                except: pass
    else:
        print("\n✗ Stage-10 not started yet")
        print(f"  Stages so far: {[s.name for s in stages]}")
else:
    print("No runs found")

# Also check running processes
print("\n=== Running Python processes ===")
result = subprocess.run(
    ['tasklist', '/FI', 'IMAGENAME eq python.exe', '/FO', 'CSV'],
    capture_output=True, text=True
)
for line in result.stdout.strip().split('\n')[1:]:
    parts = line.strip('"').split('","')
    if len(parts) >= 3:
        print(f"  PID: {parts[1]}  Mem: {parts[4]}")
