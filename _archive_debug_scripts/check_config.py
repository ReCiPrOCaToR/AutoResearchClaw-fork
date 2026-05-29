from pathlib import Path
import json

# Check what code_agent actually does
code_agent_script = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\stages\code_generation.py")

print("=== Stage 10 Configuration ===")
with open(r"D:\My_Project\AutoResearchClaw\config.yaml", 'r', encoding='utf-8') as f:
    print(f.read()[:3000])
