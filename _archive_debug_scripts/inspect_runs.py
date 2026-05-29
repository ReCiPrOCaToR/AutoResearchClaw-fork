from pathlib import Path
import json

root = Path(r"D:\My_Project\AutoResearchClaw\artifacts")
runs = sorted(root.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)

for run in runs[:3]:
    print(f"\n{'='*60}")
    print(f"Run: {run.name}")
    print(f"Modified: {run.stat().st_mtime}")

    # List all files recursively
    all_files = list(run.rglob("*"))
    all_files = [f for f in all_files if f.is_file()]
    print(f"Total files: {len(all_files)}")

    # Check key directories
    for subdir in ["deliverables", "experiment_runs", "charts", "evolution", "docs"]:
        subpath = run / subdir
        if subpath.exists():
            files = list(subpath.iterdir())
            print(f"  {subdir}/: {len(files)} items")
            for f in files[:5]:
                print(f"    {f.name}")

    # Check for any JSON logs or status files
    status_files = list(run.glob("*.json")) + list(run.glob("*.log")) + list(run.glob("*.md"))
    if status_files:
        print(f"  Status files: {len(status_files)}")
        for sf in status_files[:5]:
            print(f"    {sf.name}")
