from pathlib import Path
import re

# Find OpenCode-related files
root = Path(r"D:\My_Project\AutoResearchClaw")
opencode_files = list(root.rglob("*opencode*")) + list(root.rglob("*open_code*"))
print(f"OpenCode-related files: {len(opencode_files)}")
for f in opencode_files[:10]:
    print(f"  {f.relative_to(root)}")

# Search for OpenCode usage in codebase
print("\n=== Searching for OpenCode instantiation ===")
for f in root.rglob("*.py"):
    try:
        content = f.read_text(encoding='utf-8', errors='ignore')
        if 'OpenCode' in content or 'opencode' in content:
            # Find context
            for i, line in enumerate(content.split('\n')[:50]):
                if 'OpenCode' in line or 'opencode' in line.lower():
                    print(f"\n{f.relative_to(root)} (line {i+1}):")
                    print(f"  {line.strip()}")
                    # Show surrounding lines
                    lines = content.split('\n')
                    start = max(0, i-2)
                    end = min(len(lines), i+3)
                    for j in range(start, end):
                        marker = ">>>" if j == i else "   "
                        print(f"  {marker} {lines[j]}")
    except Exception as e:
        pass
