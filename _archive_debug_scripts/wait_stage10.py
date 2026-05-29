import time
from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")
stage10 = run / "stage-10"

print("Waiting for Stage 10 to complete...")
for i in range(12):  # wait up to 60s
    time.sleep(5)
    if stage10.exists():
        files = list(stage10.iterdir())
        if len(files) > 1:  # more than just complexity_analysis
            print(f"[{i*5}s] Stage 10 has {len(files)} files")
            break
    print(f"[{i*5}s] Still waiting...")

# Final inspection
print("\n=== FINAL STAGE 10 STATUS ===")
if stage10.exists():
    for f in sorted(stage10.iterdir()):
        size = f.stat().st_size
        print(f"  {f.name}: {size} bytes")

    # Read decision if available
    dec_file = stage10 / "decision.json"
    if dec_file.exists():
        dec = json.loads(dec_file.read_text())
        print(f"\nDecision: {dec.get('decision')}")
        print(f"Status: {dec.get('status')}")
        print(f"Error: {dec.get('error')}")
        print(f"Outputs: {dec.get('output_artifacts')}")

# Check if stage 11 started
stage11 = run / "stage-11"
if stage11.exists():
    print(f"\n*** STAGE 11 STARTED! ***")
    print(f"Files: {len(list(stage11.iterdir()))}")

# Check total artifacts
total = len(list(run.rglob("*")))
print(f"\nTotal files in run: {total}")
