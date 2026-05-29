"""Diagnose Stage 10 failure: is stream=false applied to ALL LLM calls?"""
from pathlib import Path
import sys

# Import the actual LLMClient
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")
from researchclaw.llm.client import LLMClient

# Check the _raw_call method source
import inspect
src = inspect.getsource(LLMClient._raw_call)
print("=== LLMClient._raw_call source ===")
print(src[:2000])
print("\n... (rest of method)")

# Check if 'stream' appears
if '"stream"' in src or "'stream'" in src:
    print("\n✓ Found stream parameter in _raw_call")
else:
    print("\n✗ NO stream parameter in _raw_call")

# Also check chat() method
chat_src = inspect.getsource(LLMClient.chat)
print("\n=== LLMClient.chat source (first 1000 chars) ===")
print(chat_src[:1000])
