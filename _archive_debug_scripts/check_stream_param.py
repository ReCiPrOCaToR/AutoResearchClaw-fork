# Check if stream parameter is set in the request body
import re

with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

# Search for body construction
if '"stream"' in content or "'stream'" in content:
    print("Found 'stream' parameter in code")
    # Show context
    idx = content.find('"stream"')
    if idx == -1:
        idx = content.find("'stream'")
    print(f"Context around 'stream':")
    print(content[max(0,idx-100):idx+200])
else:
    print("No 'stream' parameter found in client.py")
    print("This confirms: stream is never set, defaults to true on many APIs")
