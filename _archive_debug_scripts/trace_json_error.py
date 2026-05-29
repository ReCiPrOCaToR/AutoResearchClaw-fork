# Check response parsing - where does "Expecting value" come from?
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== Response parsing code ===")
for i, line in enumerate(lines):
    if 'json.loads' in line and ('resp' in line.lower() or 'data' in line.lower() or 'body' in line.lower()):
        print(f"Line {i+1}: {line.rstrip()}")
        # Show context
        start = max(0, i-3)
        end = min(len(lines), i+5)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")

print("\n\n=== Search for 'Expecting value' ===")
for i, line in enumerate(lines):
    if 'expecting' in line.lower() or 'json' in line.lower():
        if 'error' in line.lower() or 'except' in line.lower():
            print(f"Line {i+1}: {line.rstrip()}")
