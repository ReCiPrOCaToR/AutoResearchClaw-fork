# Find _chat_with_prompt definition
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _chat_with_prompt ===")
for i, line in enumerate(lines):
    if 'def _chat_with_prompt' in line:
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+100, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
        break

print("\n=== Check exception handling ===")
# Search for try/except around llm.chat
for i, line in enumerate(lines):
    if 'llm.chat' in line or 'resp = ' in line:
        if i > 0 and 'try' in lines[i-1]:
            print(f"Line {i}: context around llm call:")
            for j in range(i-1, min(i+10, len(lines))):
                print(f"  {j+1}: {lines[j]}")
