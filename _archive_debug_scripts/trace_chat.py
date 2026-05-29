# Find the chat() method and see if it calls _raw_call
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== LLMClient.chat() method ===")
for i, line in enumerate(lines):
    if 'def chat(' in line:
        print(f"Found at line {i+1}")
        for j in range(i, min(i+100, len(lines))):
            print(f"  {lines[j]}")
        break

# Check if chat calls _raw_call or _call_with_retry
print("\n=== Searching for _raw_call usage ===")
for i, line in enumerate(lines):
    if '_raw_call' in line and 'def' not in line:
        print(f"Line {i+1}: {line.rstrip()}")

print("\n=== Searching for _call_with_retry usage ===")
for i, line in enumerate(lines):
    if '_call_with_retry' in line and 'def' not in line:
        print(f"Line {i+1}: {line.rstrip()}")
