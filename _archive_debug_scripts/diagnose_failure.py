from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-044520-03dfbf")

print("=== STAGE 10 DETAILS ===\n")
stage10 = run / "stage-10"

for f in sorted(stage10.iterdir()):
    print(f"\n--- {f.name} ---")
    content = f.read_text(encoding='utf-8', errors='replace')
    print(content[:2000])

# Also check if there's an error log somewhere
print("\n\n=== CHECKING FOR ERROR LOGS ===")
error_files = list(run.rglob("error*.txt")) + list(run.rglob("*.err")) + list(run.glob("*.log"))
print(f"Error-related files: {len(error_files)}")
for err in error_files:
    print(f"\n{err.name}:")
    print(err.read_text(encoding='utf-8', errors='replace')[:500])

# Check stage health for previous stages to see if any warnings
print("\n\n=== STAGE HEALTH SUMMARY ===")
for stage_num in range(1, 11):
    stage_dir = run / f"stage-{stage_num:02d}"
    health = stage_dir / "stage_health.json"
    if health.exists():
        data = json.loads(health.read_text())
        status = data.get('status', '?')
        duration = data.get('duration_sec', 0)
        error = data.get('error')
        print(f"Stage {stage_num:02d}: {status:12s} duration={duration:.2f}s error={error}")
