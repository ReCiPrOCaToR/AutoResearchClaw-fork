from pathlib import Path

root = Path(r"D:\My_Project\AutoResearchClaw")
artifacts = root / "artifacts"

print("=== Checking Artifacts ===")
if artifacts.exists():
    runs = sorted(artifacts.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Found {len(runs)} artifact directories")
    for run in runs[:3]:
        mtime = run.stat().st_mtime
        print(f"\n{run.name}")
        print(f"  Modified: {mtime}")
        deliverables = run / "deliverables"
        print(f"  Has deliverables: {deliverables.exists()}")
        if deliverables.exists():
            files = list(deliverables.iterdir())
            print(f"  Files: {len(files)}")
            for f in files[:8]:
                print(f"    {f.name}")
else:
    print("No artifacts directory")
