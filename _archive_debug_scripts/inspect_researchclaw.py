# Check researchclaw module structure
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")
print("=== researchclaw/ structure ===")
for item in sorted(researchclaw.iterdir()):
    if item.is_dir():
        print(f"  {item.name}/")
        # Show first few files in subdir
        for sub in sorted(item.iterdir())[:5]:
            print(f"    {sub.name}")
    else:
        print(f"  {item.name}")

print("\n=== Looking for main() or cli ===")
# Search for main function
for pyfile in researchclaw.rglob("*.py"):
    if pyfile.name in ('__main__.py', 'main.py', 'cli.py', 'run.py'):
        print(f"  Entry candidate: {pyfile.relative_to(researchclaw)}")
        try:
            content = pyfile.read_text()
            if 'def main' in content or 'if __name__' in content:
                print(f"    Contains main/entry point")
        except: pass
