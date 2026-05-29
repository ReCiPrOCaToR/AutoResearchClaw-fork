# Check if there are multiple copies of client.py
import subprocess
result = subprocess.run(
    ['find', '-name', 'client.py', '-path', '*llm*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print("client.py locations:")
for p in result.stdout.strip().split('\n'):
    print(f"  {p}")

# Check pycache
result2 = subprocess.run(
    ['find', '-name', 'client.*.pyc', '-o', '-name', '__pycache__*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print(f"\nPycache/client files: {len(result2.stdout.strip().split(chr(10)) if result2.stdout.strip() else 0)}")
