# Find _execute_problem_decompose definition in executor.py
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for _execute_problem_decompose ===")
for i, line in enumerate(lines):
    if '_execute_problem_decompose' in line and 'def' in line:
        print(f"Found at line {i+1}")
        # Show the full function
        indent_level = len(line) - len(line.lstrip())
        for j in range(i, min(i+200, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent_level and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Top of executor.py (imports section) ===")
for i, line in enumerate(lines[:50]):
    print(f"  {i+1}: {line}")
