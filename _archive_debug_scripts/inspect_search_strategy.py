"""Check what _execute_search_strategy does with problem_tree."""
from pathlib import Path

lit_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_literature.py")
content = lit_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _execute_search_strategy function ===")
in_func = False
for i, line in enumerate(lines):
    if 'def _execute_search_strategy' in line:
        in_func = True
        indent = len(line) - len(line.lstrip())
    if in_func:
        print(f"  {i+1}: {line}")
        if line.strip() and not line.startswith(' ' * (indent + 1)) and i > 65:
            if not line.strip().startswith('#'):
                break

print("\n=== Operations on problem_tree variable ===")
for i, line in enumerate(lines):
    if 'problem_tree' in line and 'def ' not in line:
        print(f"Line {i+1}: {line.strip()}")
