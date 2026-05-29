# Check imports in _code_generation.py - does it import LLMClient fresh?
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== Imports (first 30 lines) ===")
for i in range(min(30, len(lines))):
    print(f"{i+1:3d}: {lines[i]}", end='')
