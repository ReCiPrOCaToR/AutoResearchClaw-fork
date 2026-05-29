# Find the CLI entry point and config loading
from pathlib import Path
import sys

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")

# Find __main__.py and see what it imports
main_py = researchclaw / "__main__.py"
print("=== __main__.py ===")
print(main_py.read_text())

# Find main() function
print("\n=== Searching for main() ===")
for pyfile in researchclaw.rglob("*.py"):
    if pyfile.name in ('__main__.py', 'main.py', 'cli.py', 'run.py', 'app.py'):
        content = pyfile.read_text()
        if 'def main' in content:
            print(f"Found main in: {pyfile.relative_to(researchclaw)}")
            # Show around main
            for i, line in enumerate(content.split('\n')):
                if 'def main' in line:
                    print(f"  Line {i+1}: {line.strip()}")
                    lines = content.split('\n')
                    for j in range(i, min(i+20, len(lines))):
                        print(f"    {lines[j]}")
                    break
