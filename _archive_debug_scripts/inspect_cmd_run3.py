# Search for config loading in cmd_run
from pathlib import Path

cli_py = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli.py")
content = cli_py.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Full cmd_run config loading ===")
in_cmd_run = False
for i, line in enumerate(lines):
    if 'def cmd_run(' in line:
        in_cmd_run = True
        print(f"Entered cmd_run at line {i+1}")
        continue
    
    if in_cmd_run:
        # Show all lines until adapters = AdapterBundle()
        if 'AdapterBundle()' in line:
            print(f"\n--- Found AdapterBundle at line {i+1} ---")
            # Show leading lines
            for j in range(max(0, i-30), i+1):
                print(f"  {j+1}: {lines[j]}")
            break

print("\n=== Also check _resolve_config_or_exit ===")
for i, line in enumerate(lines):
    if 'def _resolve_config_or_exit' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+60, len(lines))):
            print(f"  {j+1}: {lines[j]}")
        break
