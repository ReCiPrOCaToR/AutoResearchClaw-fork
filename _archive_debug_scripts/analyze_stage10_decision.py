from pathlib import Path
import json

# Check stage-10 decision and what path it chose
run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf\stage-10")

print("=== Stage 10 Decision Logic ===\n")

# Read decision
decision = json.loads((run / "decision.json").read_text())
print(f"Decision: {decision.get('decision')}")
print(f"Status: {decision.get('status')}")
print(f"Error: {decision.get('error')}")

# The complexity analysis said "recommendation": "code_agent"
ca = json.loads((run / "complexity_analysis.json").read_text())
print(f"\nComplexity score: {ca.get('score')}")
print(f"Recommendation: {ca.get('recommendation')}")

# Now check if code_agent was invoked
# Look for code_agent artifacts
code_agent_dir = run / "code_agent_workspace"
if code_agent_dir.exists():
    print(f"\ncode_agent workspace exists: {len(list(code_agent_dir.rglob('*')))} files")
else:
    print(f"\nNo code_agent workspace found")

# Check for any generated code
all_files = list(run.rglob("*"))
print(f"\nAll files in stage-10:")
for f in sorted(all_files, key=lambda x: x.stat().st_mtime):
    print(f"  {f.name} ({f.stat().st_size} bytes)")

# Also check if opencode was attempted
opencode_dirs = list(run.glob("opencode_beast*"))
print(f"\nOpenCode beast dirs: {len(opencode_dirs)}")
for d in opencode_dirs:
    print(f"  {d.name}")
