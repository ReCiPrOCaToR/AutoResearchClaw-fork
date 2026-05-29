from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")

# Check stage-09 to see what experiment plan was generated
stage09 = run / "stage-09"
print("=== Stage 09 Outputs (inputs to Stage 10) ===\n")

if stage09.exists():
    for f in sorted(stage09.iterdir()):
        print(f"\n--- {f.name} ({f.stat().st_size} bytes) ---")
        try:
            content = f.read_text(encoding='utf-8', errors='replace')
            print(content[:800])
        except Exception as e:
            print(f"Error reading: {e}")

# Also check benchmark plan
benchmark_files = list(stage09.rglob("benchmark_plan.json"))
if benchmark_files:
    print("\n=== BENCHMARK PLAN ===")
    print(json.dumps(json.loads(benchmark_files[0].read_text()), indent=2)[:1000])
