from pathlib import Path
import subprocess

# Find code_agent implementation
result = subprocess.run(
    ["find", "-name", "*code_agent*", "-not", "-path", "*/__pycache__/*"],
    capture_output=True, text=True,
    cwd=r"D:\My_Project\AutoResearchClaw"
)
print("Code agent files:")
print(result.stdout[:3000])

# Also search for "code_agent" class definition
print("\n=== Searching for code_agent class ===")
for f in Path(r"D:\My_Project\AutoResearchClaw").rglob("*.py"):
    if "__pycache__" in str(f):
        continue
    try:
        content = f.read_text(encoding='utf-8', errors='ignore')
        if 'class' in content and 'code_agent' in content.lower() and 'def' in content:
            rel_path = str(f.relative_to(Path(r'D:\My_Project\AutoResearchClaw')))
            print(f"\nFound in: {rel_path}")
            # Show class definition
            for i, line in enumerate(content.split('\n')[:100]):
                if 'class' in line and 'code' in line.lower():
                    print(f"  Line {i+1}: {line}")
                    # Show next 20 lines
                    lines = content.split('\n')
                    for j in range(i, min(i+20, len(lines))):
                        print(f"    {lines[j]}")
                    break
    except:
        pass
