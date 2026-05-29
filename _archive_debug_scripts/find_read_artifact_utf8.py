# Find _read_prior_artifact definition with encoding check
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for _read_prior_artifact ===")
found = False
for i, line in enumerate(lines):
    if 'def _read_prior_artifact' in line:
        print(f"Found at line {i+1}")
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+100, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
            if 'read_text' in cur_line or 'open(' in cur_line:
                print(f"      ^^^ FILE READ OPERATION")
        found = True
        break

if not found:
    print("Not found directly. Searching for any read_prior_artifact...")
    for i, line in enumerate(lines):
        if 'read_prior_artifact' in line:
            print(f"  Line {i+1}: {line.strip()[:200]}")
