# Find _read_prior_artifact by scanning
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

# Search more carefully
for i, line in enumerate(lines):
    if '_read_prior_artifact' in line and 'def' in line:
        print(f"Found at line {i+1}")
        # Show full function
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+100, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Also search for 'def _read_prior_artifact' with different spacing ===")
for i, line in enumerate(lines):
    if 'read_prior_artifact' in line.lower() and 'def' in line.lower():
        print(f"Line {i+1}: {line.strip()}")
