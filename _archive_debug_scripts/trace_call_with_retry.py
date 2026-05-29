# Find _call_with_retry implementation
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'def _call_with_retry' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+80, len(lines))):
            print(f"  {lines[j]}")
        break
