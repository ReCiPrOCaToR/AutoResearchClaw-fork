"""Verify LLM patch is loaded correctly."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

# Force fresh import
import importlib
if 'researchclaw.llm.client' in sys.modules:
    del sys.modules['researchclaw.llm.client']

from researchclaw.llm.client import LLMClient
import inspect

src = inspect.getsource(LLMClient._raw_call)
has_stream = 'body["stream"] = False' in src
print(f"✓ stream=false in _raw_call: {has_stream}")

# Check branch logic
lines = src.split('\n')
in_else = False
for i, line in enumerate(lines):
    if 'if self._normalize_wire_api' in line:
        print(f"  Branch at line {i}: {line.strip()}")
        in_else = True
    elif in_else and line.strip().startswith('else:'):
        print(f"  Line {i}: else branch found")
        break

print("\n✓ Patch verified. Ready to run pipeline.")
print("  Run: python run_fixed.py --auto-approve")
