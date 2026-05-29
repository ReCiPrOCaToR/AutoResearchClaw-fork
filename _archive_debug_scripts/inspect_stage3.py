# Check stage-03 details
from pathlib import Path

stage3 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-03")
print(f"Stage-03 files:")
for f in sorted(stage3.iterdir()):
    size = f.stat().st_size
    print(f"  {f.name} ({size} bytes)")
    if f.suffix in ('.json', '.yaml', '.txt') and size < 5000:
        try:
            content = f.read_text()
            print(f"    Content: {content[:300]}")
        except Exception as e:
            print(f"    Error: {e}")

# Check stage health
health = stage3 / "stage_health.json"
if health.exists():
    print(f"\nStage health:")
    print(health.read_text())

decision = stage3 / "decision.json"
if decision.exists():
    print(f"\nDecision:")
    print(decision.read_text())
