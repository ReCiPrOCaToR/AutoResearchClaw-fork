# Check where LLMClient is instantiated for Stage 10
import subprocess
result = subprocess.run(
    ['find', '-name', 'executor.py', '-not', '-path', '*/__pycache__/*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print("Executor files:", result.stdout)

# Now grep for LLMClient instantiation
if result.stdout.strip():
    path = result.stdout.strip().split('\n')[0]
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    print(f"\n=== LLMClient creation in {path} ===")
    for i, line in enumerate(lines):
        if 'LLMClient(' in line or 'LLMClient.from_rc_config' in line:
            print(f"Line {i+1}: {line.rstrip()}")
            # Show context
            start = max(0, i-2)
            end = min(len(lines), i+8)
            for j in range(start, end):
                marker = ">>>" if j == i else "   "
                print(f"  {marker} {lines[j]}")
