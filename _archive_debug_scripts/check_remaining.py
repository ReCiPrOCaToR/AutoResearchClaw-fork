from pathlib import Path

root = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
if root.exists():
    runs = sorted(root.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Remaining runs: {len(runs)}")
    for r in runs:
        print(f"  {r.name}")
