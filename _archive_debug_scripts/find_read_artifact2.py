# Search for _read_prior_artifact more broadly
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

# Find all function definitions
print("=== All function definitions in _helpers.py ===")
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('def ') and '_read' in line:
        print(f"  Line {i+1}: {stripped}")

# Also search for 'read_prior_artifact' anywhere
print("\n=== All occurrences of 'read_prior_artifact' ===")
for i, line in enumerate(lines):
    if 'read_prior_artifact' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")
