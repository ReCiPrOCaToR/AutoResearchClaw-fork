import sys
import importlib.util
from pathlib import Path

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

spec = importlib.util.find_spec('researchclaw')
print(f"researchclaw installed: {spec is not None}")

root = Path(r"D:\My_Project\AutoResearchClaw")
print(f"\nProject root: {root}")
print(f"config.yaml exists: {root.joinpath('config.yaml').exists()}")
print(f"config.researchclaw.example.yaml exists: {root.joinpath('config.researchclaw.example.yaml').exists()}")

try:
    import researchclaw
    print(f"researchclaw version: {getattr(researchclaw, '__version__', 'unknown')}")
except ImportError as e:
    print(f"researchclaw import error: {e}")
