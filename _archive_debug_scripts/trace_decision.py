# Find where the decision to use code_agent vs opencode is made
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== Finding decision logic (opencode vs code_agent) ===\n")
for i, line in enumerate(lines[:1600]):
    if 'opencode' in line.lower() or 'code_agent' in line.lower():
        if 'if' in line or 'else' in line or 'decision' in line.lower() or 'choose' in line.lower():
            print(f"Line {i+1}: {line.strip()}")
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+5)
            for j in range(start, end):
                marker = ">>>" if j == i else "   "
                print(f"  {marker} {lines[j]}")

# Find the first call to _chat or llm.chat AFTER the complexity analysis
print("\n\n=== First LLM call after complexity ===")
found_complexity = False
for i, line in enumerate(lines):
    if 'complexity_analysis' in line.lower() and 'json' in line.lower():
        found_complexity = True
        print(f"Complexity analysis at line {i+1}")
    if found_complexity and ('llm.chat' in line or '_chat(' in line):
        print(f"\nFirst LLM call at line {i+1}:")
        start = max(0, i-5)
        end = min(len(lines), i+10)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")
        break
