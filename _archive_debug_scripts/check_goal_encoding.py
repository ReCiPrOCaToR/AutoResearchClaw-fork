"""Check actual goal.md encoding and content."""
from pathlib import Path

goal_path = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf\stage-01\goal.md")
print(f"File exists: {goal_path.exists()}")
print(f"File size: {goal_path.stat().st_size} bytes")

# Try reading with UTF-8
try:
    content = goal_path.read_text(encoding='utf-8')
    print("✓ UTF-8 read successful")
    print(f"First 200 chars:\n{content[:200]}")
except UnicodeDecodeError as e:
    print(f"✗ UTF-8 failed: {e}")
    # Try GBK
    try:
        content = goal_path.read_text(encoding='gbk')
        print("✓ GBK read successful (unexpected)")
    except:
        print("✗ GBK also failed")

# Check raw bytes
with open(goal_path, 'rb') as f:
    raw = f.read(100)
print(f"\nFirst 100 bytes (hex): {raw.hex()[:200]}")
