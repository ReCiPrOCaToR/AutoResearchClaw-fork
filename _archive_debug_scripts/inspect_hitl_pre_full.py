# Find _run_hitl_pre_stage full code
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _run_hitl_pre_stage ===")
for i, line in enumerate(lines):
    if 'def _run_hitl_pre_stage' in line:
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+120, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Check what _get_hitl_session does ===")
# Find _get_hitl_session
for i, line in enumerate(lines):
    if 'def _get_hitl_session' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+40, len(lines))):
            print(f"  {j+1}: {lines[j]}")
        break
