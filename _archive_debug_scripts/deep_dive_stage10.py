from pathlib import Path
import json

# Check if opencode was triggered by looking for beast mode dirs or logs
run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-050113-03dfbf")

# Search ALL stage-10 subdirectories for opencode evidence
stage10 = run / "stage-10"
print("=== Searching for OpenCode traces ===\n")

all_items = list(stage10.rglob("*"))
for item in all_items:
    if 'opencode' in item.name.lower() or 'beast' in item.name.lower():
        print(f"Found: {item.relative_to(stage10)}")
        if item.is_file():
            try:
                print(f"  Content: {item.read_text(encoding='utf-8', errors='replace')[:500]}")
            except: pass

# Check if there's a log from code_agent
logs = list(stage10.rglob("*.log")) + list(stage10.rglob("*.txt"))
print(f"\nLog files in stage-10: {len(logs)}")
for log in logs:
    print(f"  {log.name}")
    try:
        content = log.read_text(encoding='utf-8', errors='replace')
        if 'error' in content.lower() or 'fail' in content.lower():
            print(f"  *** CONTAINS ERROR/FAIL ***")
            print(f"  Last 10 lines:")
            lines = content.split('\n')
            for line in lines[-10:]:
                print(f"    {line}")
    except: pass

# Read decision.json to understand what path was chosen
decision = json.loads((stage10 / "decision.json").read_text())
print(f"\n=== DECISION ===")
print(f"Decision: {decision.get('decision')}")
print(f"Status: {decision.get('status')}")
print(f"Error: {decision.get('error')}")

# Check if there are any other artifact files
print(f"\n=== ALL STAGE-10 FILES ===")
for f in sorted(all_items):
    size = f.stat().st_size
    print(f"  {size:>6}  {f.relative_to(stage10)}")
