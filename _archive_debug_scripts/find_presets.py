# Find PROVIDER_PRESETS definition
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== PROVIDER_PRESETS ===")
in_presets = False
for i, line in enumerate(lines):
    if 'PROVIDER_PRESETS' in line and '=' in line and 'def' not in line:
        in_presets = True
    if in_presets:
        print(f"Line {i+1}: {line}")
        if line.strip() and not line[0].isspace() and i > 0:
            break
        if len(line) < 5 and i > 100:
            break

print("\n=== Search for 'modelscope' or 'stepfun' ===")
for i, line in enumerate(lines):
    if 'modelscope' in line.lower() or 'stepfun' in line.lower():
        print(f"Line {i+1}: {line.strip()}")
