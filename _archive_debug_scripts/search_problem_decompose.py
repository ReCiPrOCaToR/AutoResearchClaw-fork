# Search for _execute_problem_decompose more carefully
from pathlib import Path

workspace = Path(r"D:\My_Project\AutoResearchClaw")
print("=== Searching all .py files ===")

found = False
for pyfile in workspace.rglob("*.py"):
    if '__pycache__' in str(pyfile):
        continue
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if '_execute_problem_decompose' in content:
            print(f"\nFound in: {pyfile.relative_to(workspace)}")
            for i, line in enumerate(content.split('\n')):
                if '_execute_problem_decompose' in line:
                    print(f"  Line {i+1}: {line.strip()}")
                    # Show next 10 lines
                    lines = content.split('\n')
                    for j in range(i, min(i+15, len(lines))):
                        print(f"    {lines[j]}")
            found = True
    except: pass

if not found:
    print("NOT FOUND in any .py file!")
    print("\nChecking for similar names:")
    for pyfile in workspace.rglob("*.py"):
        if '__pycache__' in str(pyfile):
            continue
        try:
            content = pyfile.read_text(encoding='utf-8', errors='ignore')
            if 'problem' in content.lower() and 'execute' in content.lower():
                print(f"  {pyfile.relative_to(workspace)}")
        except: pass
