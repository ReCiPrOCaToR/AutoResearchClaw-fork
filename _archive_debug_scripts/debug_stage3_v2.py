"""Step-by-step reproduction of execute_stage for Stage 3 - fixed config loading."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from pathlib import Path
from researchclaw.config import RCConfig
from researchclaw.adapters import AdapterBundle
from researchclaw.pipeline.stages import Stage
from researchclaw.pipeline.executor import execute_stage, CONTRACTS
from researchclaw.llm import create_llm_client
import tempfile
import yaml

# Load config the same way run_fixed.py does
print("Loading config...")
with open(r"D:\My_Project\AutoResearchClaw\config.yaml", 'r', encoding='utf-8') as f:
    config_data = yaml.safe_load(f)

# RCConfig is likely a dataclass - construct directly
try:
    config = RCConfig(**config_data)
    print(f"✓ Config loaded via RCConfig(**data)")
except Exception as e:
    print(f"Direct construction failed: {e}")
    # Try alternative: use from_rc_config pattern from executor
    from researchclaw.llm.client import LLMClient
    candidate = LLMClient.from_rc_config(type('obj', (object,), config_data)())
    # This won't work - let's just use the yaml data directly
    sys.exit(1)

print(f"  Project: {config.project.name}")
print(f"  Topic: {config.research.topic[:50]}")

# Create adapters
adapters = AdapterBundle()
print(f"✓ Adapters created, hitl={adapters.hitl}")

# Create temp run directory
with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp) / "test-run"
    run_dir.mkdir()
    
    # Copy stage-01 outputs (goal.md is required input for Stage 3)
    real_run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf")
    (run_dir / "stage-01").mkdir()
    (run_dir / "stage-02").mkdir()
    
    goal_src = real_run / "stage-01" / "goal.md"
    if goal_src.exists():
        (run_dir / "stage-01" / "goal.md").write_text(goal_src.read_text())
        print(f"✓ Copied goal.md from real run")
    else:
        print(f"✗ goal.md not found in {real_run/'stage-01'}")
        # Check what IS in stage-01
        actual_stage1 = real_run / "stage-01"
        if actual_stage1.exists():
            print(f"  Actual stage-01 contents: {list(actual_stage1.iterdir())}")
        sys.exit(1)
    
    # Verify input file exists where execute_stage expects it
    contract = CONTRACTS[Stage.PROBLEM_DECOMPOSE]
    goal_input = run_dir / contract.input_files[0]
    print(f"\nInput file check: {goal_input}")
    print(f"  Exists: {goal_input.exists()}")
    if not goal_input.exists():
        print(f"  ✗ Missing required input! Stage will fail with 'Missing input'")
        # But that would still write stage_health.json - not a crash
        # So this is not the silent crash cause
    
    # Call execute_stage
    print(f"\n=== Calling execute_stage ===")
    try:
        result = execute_stage(
            Stage.PROBLEM_DECOMPOSE,
            run_dir=run_dir,
            run_id="test-stage3",
            config=config,
            adapters=adapters,
            auto_approve_gates=True,
        )
        print(f"✓ SUCCESS: {result.status}")
        print(f"  Artifacts: {result.artifacts}")
        stage3_dir = run_dir / "stage-03"
        if stage3_dir.exists():
            print(f"  Stage dir contents: {list(stage3_dir.iterdir())}")
    except Exception as e:
        print(f"✗ EXCEPTION: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        stage3_dir = run_dir / "stage-03"
        if stage3_dir.exists():
            print(f"Stage dir after crash exists: {list(stage3_dir.iterdir())}")
        else:
            print(f"Stage dir not created yet")
