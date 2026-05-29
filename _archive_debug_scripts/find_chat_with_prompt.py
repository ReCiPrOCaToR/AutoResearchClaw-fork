# Search for _chat_with_prompt definition in _helpers.py
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== All function definitions in _helpers.py ===")
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('def ') and not stripped.startswith('def _'):
        # Private function
        func_name = stripped.split('(')[0].replace('def ', '')
        print(f"  Line {i+1}: {func_name}")
    elif stripped.startswith('def '):
        # Public function
        func_name = stripped.split('(')[0].replace('def ', '')
        print(f"  Line {i+1}: {func_name}")

print("\n=== Specifically searching for _chat_with_prompt ===")
for i, line in enumerate(lines):
    if '_chat_with_prompt' in line and 'def' in line:
        print(f"Found at line {i+1}")
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+80, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
