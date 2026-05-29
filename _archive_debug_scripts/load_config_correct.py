"""Correctly load RCConfig from config.yaml."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from pathlib import Path
from researchclaw.config import RCConfig
import yaml

# Load YAML
config_path = Path(r"D:\My_Project\AutoResearchClaw\config.yaml")
with config_path.open('r', encoding='utf-8') as f:
    config_data = yaml.safe_load(f)

# RCConfig likely uses dataclass or similar - try constructing directly
try:
    # Try using from_dict or similar
    if hasattr(RCConfig, 'from_dict'):
        config = RCConfig.from_dict(config_data)
    elif hasattr(RCConfig, 'parse_obj'):
        config = RCConfig.parse_obj(config_data)
    else:
        # Try direct construction - RCConfig is likely a dataclass
        config = RCConfig(**config_data)
except Exception as e:
    print(f"Direct construction failed: {e}")
    # Fallback: check what RCConfig expects
    import inspect
    sig = inspect.signature(RCConfig.__init__)
    print(f"RCConfig.__init__ signature: {sig}")
    sys.exit(1)

print(f"✓ Config loaded successfully")
print(f"  Project: {config.project.name}")
print(f"  Topic: {config.research.topic[:50]}")
print(f"  LLM provider: {config.llm.provider}")
print(f"  LLM base_url: {config.llm.base_url}")
print(f"  LLM model: {config.llm.primary_model}")

# Now try creating LLM client
from researchclaw.llm import create_llm_client
try:
    llm = create_llm_client(config)
    print(f"✓ LLM client created: {llm}")
except Exception as e:
    print(f"✗ LLM client creation failed: {e}")
    import traceback
    traceback.print_exc()
