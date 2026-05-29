import requests
import json

API_KEY = "ms-c6e8ab49-dbd4-45a2-886a-3c7e96ef60d4"
BASE_URL = "https://api-inference.modelscope.cn/v1"
MODEL = "MiniMax/MiniMax-M2.5"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Test 1: Normal request
payload1 = {"model": MODEL, "messages": [{"role": "user", "content": "Say hello"}], "stream": False}
resp1 = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload1, timeout=30)
print(f"Test 1 (normal): {resp1.status_code}")
if resp1.status_code == 200:
    print(f"  Content: {resp1.json()['choices'][0]['message']['content'][:50]}")
else:
    print(f"  Error: {resp1.text[:200]}")

# Test 2: With response_format json_object
payload2 = {"model": MODEL, "messages": [{"role": "user", "content": "Return JSON: {\"name\": \"test\"}"}], "stream": False, "response_format": {"type": "json_object"}}
resp2 = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload2, timeout=30)
print(f"\nTest 2 (json_object): {resp2.status_code}")
print(f"  Response: {resp2.text[:300]}")