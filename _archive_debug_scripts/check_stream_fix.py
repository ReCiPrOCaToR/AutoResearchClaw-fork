# Check if stream=false is in the body building code
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== Checking for stream parameter ===")
for i, line in enumerate(lines):
    if 'stream' in line.lower() and ('body' in line.lower() or 'json' in line.lower() or 'data' in line.lower()):
        print(f"Line {i+1}: {line.rstrip()}")

print("\n=== Checking _raw_call method ===")
# Find _raw_call definition
for i, line in enumerate(lines):
    if 'def _raw_call' in line:
        print(f"Found at line {i+1}")
        # Show the whole method
        indent_level = len(line) - len(line.lstrip())
        for j in range(i, min(i+80, len(lines))):
            cur_indent = len(lines[j]) - len(lines[j].lstrip())
            if lines[j].strip() and cur_indent <= indent_level and j > i:
                break
            print(f"  {lines[j].rstrip()}")
        break
