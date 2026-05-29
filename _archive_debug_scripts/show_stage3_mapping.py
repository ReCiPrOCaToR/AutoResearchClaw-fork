# Read the full stages.py to find Stage 3 executor
from pathlib import Path

stages_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stages.py")
content = stages_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

# Find Stage enum
print("=== Stage Enum ===")
for i, line in enumerate(lines):
    if 'class Stage' in line or (line.strip().startswith('TOPIC') or line.strip().startswith('PROBLEM')):
        print(f"  {i+1}: {line}")

print("\n=== _STAGE_EXECUTORS dict ===")
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line:
        # Print from here to closing brace
        brace_count = 0
        for j in range(i, len(lines)):
            line_content = lines[j]
            print(f"  {j+1}: {line_content}")
            brace_count += line_content.count('{') - line_content.count('}')
            if brace_count <= 0 and j > i:
                break
        break
