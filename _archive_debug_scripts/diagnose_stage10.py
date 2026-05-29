import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

# Check which LLM path is used in Stage 10
from researchclaw.llm.client import LLMClient
import inspect

# Find the _raw_call body building section
source = inspect.getsource(LLMClient._raw_call)

# Check if stream is added in both branches
if '_build_responses_body' in source:
    print("Found _build_responses_body call")
    # Find that function
    source2 = inspect.getsource(LLMClient._build_responses_body)
    print("_build_responses_body source:")
    print(source2[:500])
else:
    print("No _build_responses_body found")

# Also check if there's a separate adapter for Anthropic/Gemini
try:
    from researchclaw.llm.anthropic import AnthropicAdapter
    print("\nAnthropic adapter exists")
except:
    print("\nNo Anthropic adapter")

try:
    from researchclaw.llm.gemini import GeminiAdapter
    print("Gemini adapter exists")
except:
    print("No Gemini adapter")

# Check if Stage 10 uses OpenCode
print("\n--- Checking if OpenCode is triggered ---")
with open(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline\stage_impls\_code_generation.py", 'r', encoding='utf-8') as f:
    stage_code = f.read()

# Search for OpenCode usage
if 'opencode' in stage_code.lower():
    print("Stage 10 references OpenCode")
    # Find relevant lines
    for i, line in enumerate(stage_code.split('\n')[:200]):
        if 'opencode' in line.lower() or 'OpenCode' in line:
            print(f"  Line {i+1}: {line}")
else:
    print("No OpenCode references in Stage 10")

# Check for code_agent usage
if 'code_agent' in stage_code.lower():
    print("\nStage 10 uses code_agent")
    for i, line in enumerate(stage_code.split('\n')[:200]):
        if 'code_agent' in line.lower():
            print(f"  Line {i+1}: {line}")
