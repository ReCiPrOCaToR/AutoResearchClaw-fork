from pathlib import Path
import subprocess

result = subprocess.run(
    ["find", "-name", "code_generation.py"],
    capture_output=True, text=True,
    cwd=r"D:\My_Project\AutoResearchClaw"
)
print(result.stdout[:2000])
print("STDERR:", result.stderr[:500])
