"""Find how RCConfig is loaded in the actual run command."""
import subprocess
result = subprocess.run(
    ['find', '-name', 'run.py', '-path', '*researchclaw*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print("run.py locations:")
print(result.stdout)

# Also check __main__.py
result2 = subprocess.run(
    ['find', '-name', '__main__.py', '-path', '*researchclaw*'],
    capture_output=True, text=True,
    cwd=r'D:\My_Project\AutoResearchClaw'
)
print("\n__main__.py locations:")
print(result2.stdout)
