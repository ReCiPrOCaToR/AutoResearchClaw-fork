# Find Stage 3 executor mapping
from pathlib import Path

stages_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stages.py")
try:
    content = stages_file.read_text(encoding='utf-8', errors='ignore')
except:
    content = stages_file.read_text(encoding='latin-1', errors='ignore')

lines = content.split('\n')
print("=== Stage to executor mapping ===")
for i, line in enumerate(lines):
    if '_STAGE_EXECUTORS' in line or 'executor' in line.lower():
        if line.strip():
            print(f"Line {i+1}: {line.strip()}")
            # Show next lines if it's a multi-line dict
            if line.strip().endswith('{') or '=' in line and '{' in line:
                for j in range(i+1, min(i+20, len(lines))):
                    if lines[j].strip() and not lines[j].startswith(' ' * 4):
                        break
                    print(f"  {j+1}: {lines[j]}")

print("\n=== Looking for Stage.PROBLEM_DECOMPOSE or Stage(3) ===")
for i, line in enumerate(lines):
    if 'PROBLEM_DECOMPOSE' in line or ('Stage(3)' in line or 'Stage.ANALYSIS' in line):
        print(f"Line {i+1}: {line.strip()}")
