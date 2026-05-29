from pathlib import Path
import re

# Find the main entry point for Stage 10
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    content = f.read()

# Find function definitions
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.startswith('def ') and i < 3000:
        print(f"Line {i+1}: {line}")

# Look for the stage runner function (usually called run or execute)
print("\n\nSearching for LLM calls in early part:")
# Find first occurrence of 'llm.chat' or 'LLMClient'
for i, line in enumerate(lines[:3000]):
    if 'llm.chat' in line.lower() or 'LLMClient' in line:
        print(f"Line {i+1}: {line.strip()}")
        # Show context
        start = max(0, i-3)
        end = min(len(lines), i+4)
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"  {marker} {lines[j]}")
