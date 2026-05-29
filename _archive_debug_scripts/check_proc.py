import subprocess
import sys
import time

result = subprocess.run(
    [sys.executable, "-c", "import psutil; p = psutil.Process(15484); print(f'PID: {p.pid}'); print(f'Status: {p.status()}'); print(f'CPU: {p.cpu_percent(interval=0.5):.1f}%'); print(f'Memory: {p.memory_info().rss/1024**2:.1f} MB'); children = p.children(recursive=True); print(f'Children: {len(children)}'); [print(f'  PID {c.pid}: {c.status()}') for c in children]"],
    capture_output=True, text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[:200])

# Check artifact directory size
from pathlib import Path
run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
files = list(run.rglob("*"))
print(f"\nFiles in latest run: {len(files)}")
