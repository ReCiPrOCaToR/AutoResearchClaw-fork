# Find where config is loaded in cli.py main()
from pathlib import Path

cli_py = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\cli.py")
content = cli_py.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== Searching for config loading in main() ===")
in_main = False
for i, line in enumerate(lines):
    if 'def main(' in line:
        in_main = True
        print(f"Entered main at line {i+1}")
    if in_main:
        if any(kw in line.lower() for kw in ['rcconfig', 'from_yaml', 'load_config', 'resolve_config', 'yaml.safe_load']):
            print(f"Line {i+1}: {line.strip()}")
            # Show surrounding context
            start = max(0, i-3)
            end = min(len(lines), i+8)
            for j in range(start, end):
                marker = ">>>" if j == i else "   "
                print(f"  {marker} {lines[j]}")
        if 'return' in line and i > 1020:
            break

print("\n=== Search for 'RCConfig' usage ===")
for i, line in enumerate(lines):
    if 'RCConfig' in line and i > 1000:
        print(f"Line {i+1}: {line.strip()}")
