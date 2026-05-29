# Find and read the CLI run module
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")

# Find cli.py
cli_py = researchclaw / "cli.py"
if cli_py.exists():
    print("=== cli.py (first 100 lines) ===")
    lines = cli_py.read_text(encoding='utf-8', errors='ignore').split('\n')
    for i, line in enumerate(lines[:100]):
        print(f"  {i+1}: {line}")
    
    print("\n=== Search for config loading ===")
    for i, line in enumerate(lines):
        if 'config' in line.lower() and ('load' in line.lower() or 'yaml' in line.lower() or 'from_yaml' in line.lower() or 'RCConfig' in line):
            print(f"  Line {i+1}: {line.strip()}")
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+5)
            for j in range(start, end):
                print(f"    {lines[j]}")
else:
    print("cli.py not found")

# Also check for any "def run" function
print("\n=== Search for 'def run' ===")
for pyfile in researchclaw.rglob("*.py"):
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if 'def run(' in content:
            print(f"  {pyfile.relative_to(researchclaw)}")
    except: pass
