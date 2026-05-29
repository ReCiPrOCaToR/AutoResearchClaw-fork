# Find where create_llm_client is called in executor.py
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== create_llm_client calls ===")
for i, line in enumerate(lines):
    if 'create_llm_client' in line or 'llm =' in line:
        print(f"Line {i+1}: {line.strip()}")
        # Show surrounding context
        start = max(0, i-3)
        end = min(len(lines), i+6)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")
        print()
