# Check write_text calls in _execute_search_strategy
from pathlib import Path

lit_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_literature.py")
content = lit_file.read_text(encoding='utf-8', errors='ignore')
lines = content.split('\n')

print("=== write_text calls in _literature.py ===")
for i, line in enumerate(lines):
    if 'write_text' in line:
        # Check if encoding is specified
        has_encoding = 'encoding=' in line
        print(f"Line {i+1}: {line.strip()[:100]}")
        print(f"  → encoding specified: {has_encoding}")
        if not has_encoding:
            print(f"  ⚠️ MISSING encoding='utf-8'!")

print("\n=== Also check Stage 1 and 2 write_text ===")
# Check stage_impls/_topic.py
topic_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_topic.py")
if topic_file.exists():
    content = topic_file.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'write_text' in line:
            has_encoding = 'encoding=' in line
            print(f"_topic.py Line {i+1}: {line.strip()[:80]}")
            print(f"  → encoding: {has_encoding}")

# Check stage_impls/_planning.py
planning_file = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_planning.py")
if planning_file.exists():
    content = planning_file.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'write_text' in line:
            has_encoding = 'encoding=' in line
            print(f"_planning.py Line {i+1}: {line.strip()[:80]}")
            print(f"  → encoding: {has_encoding}")