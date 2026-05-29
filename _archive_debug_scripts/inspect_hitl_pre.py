# Find _run_hitl_pre_stage definition
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _run_hitl_pre_stage function ===")
for i, line in enumerate(lines):
    if 'def _run_hitl_pre_stage' in line:
        # Show full function
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+100, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== What adapters are passed to execute_stage? ===")
# Find where execute_stage is called and what adapters are passed
for i, line in enumerate(lines):
    if 'execute_stage(' in line and 'def ' not in line:
        print(f"Call at line {i+1}:")
        start = max(0, i-3)
        end = min(len(lines), i+6)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")
