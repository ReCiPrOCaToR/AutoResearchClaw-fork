# Check AdapterBundle initialization
from pathlib import Path

adapters_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\adapters.py")
if adapters_file.exists():
    print("=== adapters.py ===")
    content = adapters_file.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    for i, line in enumerate(lines[:100]):
        print(f"  {i+1}: {line}")
    
    print("\n=== AdapterBundle class ===")
    for i, line in enumerate(lines):
        if 'class AdapterBundle' in line or 'class' in line and 'Adapter' in line:
            for j in range(i, min(i+60, len(lines))):
                print(f"  {j+1}: {lines[j]}")
            break
else:
    print("adapters.py not found")
    # Search for AdapterBundle elsewhere
    import subprocess
    result = subprocess.run(['find', '-name', '*.py', '-exec', 'grep', '-l', 'AdapterBundle', '{}', ';'],
                           capture_output=True, text=True, cwd=r'D:\My_Project\AutoResearchClaw')
    print("AdapterBundle found in:")
    print(result.stdout[:500])
