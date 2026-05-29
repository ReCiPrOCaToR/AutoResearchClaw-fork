from pathlib import Path
import subprocess
import sys

# Check if opencode is installed
result = subprocess.run(
    ["opencode", "--version"],
    capture_output=True, text=True,
    timeout=10
)
print(f"OpenCode version check: rc={result.returncode}")
print(f"STDOUT: {result.stdout[:200]}")
print(f"STDERR: {result.stderr[:200]}")

# Check OpenCode config
home = Path.home()
opencode_config = home / ".opencode" / "config.json"
if opencode_config.exists():
    print(f"\nOpenCode config exists: {opencode_config}")
    print(opencode_config.read_text()[:500])
else:
    print(f"\nNo OpenCode config at {opencode_config}")

# Check if npm/opencode is available
npm_result = subprocess.run(["npm", "--version"], capture_output=True, text=True, timeout=10)
print(f"\nnpm version: {npm_result.stdout.strip() if npm_result.returncode==0 else 'not installed'}")
