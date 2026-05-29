import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

# Check if there's an Anthropic or Gemini adapter being used
from researchclaw.llm.client import LLMClient
import inspect

# Print the _raw_call method to see the full logic
source = inspect.getsource(LLMClient._raw_call)
print("=== Full _raw_call method ===")
print(source)
