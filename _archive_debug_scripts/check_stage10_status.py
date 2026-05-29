from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
stage10 = run / "stage-10"

print("=== Stage 10 Files ===")
if stage10.exists():
    for f in sorted(stage10.iterdir()):
        print(f"  {f.name} ({f.stat().st_size} bytes)")

# Try to read decision
decision = stage10 / "decision.json"
if decision.exists():
    print("\n=== DECISION ===")
    print(json.dumps(json.loads(decision.read_text()), indent=2))
else:
    print("\nNo decision.json yet")

# Check logs
import subprocess
result = subprocess.run(
    ["python", "-c", "import psutil; [print(f'{p.pid}: {p.name()} - {\" \".join(p.cmdline())}') for p in psutil.process_iter(['pid','name','cmdline']) if 'researchclaw' in str(p.info)]"],
    capture_output=True, text=True, cwd=r"D:\My_Project\AutoResearchClaw"
)
if result.stdout.strip():
    print("\n=== RESEARCHCLAW PROCESSES ===")
    print(result.stdout)
else:
    print("\nNo researchclaw processes running")
