# Check if _execute_problem_decompose uses config.project or other nested attrs
from pathlib import Path

topic_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_topic.py")
content = topic_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== _execute_problem_decompose: config accesses ===")
for i, line in enumerate(lines):
    if 'config.' in line and 'def ' not in line:
        print(f"  Line {i+1}: {line.strip()}")

print("\n=== _execute_topic_init: config accesses ===")
in_topic_init = False
for i, line in enumerate(lines):
    if 'def _execute_topic_init' in line:
        in_topic_init = True
    elif in_topic_init and 'def ' in line and '_execute_topic_init' not in line:
        break
    elif in_topic_init and 'config.' in line:
        print(f"  Line {i+1}: {line.strip()}")
