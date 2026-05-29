# Read full _topic.py to understand Stage 3 execution
from pathlib import Path

topic_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_topic.py")
content = topic_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _execute_problem_decompose function (full) ===")
in_func = False
indent_level = 0
for i, line in enumerate(lines):
    if '_execute_problem_decompose' in line and 'def' in line:
        in_func = True
        indent_level = len(line) - len(line.lstrip())
    if in_func:
        print(f"  {i+1}: {line}")
        # Check if we've left the function
        if line.strip() and not line.startswith(' ' * (indent_level + 1)) and i > 115 and not line.strip().startswith('#'):
            if len(line) - len(line.lstrip()) <= indent_level:
                break

print("\n=== Imports at top of _topic.py ===")
for i, line in enumerate(lines[:50]):
    print(f"  {i+1}: {line}")
