"""Inspect RCConfig structure properly."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from researchclaw.config import RCConfig
import yaml

# Load YAML
with open(r"D:\My_Project\AutoResearchClaw\config.yaml", 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print("=== YAML data structure (top-level keys) ===")
print(f"Keys: {list(data.keys())}")
print(f"\nproject: {data.get('project')}")
print(f"Type: {type(data.get('project'))}")

# Check if RCConfig expects nested dataclasses
print(f"\n=== RCConfig annotations ===")
if hasattr(RCConfig, '__annotations__'):
    for key, val in RCConfig.__annotations__.items():
        print(f"  {key}: {val}")

# Try building with proper nested objects
from dataclasses import dataclass, field
from typing import Optional

# Maybe RCConfig uses nested config objects
print(f"\n=== Trying RCConfig(**data) ===")
try:
    config = RCConfig(**data)
    print(f"✓ Config created")
    # Try to access nested
    if hasattr(config, 'project'):
        proj = config.project
        if hasattr(proj, 'name'):
            print(f"  project.name: {proj.name}")
        else:
            print(f"  project is: {proj} (type: {type(proj)})")
    else:
        print(f"  No 'project' attribute")
        print(f"  Available attrs: {dir(config)[:10]}")
except Exception as e:
    print(f"✗ Failed: {e}")
    import traceback
    traceback.print_exc()
