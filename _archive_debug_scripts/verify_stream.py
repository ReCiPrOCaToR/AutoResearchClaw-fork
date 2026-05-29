import sys, json, os
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

# Patch verification - check that stream=false is set
from researchclaw.llm.client import LLMClient
import inspect

src = inspect.getsource(LLMClient._raw_call)
has_stream_false = 'body["stream"] = False' in src or "body['stream'] = False" in src
print(f"Patch present in _raw_call: {has_stream_false}")

# Also check the conditional branches
lines = src.split('\n')
for i, l in enumerate(lines):
    if 'if self._normalize_wire_api' in l:
        print(f"Line {i}: {l.strip()}")
        # Show next 5 lines
        for j in range(1,6):
            if i+j < len(lines):
                print(f"  +{j}: {lines[i+j].strip()}")

# Now check actual behavior by mocking a request
print("\n=== Checking branch decision ===")
# Create a dummy config to test
class DummyConfig:
    base_url = "https://api-inference.modelscope.cn/v1"
    wire_api = "chat_completions"
    api_key = "test"

c = LLMClient.__new__(LLMClient)
c.config = DummyConfig()
result = c._normalize_wire_api(c.config.wire_api)
print(f"wire_api '{c.config.wire_api}' normalizes to: {result!r}")
print(f"Will take 'responses' branch? {result == 'responses'}")
