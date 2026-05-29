# Find _read_prior_artifact implementation
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _read_prior_artifact ===")
for i, line in enumerate(lines):
    if 'def _read_prior_artifact' in line:
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+80, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Check for read_text/open usage ===")
for i, line in enumerate(lines):
    if ('read_text(' in line or 'open(' in line) and '_read_prior_artifact' not in line:
        if 'encoding' in line.lower():
            print(f"Line {i+1}: {line.strip()}")
