# Find cmd_run function in cli.py
from pathlib import Path

cli_py = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli.py")
content = cli_py.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for def cmd_run ===")
for i, line in enumerate(lines):
    if 'def cmd_run' in line:
        print(f"Found at line {i+1}")
        # Show full function
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+200, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {lines[j]}")
        break

print("\n=== Search for config loading pattern ===")
for i, line in enumerate(lines):
    if any(kw in line.lower() for kw in ['rcconfig', 'from_yaml', 'load_config', 'yaml.load', 'config =']):
        if i < 2000:  # Only early part (cmd_run likely early)
            print(f"Line {i+1}: {line.strip()}")
