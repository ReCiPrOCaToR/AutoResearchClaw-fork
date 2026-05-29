# Check how code_agent is instantiated in _execute_code_generation
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== CodeAgent instantiation ===")
for i, line in enumerate(lines):
    if 'CodeAgent' in line and '(' in line:
        # Show context
        start = max(0, i-3)
        end = min(len(lines), i+10)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"{marker} {lines[j].rstrip()}")

print("\n\n=== LLM creation in _execute_code_generation ===")
for i, line in enumerate(lines):
    if 'LLMClient' in line and '=' in line:
        start = max(0, i-2)
        end = min(len(lines), i+5)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"{marker} {lines[j].rstrip()}")
