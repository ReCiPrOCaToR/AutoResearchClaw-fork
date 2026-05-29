# Check what LLMClient is created during Stage 10 execution
# Look for where LLMClient is instantiated in the pipeline
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== LLMClient creation in executor.py ===")
for i, line in enumerate(lines):
    if 'LLMClient' in line and '(' in line:
        print(f"Line {i+1}: {line.strip()}")
        # Show context
        start = max(0, i-3)
        end = min(len(lines), i+8)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")

print("\n=== Wire API usage ===")
for i, line in enumerate(lines):
    if 'wire_api' in line or 'wire_api=' in line:
        print(f"Line {i+1}: {line.strip()}")
