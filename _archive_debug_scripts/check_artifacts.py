from pathlib import Path

root = Path(r"D:\My_Project\AutoResearchClaw")
artifacts = root / "artifacts"

if artifacts.exists():
    runs = sorted(artifacts.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Found {len(runs)} artifact directories")
    for run in runs[:5]:
        print(f"  {run.name}")
else:
    print("No artifacts yet")
