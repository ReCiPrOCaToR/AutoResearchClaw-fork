# Search for _read_prior_artifact definition and encoding
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for '_read_prior_artifact' ===")
found = False
for i, line in enumerate(lines):
    if 'def _read_prior_artifact' in line:
        print(f"Found at line {i+1}")
        # Show full function
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+100, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
        found = True
        break

if not found:
    print("Function not found directly. Checking if it's imported or has different name...")
    # Search for any function that reads prior artifacts
    for i, line in enumerate(lines):
        if 'def ' in line and ('read' in line.lower() or 'prior' in line.lower() or 'artifact' in line.lower()):
            print(f"  Possible: line {i+1}: {line.strip()}")

# Check file reading patterns in the file
print("\n=== File read patterns in _helpers.py ===")
for i, line in enumerate(lines):
    if ('Path(' in line or '.read_text(' in line or '.open(' in line) and 'encoding' in line:
        print(f"Line {i+1}: {line.strip()}")
