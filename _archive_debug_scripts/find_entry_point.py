# Find the actual CLI entry point and main() function
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")

# List top-level structure
print("=== researchclaw/ top-level ===")
for item in sorted(researchclaw.iterdir()):
    print(f"  {item.name}/" if item.is_dir() else f"  {item.name}")

# Search for main() function
print("\n=== Searching for 'def main' ===")
found_main = False
for pyfile in researchclaw.rglob("*.py"):
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if 'def main(' in content:
            print(f"Found: {pyfile.relative_to(researchclaw)}")
            # Show context
            for i, line in enumerate(content.split('\n')):
                if 'def main' in line:
                    print(f"  Line {i+1}: {line.strip()}")
                    lines = content.split('\n')
                    for j in range(i, min(i+25, len(lines))):
                        print(f"    {lines[j]}")
                    found_main = True
                    break
    except: pass

if not found_main:
    print("No main() function found")
    
# Check if there's a __main__.py with more content
main_py = researchclaw / "__main__.py"
print(f"\n=== __main__.py (full) ===")
print(main_py.read_text(encoding='utf-8'))

# Also check for any .py that imports click or argparse
print("\n=== CLI framework usage ===")
for pyfile in researchclaw.rglob("*.py"):
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if any(kw in content for kw in ['import click', 'import argparse', 'from click']):
            print(f"  CLI framework in: {pyfile.relative_to(researchclaw)}")
    except: pass
