# Search for early returns or conditions that might skip code generation
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    content = f.read()

# Find main function
import re
# Find _execute_code_generation function
start = content.find('def _execute_code_generation')
print(f"Function starts at position: {start}")
if start != -1:
    # Show first 2000 chars of function
    snippet = content[start:start+2000]
    print(snippet)

# Look for "return" statements before the main logic
lines = content.split('\n')
for i, line in enumerate(lines):
    if i > 50 and i < 200 and 'return' in line and 'def' not in line:
        print(f"\nEarly return at line {i+1}: {line.strip()}")
