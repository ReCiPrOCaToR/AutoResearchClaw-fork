# Find the CLI main() function
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")
cli_dir = researchclaw / "cli"

print("=== CLI directory ===")
if cli_dir.exists():
    for f in sorted(cli_dir.iterdir()):
        print(f"  {f.name}")
else:
    print("cli/ not found")
    # Search for main()
    for pyfile in researchclaw.rglob("*.py"):
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if 'def main(' in content:
            print(f"Found main in: {pyfile.relative_to(researchclaw)}")

# Check __main__.py again
main_py = researchclaw / "__main__.py"
print(f"\n=== __main__.py content ===")
print(main_py.read_text())

# Find cli module
print("\n=== Searching for 'def main' ===")
for pyfile in researchclaw.rglob("*.py"):
    try:
        content = pyfile.read_text(encoding='utf-8', errors='ignore')
        if 'def main(' in content:
            print(f"  {pyfile.relative_to(researchclaw)}")
            # Show around main
            for i, line in enumerate(content.split('\n')):
                if 'def main' in line:
                    print(f"    Line {i+1}: {line.strip()}")
                    lines = content.split('\n')
                    for j in range(i, min(i+15, len(lines))):
                        print(f"      {lines[j]}")
                    break
    except: pass
