# Find the FIRST llm.chat call in Stage 10 (the one that likely fails)
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== Searching for first llm.chat or LLM invocation ===\n")
for i, line in enumerate(lines[:1500]):
    if 'llm.chat' in line or ('LLMClient' in line and 'def' not in line):
        # Show context
        print(f"Line {i+1}: {line.rstrip()}")
        start = max(0, i-5)
        for j in range(start, i+1):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j].rstrip()}")
        print()
        # Only show first few occurrences
        if i > 500:
            print("... (stopping search)")
            break
