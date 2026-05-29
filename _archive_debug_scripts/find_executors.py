# Find _STAGE_EXECUTORS mapping
from pathlib import Path

stages_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stages.py")
content = stages_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for _STAGE_EXECUTORS ===")
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line:
        print(f"Found at line {i+1}")
        # Show from this line to end of mapping
        for j in range(i, min(i+50, len(lines))):
            print(f"  {j+1}: {lines[j]}")
            if lines[j].strip() and j > i and not lines[j].startswith(' ' * 4) and not lines[j].startswith('\t'):
                if '}' in line or ')' in line:
                    break
        break

print("\n=== Alternatively, search for Stage(2) or Stage.PROBLEM_DECOMPOSE usage ===")
for i, line in enumerate(lines):
    if ('Stage(2)' in line or 'Stage.PROBLEM_DECOMPOSE' in line) and '=' in line:
        print(f"Line {i+1}: {line.strip()}")
