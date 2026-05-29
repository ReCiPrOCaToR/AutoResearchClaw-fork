# Check how Stage 10 is executed - does it spawn a subprocess?
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== Looking for subprocess or multiprocessing ===")
for i, line in enumerate(lines):
    if any(kw in line.lower() for kw in ['subprocess', 'multiprocessing', 'process(', 'spawn', 'Popen']):
        print(f"Line {i+1}: {line.strip()}")

print("\n=== Entry point function name ===")
for i, line in enumerate(lines[:100]):
    if 'def ' in line and ('execute' in line.lower() or 'run' in line.lower() or 'stage' in line.lower()):
        print(f"Line {i+1}: {line.strip()}")

# Check if code_agent runs in-process or spawns something
print("\n=== CodeAgent sandbox creation ===")
for i, line in enumerate(lines):
    if 'sandbox_factory' in line or 'create_sandbox' in line:
        print(f"Line {i+1}: {line.strip()}")
