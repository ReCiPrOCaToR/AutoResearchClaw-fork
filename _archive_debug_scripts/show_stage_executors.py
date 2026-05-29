# Find the _STAGE_EXECUTORS dict
from pathlib import Path

stages_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stages.py")
content = stages_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for _STAGE_EXECUTORS ===")
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line:
        print(f"Found at line {i+1}")
        # Print full dict
        for j in range(i, len(lines)):
            print(f"  {j+1}: {lines[j]}")
            if lines[j].strip() == '}':
                break
        break

# Also look for "Stage.ANALYSIS" or similar
print("\n=== Stage enum values ===")
for i, line in enumerate(lines):
    if 'class Stage' in line or 'enum' in line.lower():
        for j in range(i, min(i+30, len(lines))):
            print(f"  {j+1}: {lines[j]}")
        break
