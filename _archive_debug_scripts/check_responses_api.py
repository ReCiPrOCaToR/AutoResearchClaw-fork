# Check what _build_responses_body does and if wire_api is set to "responses"
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Find _build_responses_body
print("=== _build_responses_body method ===")
for i, line in enumerate(lines):
    if 'def _build_responses_body' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+60, len(lines))):
            print(f"  {lines[j]}")
        break

# Check if config.wire_api is set anywhere for ModelScope
print("\n=== Searching for wire_api assignments ===")
for i, line in enumerate(lines):
    if 'wire_api' in line and '=' in line and 'def' not in line:
        print(f"Line {i+1}: {line.rstrip()}")

# Check provider presets for ModelScope
print("\n=== Searching for ModelScope in PROVIDER_PRESETS ===")
# Find PROVIDER_PRESETS
for i, line in enumerate(lines):
    if 'PROVIDER_PRESETS' in line or 'provider' in line.lower():
        if '{' in line or ':' in line:
            print(f"Line {i+1}: {line.rstrip()}")
