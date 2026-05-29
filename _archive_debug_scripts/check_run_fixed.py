# Check what run_fixed.py does and how it handles errors
from pathlib import Path

run_fixed = Path(r"D:\My_Project\AutoResearchClaw\run_fixed.py")
print("=== run_fixed.py content ===")
print(run_fixed.read_text())

print("\n=== Check if researchclaw.run module handles exceptions ===")
# Find main entry point
run_module = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli\run.py")  # common location
if not run_module.exists():
    run_module = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\run.py")
if run_module.exists():
    print(f"Found run module: {run_module}")
    content = run_module.read_text()
    # Look for main() or entry point
    for i, line in enumerate(content.split('\n')[:100]):
        if 'def main' in line or 'if __name__' in line:
            print(f"  Line {i+1}: {line}")
            # Show context
            lines = content.split('\n')
            start = max(0, i-3)
            for j in range(start, min(i+10, len(lines))):
                print(f"    {lines[j]}")
