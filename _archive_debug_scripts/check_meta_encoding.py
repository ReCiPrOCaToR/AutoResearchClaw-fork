# Check _write_stage_meta encoding
from pathlib import Path

helpers_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\_helpers.py")
content = helpers_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _write_stage_meta function ===")
for i, line in enumerate(lines):
    if 'def _write_stage_meta' in line:
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+40, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
            if 'write_text' in cur_line:
                has_encoding = 'encoding=' in cur_line
                print(f"      → encoding: {has_encoding}")
        break

print("\n=== Also check _write_jsonl ===")
for i, line in enumerate(lines):
    if 'def _write_jsonl' in line:
        indent = len(line) - len(line.lstrip())
        for j in range(i, min(i+30, len(lines))):
            cur_line = lines[j]
            cur_indent = len(cur_line) - len(cur_line.lstrip())
            if cur_line.strip() and cur_indent <= indent and j > i:
                break
            print(f"  {j+1}: {cur_line}")
            if 'write_text' in cur_line or 'open(' in cur_line:
                has_encoding = 'encoding=' in cur_line
                print(f"      → encoding: {has_encoding}")