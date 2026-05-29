# Check execute_stage try block range
from pathlib import Path

executor_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py")
content = executor_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== execute_stage function structure ===")
in_func = False
try_start = None
try_end = None
finally_start = None

for i, line in enumerate(lines):
    if 'def execute_stage' in line:
        in_func = True
        print(f"Entered execute_stage at line {i+1}")
        continue
    
    if in_func:
        if 'try:' in line and try_start is None:
            try_start = i + 1
            print(f"  try: starts at line {try_start}")
        if 'finally:' in line and finally_start is None:
            finally_start = i + 1
            print(f"  finally: starts at line {finally_start}")
            # Show what's in finally
            for j in range(i, min(i+30, len(lines))):
                print(f"    {j+1}: {lines[j]}")
            break

print(f"\n=== Code before try: block (lines before {try_start}) ===")
if try_start:
    # Find where execute_stage starts
    for i, line in enumerate(lines):
        if 'def execute_stage' in line:
            for j in range(i, try_start):
                print(f"  {j+1}: {lines[j]}")
            break

print("\n=== Key: what happens before try:? ===")
# Check if there's code that could crash before try block
for i, line in enumerate(lines):
    if 'def execute_stage' in line:
        for j in range(i, min(i+50, len(lines))):
            if 'try:' in lines[j]:
                print(f"  >>> Code between function start and try:")
                for k in range(i, j):
                    if lines[k].strip() and not lines[k].strip().startswith('#'):
                        print(f"    {k+1}: {lines[k].strip()[:80]}")
        break