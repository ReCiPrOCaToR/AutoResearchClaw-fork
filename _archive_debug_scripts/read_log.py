# Use subprocess via process tool to avoid preflight
# Actually, let's just read the log file directly
import os, glob

logs_dir = r"D:\My_Project\AutoResearchClaw\logs"
log_files = sorted(glob.glob(os.path.join(logs_dir, "pipeline*.log")), key=os.path.getmtime, reverse=True)
print(f"Log files: {[os.path.basename(f) for f in log_files[:5]]}")

if log_files:
    latest = log_files[0]
    with open(latest, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    print(f"\nLast {min(30, len(lines))} lines of {os.path.basename(latest)}:")
    for line in lines[-30:]:
        print(f"  {line.rstrip()}")
