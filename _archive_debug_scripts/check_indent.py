# Check exact indentation of the stream=false line
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== Checking indentation around line 440 ===")
for i in range(418, 448):
    line = lines[i]
    # Show spaces visually
    vis = line.replace(' ', '·').replace('\t', '→')
    print(f"{i+1:4d}: {vis}", end='')

# Also check the if/else structure
print("\n\n=== Structure check ===")
for i in range(415, 445):
    line = lines[i]
    stripped = line.strip()
    if stripped.startswith('if ') or stripped.startswith('else:') or stripped.startswith('elif '):
        print(f"Line {i+1}: {stripped}")
