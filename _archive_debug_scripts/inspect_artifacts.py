from pathlib import Path

root = Path(r"D:\My_Project\AutoResearchClaw")
artifacts = root / "artifacts"

if artifacts.exists():
    runs = sorted(artifacts.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"Found {len(runs)} artifact directories\n")
    for run in runs[:2]:
        print(f"=== {run.name} ===")
        deliverables = run / "deliverables"
        if deliverables.exists():
            files = list(deliverables.iterdir())
            print(f"  Deliverables: {len(files)} files")
            for f in files[:10]:
                print(f"    {f.name}")
        else:
            print("  No deliverables/")
        print()
