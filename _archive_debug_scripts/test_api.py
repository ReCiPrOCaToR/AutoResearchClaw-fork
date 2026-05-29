import requests

API_KEY = "ms-c6e8ab49-dbd4-45a2-886a-3c7e96ef60d4"
BASE_URL = "https://api-inference.modelscope.cn/v1"
MODEL = "MiniMax/MiniMax-M2.5"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
payload = {"model": MODEL, "messages": [{"role": "user", "content": "Hello"}], "stream": False}

try:
    resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=30)
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        data = resp.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        print(f"SUCCESS! Content: {content[:100]}")
    else:
        print(f"Response: {resp.text[:300]}")
except Exception as e:
    print(f"Error: {e}")