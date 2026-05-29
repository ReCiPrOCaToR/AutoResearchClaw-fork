# Find _STAGE_EXECUTORS registration in executor.py
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for _STAGE_EXECUTORS ===")
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+200, len(lines))):
            if j < len(lines):
                print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Looking for Stage.PROBLEM_DECOMPOSE ===")
for i, line in enumerate(lines):
    if 'PROBLEM_DECOMPOSE' in line or 'Stage.PROBLEM' in line:
        print(f"Line {i+1}: {line.strip()}")

print("\n=== Looking for @stage decorator or registry ===")
for i, line in enumerate(lines):
    if '@stage' in line.lower() or 'register' in line.lower() or 'STAGE_EXECUTORS' in line.upper():
        print(f"Line {i+1}: {line.strip()}")
