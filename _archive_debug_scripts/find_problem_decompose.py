# Find where _execute_problem_decompose is defined
import subprocess
result = subprocess.run(
    ['find', '-name', '*.py', '-not', '-path', '*/__pycache__/*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)

print("=== Searching for _execute_problem_decompose ===")
for pyfile in result.stdout.strip().split('\n'):
    if not pyfile.strip():
        continue
    try:
        with open(pyfile, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if '_execute_problem_decompose' in content:
            print(f"\nFound in: {pyfile}")
            # Show definition
            for i, line in enumerate(content.split('\n')):
                if '_execute_problem_decompose' in line and 'def' in line:
                    print(f"  Line {i+1}: {line.strip()}")
                    # Show next 30 lines
                    lines = content.split('\n')
                    for j in range(i, min(i+30, len(lines))):
                        print(f"    {lines[j]}")
                    break
    except Exception as e:
        pass

print("\n=== Also check if it's imported ===")
# Check executor.py imports
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py", 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
for i, line in enumerate(content.split('\n')[:100]):
    if 'import' in line or 'from' in line:
        print(f"  {i+1}: {line.strip()}")
