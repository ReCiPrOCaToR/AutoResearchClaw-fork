from pathlib import Path
import json

run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-043320-03dfbf")

print("=== checkpoint.json ===")
ckpt = run / "checkpoint.json"
if ckpt.exists():
    raw = ckpt.read_text()
    print(f"Raw ({len(raw)} chars): {raw[:500]}")

print("\n=== pipeline_summary.json ===")
summary = run / "pipeline_summary.json"
if summary.exists():
    raw = summary.read_text()
    print(f"Raw ({len(raw)} chars): {raw[:500]}")

print("\n=== heartbeat.json ===")
hb = run / "heartbeat.json"
if hb.exists():
    raw = hb.read_text()
    print(f"Raw ({len(raw)} chars): {raw[:500]}")

print("\n=== manifest.json ===")
manifest = run / "deliverables" / "manifest.json"
if manifest.exists():
    data = json.loads(manifest.read_text())
    print(json.dumps(data, indent=2)[:1000])
