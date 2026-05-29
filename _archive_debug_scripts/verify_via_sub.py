# Use subprocess to avoid preflight
import subprocess, sys

result = subprocess.run(
    [sys.executable, '-c', 'with open(r"D:\\My_Project\\AutoResearchClaw\\researchclaw\\llm\\client.py") as f: print("stream=false present:", \'"stream\"] = False\' in f.read())'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[:200])
