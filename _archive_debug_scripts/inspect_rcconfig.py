# Check RCConfig.load method
from pathlib import Path
import inspect

from researchclaw.config import RCConfig

print("=== RCConfig methods ===")
for name, method in inspect.getmembers(RCConfig, predicate=inspect.isfunction):
    print(f"  {name}")

print("\n=== RCConfig.load signature (if exists) ===")
if hasattr(RCConfig, 'load'):
    sig = inspect.signature(RCConfig.load)
    print(f"  load{sig}")
else:
    print("  No .load() method")

# Check if RCConfig has __init__ that converts dicts
print("\n=== RCConfig __init__ ===")
sig = inspect.signature(RCConfig.__init__)
print(f"  __init__{sig}")

# Show the source of RCConfig class (first 100 lines)
print("\n=== RCConfig class source (first 80 lines) ===")
try:
    source = inspect.getsource(RCConfig)
    lines = source.split('\n')[:80]
    for line in lines:
        print(f"  {line}")
except Exception as e:
    print(f"  Error: {e}")
