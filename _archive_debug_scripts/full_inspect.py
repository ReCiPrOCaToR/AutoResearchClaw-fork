from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")

# Check all stage-10 files thoroughly
stage10 = run / "stage-10"
print("=== Stage 10 Complete File List ===\n")

if stage10.exists():
    files = sorted(stage10.rglob("*"), key=lambda f: f.stat().st_mtime)
    for f in files:
        size = f.stat().st_size
        print(f"{size:>6}  {f.relative_to(stage10)}")

# Look for any log files or error outputs
print("\n=== Searching for logs/errors ===")
log_files = list(run.rglob("*.log")) + list(run.rglob("*.err")) + list(run.rglob("error*.txt"))
print(f"Log/error files: {len(log_files)}")
for log in log_files:
    print(f"  {log.relative_to(run)}")
    try:
        content = log.read_text(encoding='utf-8', errors='replace')
        if 'error' in content.lower() or 'exception' in content.lower():
            print(f"    *** CONTAINS ERROR ***")
            # Show last 10 lines
            lines = content.split('\n')
            for line in lines[-10:]:
                print(f"      {line[:120]}")
    except Exception as e:
        print(f"    (read error: {e})")

# Check if any partial code was generated
code_files = list(run.rglob("*.py"))
print(f"\n=== Python files in entire run: {len(code_files)} ===")
for cf in code_files:
    print(f"  {cf.relative_to(run)} ({cf.stat().st_size} bytes)")

# Check experiment dir
exp_dir = run / "experiment"
if exp_dir.exists():
    print(f"\n=== Experiment directory ===")
    exp_files = list(exp_dir.rglob("*"))
    print(f"Files: {len(exp_files)}")
    for f in exp_files[:10]:
        print(f"  {f.relative_to(run)}")
