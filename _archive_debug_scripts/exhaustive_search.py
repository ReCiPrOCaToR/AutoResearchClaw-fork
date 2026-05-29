from pathlib import Path
import json

# Check if stage-10 has any hidden files or subdirs we missed
stage10 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf\stage-10")
all_items = list(stage10.rglob("*"))
print(f"Total items in stage-10: {len(all_items)}")
for item in all_items:
    print(f"  {item.relative_to(stage10)}")

# Also check parent run dir for any stage-10 subdirs that might be separate
run = stage10.parent
subdirs = [d for d in run.iterdir() if d.is_dir() and 'stage-10' in d.name.lower()]
print(f"\nStage-10 related dirs: {[d.name for d in subdirs]}")
for d in subdirs:
    files = list(d.rglob("*"))
    print(f"  {d.name}: {len(files)} files")

# Check if there's a separate experiment output dir
exp_dirs = list(run.rglob("experiment"))
print(f"\nExperiment dirs: {len(exp_dirs)}")
for ed in exp_dirs[:5]:
    print(f"  {ed.relative_to(run)}")
