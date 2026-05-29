# Check what API type ModelScope is configured to use
import yaml
with open(r"D:\My_Project\AutoResearchClaw\config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

print("=== Config ===")
print(f"LLM provider: {config.get('llm', {}).get('provider')}")
print(f"Base URL: {config.get('llm', {}).get('base_url')}")
print(f"Wire API: {config.get('llm', {}).get('wire_api', 'chat_completions')}")
print(f"API Key env: {config.get('llm', {}).get('api_key_env')}")

# Also check for any ModelScope specific settings
if 'models' in config:
    for model_name, model_cfg in config['models'].items():
        if 'modelscope' in model_name.lower() or 'stepfun' in model_name.lower():
            print(f"\nModel '{model_name}' config:")
            print(f"  {model_cfg}")
