# Continue searching for config loading in cmd_run
from pathlib import Path

cli_py = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli.py")
content = cli_py.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== cmd_run function: config loading ===")
in_cmd_run = False
for i, line in enumerate(lines):
    if 'def cmd_run(' in line:
        in_cmd_run = True
        print(f"Entered cmd_run at line {i+1}")
        continue
    
    if in_cmd_run:
        # Look for config-related lines
        if any(keyword in line for keyword in ['config_path', 'resolve_config', 'RCConfig', 'yaml.safe_load', 'config =']):
            print(f"Line {i+1}: {line.strip()}")
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+6)
            for j in range(start, end):
                if j != i:
                    print(f"  {j+1}: {lines[j]}")
        
        # Stop at adapter creation or pipeline execution
        if 'AdapterBundle()' in line:
            print(f"\n=== Adapter creation at line {i+1} ===")
            print(f"  Context:")
            for j in range(max(0,i-5), min(len(lines), i+10)):
                print(f"    {j+1}: {lines[j]}")
            break
