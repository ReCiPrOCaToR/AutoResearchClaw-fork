# Find _get_hitl_session definition
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _get_hitl_session ===")
for i, line in enumerate(lines):
    if 'def _get_hitl_session' in line:
        for j in range(i, min(i+40, len(lines))):
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Check adapters usage ===")
# Find where adapters hitl is accessed
for i, line in enumerate(lines):
    if 'adapters.hitl' in line or 'adapters.message' in line or 'adapters.memory' in line:
        if 'def ' not in line:
            print(f"Line {i+1}: {line.strip()}")
