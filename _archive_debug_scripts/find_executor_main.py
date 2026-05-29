# Find main execution loop and llm initialization
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\executor.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print("=== Main function ===")
for i, line in enumerate(lines):
    if 'def run' in line or 'def main' in line or 'def execute' in line:
        print(f"Line {i+1}: {line.strip()}")

print("\n=== llm client creation ===")
for i, line in enumerate(lines):
    if 'create_llm_client' in line or 'llm =' in line:
        print(f"Line {i+1}: {line.strip()}")
        start = max(0, i-3)
        end = min(len(lines), i+6)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")
        print()
