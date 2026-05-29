import subprocess
import sys

# Check process tree to see if child processes exist
result = subprocess.run(
    [sys.executable, "-c", "import psutil, os; p = psutil.Process(30852); print(f'PID: {p.pid}'); print(f'Status: {p.status()}'); print(f'CPU%: {p.cpu_percent(interval=0.5)}'); print(f'Memory: {p.memory_info().rss / 1024**2:.1f} MB'); children = p.children(recursive=True); print(f'Children: {len(children)}'); [print(f'  Child PID {c.pid}: {c.status()}') for c in children]"],
    capture_output=True, text=True, cwd=r"D:\My_Project\AutoResearchClaw"
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[:300])
