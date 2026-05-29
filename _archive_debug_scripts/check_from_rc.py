# Check from_rc_config for ModelScope-specific logic
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== from_rc_config method ===")
for i, line in enumerate(lines):
    if 'def from_rc_config' in line:
        for j in range(i, min(i+100, len(lines))):
            print(f"{j+1:4d}: {lines[j]}")
        break

print("\n=== PROVIDER_PRESETS ===")
for i, line in enumerate(lines):
    if 'PROVIDER_PRESETS' in line and '=' in line and not line.strip().startswith('#'):
        print(f"Line {i+1}: {line.strip()}")
        # Show a few lines around it
        for j in range(i, min(i+30, len(lines))):
            if lines[j].strip() and not lines[j].startswith(' ') and j > i:
                break
            print(f"  {lines[j]}")
