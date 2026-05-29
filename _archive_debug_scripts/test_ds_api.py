"""Quick test of DeepSeek API connection for AutoResearchClaw."""
import json
import urllib.request

url = "https://api.deepseek.com/v1/chat/completions"
api_key = "sk-e7c0656d90364db89c407d478baba6e4"

body = {
    "model": "deepseek-v4-pro",
    "messages": [
        {"role": "system", "content": "You are a helpful research assistant."},
        {"role": "user", "content": "Say 'DeepSeek API connection OK' in Chinese, one line only."}
    ],
    "max_tokens": 100,
    "temperature": 0.7,
    "stream": False
}

req = urllib.request.Request(
    url,
    data=json.dumps(body).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        content = result["choices"][0]["message"]["content"]
        model = result.get("model", "unknown")
        print(f"SUCCESS! Model: {model}")
        print(f"Content: {content}")
except Exception as e:
    print(f"FAILED: {e}")
