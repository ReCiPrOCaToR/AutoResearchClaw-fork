# Check how adapters are created in the pipeline execution
# Find where AdapterBundle is instantiated
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")

print("=== Searching for AdapterBundle instantiation ===")
for pyfile in researchclaw.rglob("*.py"):
    if pyfile.name == 'run_fixed.py':
        continue
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if 'AdapterBundle(' in content and not pyfile.name.startswith('test_'):
            print(f"\n{pyfile.relative_to(researchclaw)}:")
            for i, line in enumerate(content.split('\n')):
                if 'AdapterBundle(' in line:
                    print(f"  Line {i+1}: {line.strip()}")
                    # Show context
                    lines = content.split('\n')
                    start = max(0, i-3)
                    end = min(len(lines), i+6)
                    for j in range(start, end):
                        print(f"    {lines[j]}")
    except: pass

# Check main entry point
print("\n=== Main pipeline runner ===")
run_py = researchclaw / "cli" / "run.py"
if run_py.exists():
    print(f"Found: {run_py}")
    content = run_py.read_text(encoding='utf-8', errors='ignore')[:1000]
    print(content)
else:
    print("cli/run.py not found")
    # Check other locations
    for pyfile in researchclaw.rglob("*.py"):
        if 'def main' in pyfile.read_text(encoding='utf-8', errors='ignore'):
            print(f"Main in: {pyfile}")
