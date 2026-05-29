# Check if Stage 1 succeeded and if goal.md contains Chinese
from pathlib import Path

stage1 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-01")
print("=== Stage-01 contents ===")
if stage1.exists():
    for f in sorted(stage1.iterdir()):
        print(f"  {f.name} ({f.stat().st_size} bytes)")
        if f.is_file() and f.suffix in ('.md', '.txt', '.json'):
            try:
                content = f.read_text(encoding='utf-8')
                print(f"    First 200 chars: {content[:200]}")
            except Exception as e:
                print(f"    Error: {e}")

# Check Stage 2
stage2 = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-02")
print(f"\n=== Stage-02 contents ===")
if stage2.exists():
    for f in sorted(stage2.iterdir()):
        print(f"  {f.name} ({f.stat().st_size} bytes)")
        if f.is_file() and f.suffix in ('.md', '.txt', '.json'):
            try:
                content = f.read_text(encoding='utf-8')
                print(f"    First 200 chars: {content[:200]}")
            except Exception as e:
                print(f"    Error: {e}")
