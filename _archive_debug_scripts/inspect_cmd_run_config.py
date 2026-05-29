# Find where config is loaded in cmd_run
from pathlib import Path

cli_py = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli.py")
content = cli_py.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for config loading in cmd_run ===")
in_cmd_run = False
for i, line in enumerate(lines):
    if 'def cmd_run(' in line:
        in_cmd_run = True
        print(f"Entered cmd_run at line {i+1}")
    if in_cmd_run:
        if any(kw in line for kw in ['RCConfig', 'from_yaml', 'load_config', 'yaml.', 'config_path', 'resolve_config']):
            print(f"Line {i+1}: {line.strip()}")
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+6)
            for j in range(start, end):
                marker = ">>>" if j == i else "   "
                print(f"  {marker} {lines[j]}")
        if 'adapters = AdapterBundle()' in line:
            print(f"\nFound adapters creation at line {i+1}")
        if 'execute_pipeline(' in line:
            print(f"\nFound execute_pipeline call at line {i+1}")
            break

# Also search for RCConfig usage in cli.py
print("\n=== All RCConfig occurrences in cli.py ===")
for i, line in enumerate(lines):
    if 'RCConfig' in line and 'import' not in line:
        print(f"Line {i+1}: {line.strip()}")
