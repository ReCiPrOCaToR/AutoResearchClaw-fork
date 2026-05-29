"""Test RC LLM client with new DeepSeek config."""
import sys
sys.path.insert(0, ".")

# Load RC config
from researchclaw.config import load_config
cfg = load_config("config.yaml")

# Setup LLM client
from researchclaw.llm.client import LLMConfig, LLMClient

llm_cfg = LLMConfig(
    base_url=cfg.llm.base_url,
    api_key=cfg.llm.api_key,
    wire_api=cfg.llm.wire_api,
    primary_model=cfg.llm.primary_model,
    fallback_models=cfg.llm.fallback_models,
    max_tokens=cfg.llm.max_tokens if hasattr(cfg.llm, 'max_tokens') else 4096,
    temperature=cfg.llm.temperature if hasattr(cfg.llm, 'temperature') else 0.7,
)

print(f"Base URL: {llm_cfg.base_url}")
print(f"Model: {llm_cfg.primary_model}")
print(f"Fallbacks: {llm_cfg.fallback_models}")
print(f"Wire API: {llm_cfg.wire_api}")

client = LLMClient(llm_cfg)
try:
    resp = client.chat(
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": "Say 'RC LLM client ready' in Chinese, one short line."}
        ],
        max_tokens=50,
        temperature=0.5
    )
    print(f"\nSUCCESS! Model used: {resp.model}")
    print(f"Content: {resp.content}")
    print(f"Tokens: {resp.total_tokens}")
except Exception as e:
    print(f"\nFAILED: {e}")
    import traceback
    traceback.print_exc()
