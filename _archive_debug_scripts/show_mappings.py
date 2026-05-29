# Find _STAGE_EXECUTORS definition
from pathlib import Path

stages_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stages.py")
content = stages_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Full _STAGE_EXECUTORS mapping ===")
in_mapping = False
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line and '=' in line:
        in_mapping = True
    if in_mapping:
        print(f"{i+1}: {line}")
        if line.strip() == '}':
            break

print("\n=== NEXT_STAGE mapping ===")
for i, line in enumerate(lines):
    if 'NEXT_STAGE' in line and '=' in line:
        for j in range(i, min(i+20, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
