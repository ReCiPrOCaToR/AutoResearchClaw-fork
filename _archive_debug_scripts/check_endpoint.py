# Check ModelScope endpoint URL construction
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\llm\client.py", 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

print("=== Endpoint path logic ===")
for i, line in enumerate(lines):
    if '_endpoint_path' in line or 'endpoint_url' in line:
        if 'def' in line:
            # Show the whole method
            for j in range(i, min(i+15, len(lines))):
                print(f"Line {j+1}: {lines[j]}")
        else:
            print(f"Line {i+1}: {line.strip()}")

print("\n=== Check what endpoint will be used ===")
base = "https://api-inference.modelscope.cn/v1"
for wire in ["chat_completions", "responses"]:
    norm = wire.replace("-", "_").lower()
    if norm in ("", "chat/completions", "chat_completions"):
        path = "/chat/completions"
    elif norm == "responses":
        path = "/responses"
    else:
        path = norm
    print(f"wire_api={wire!r} -> {base.rstrip('/')}{path}")
