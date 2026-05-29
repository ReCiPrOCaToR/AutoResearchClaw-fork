import subprocess
import sys
import time

# Check if process is still alive
result = subprocess.run(
    [sys.executable, "-c", "import psutil; p = psutil.Process(30852); print(f'PID 30852 running: {p.is_running()}'); print(f'Status: {p.status()}'); print(f'CPU: {p.cpu_percent(interval=0.1)}%')"],
    capture_output=True, text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[:200])

# Also check for any artifacts being created
from pathlib import Path
artifacts = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
if artifacts.exists():
    runs = list(artifacts.glob("*"))
    print(f"Artifact dirs: {len(runs)}")
    for r in runs[-3:]:
        print(f"  {r.name}")
