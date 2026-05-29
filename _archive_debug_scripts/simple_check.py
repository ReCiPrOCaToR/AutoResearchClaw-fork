# Simple check - just read file
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

has_stream = 'body["stream"] = False' in content
print(f"Stream=false present: {has_stream}")

# Count occurrences
count = content.count('"stream"')
print(f"Total 'stream' occurrences: {count}")

# Show lines with stream
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'stream' in line.lower():
        print(f"Line {i+1}: {line.strip()}")
