import os

# Check for common API key environment variables
api_keys = {
    'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY'),
    'ANTHROPIC_API_KEY': os.environ.get('ANTHROPIC_API_KEY'),
    'DEEPSEEK_API_KEY': os.environ.get('DEEPSEEK_API_KEY'),
    'MINIMAX_API_KEY': os.environ.get('MINIMAX_API_KEY'),
    'GEMINI_API_KEY': os.environ.get('GEMINI_API_KEY'),
}

print("Available API keys:")
for key, value in api_keys.items():
    if value:
        status = "[OK]"
    else:
        status = "[NOT SET]"
    print(f"  {key}: {status}")

print("\nDefault LLM config from example:")
print("  provider: openai-compatible")
print("  base_url: https://api.openai.com/v1")
print("  primary_model: gpt-4o")
print("  api_key_env: OPENAI_API_KEY")
