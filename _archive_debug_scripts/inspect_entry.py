# Check the researchclaw module structure
from pathlib import Path

researchclaw = Path(r"D:\My_Project\AutoResearchClaw\researchclaw")
print("=== researchclaw/ ===")
for f in sorted(researchclaw.iterdir()):
    print(f"  {f.name}/" if f.is_dir() else f"  {f.name}")

# Check cli module
cli = researchclaw / "cli"
if cli.exists():
    print(f"\n=== cli/ ===")
    for f in sorted(cli.iterdir()):
        print(f"  {f.name}")

# Check main entry
main_py = researchclaw / "__main__.py"
if main_py.exists():
    print(f"\n=== __main__.py ===")
    print(main_py.read_text()[:500])
