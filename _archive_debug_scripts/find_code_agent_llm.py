# Find LLM calls inside code_agent.py
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\code_agent.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== LLM calls in code_agent.py ===\n")
for i, line in enumerate(lines):
    if ('self._llm' in line and '.' in line) or ('llm.' in line.lower() and 'chat' in line.lower()):
        print(f"Line {i+1}: {line.strip()}")
        # Show context
        start = max(0, i-3)
        for j in range(start, min(i+4, len(lines))):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")

# Also search for _chat_with_prompt usage
print("\n=== _chat_with_prompt usage ===")
for i, line in enumerate(lines):
    if '_chat_with_prompt' in line and 'def' not in line:
        print(f"Line {i+1}: {line.strip()}")
