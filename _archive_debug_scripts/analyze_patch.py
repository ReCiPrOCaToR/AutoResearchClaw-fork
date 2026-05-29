"""Check if the stream=false patch is in the right place and covers all cases."""
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show _raw_call method from line 391 onwards
print("=== _raw_call method (lines 391-500) ===")
for i in range(390, min(500, len(lines))):
    print(f"{i+1:4d}: {lines[i]}", end='')

# Also check if there are any other places that construct request bodies
print("\n\n=== All places that construct request body ===")
for i, line in enumerate(lines):
    if 'body' in line and ('{' in line or '=' in line):
        if any(kw in line for kw in ['model', 'messages', 'stream', 'temperature']):
            print(f"Line {i+1}: {line.rstrip()}")

# Check for any direct HTTP calls that might bypass _raw_call
print("\n=== Direct urllib/requests calls ===")
for i, line in enumerate(lines):
    if any(kw in line for kw in ['urllib.request', 'requests.post', 'http.client']):
        print(f"Line {i+1}: {line.rstrip()}")
