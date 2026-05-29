# Check if pipeline is running and what stages completed
import subprocess, sys
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")

# Check for running Python processes with our script
result = subprocess.run(
    ['tasklist', '/FI', 'IMAGENAME eq python.exe', '/FO', 'CSV'],
    capture_output=True, text=True
)
python_procs = []
for line in result.stdout.strip().split('\n')[1:]:
    parts = line.strip('"').split('","')
    if len(parts) >= 3:
        pid = parts[1]
        mem = parts[4]
        python_procs.append((pid, mem))

print(f"Running Python processes: {len(python_procs)}")
for pid, mem in python_procs:
    print(f"  PID {pid} - {mem}")

# Check artifacts for latest run
artifacts = workspace / "artifacts"
runs = sorted(artifacts.glob("rc-*"), key=lambda p: p.stat().st_mtime, reverse=True)
if runs:
    latest = runs[0]
    print(f"\nLatest run: {latest.name}")
    stages = sorted([d for d in latest.iterdir() if d.is_dir()], key=lambda x: x.name)
    print(f"Stages completed: {[s.name for s in stages]}")
    
    stage10 = latest / "stage-10"
    if stage10.exists():
        files = list(stage10.iterdir())
        print(f"Stage-10 files: {[f.name for f in files]}")
        exp = stage10 / "experiment"
        if exp.exists():
            py_files = list(exp.glob("*.py"))
            print(f"Code files generated: {len(py_files)}")
            if py_files:
                print("✓ CODE GENERATION SUCCEEDED!")
                for f in py_files[:5]:
                    print(f"  {f.name} ({f.stat().st_size} bytes)")
            else:
                print("  (still running or no code yet)")
        else:
            print("  No experiment/ directory yet")
    else:
        print("Stage-10 not started")
else:
    print("No artifact runs found")
