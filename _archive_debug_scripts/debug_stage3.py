"""Step-by-step reproduction of execute_stage for Stage 3."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from pathlib import Path
from researchclaw.config import RCConfig
from researchclaw.adapters import AdapterBundle
from researchclaw.pipeline.stages import Stage
from researchclaw.pipeline.executor import execute_stage, CONTRACTS
from researchclaw.llm import create_llm_client
import tempfile

# Load config
config = RCConfig.from_yaml(r"D:\My_Project\AutoResearchClaw\config.yaml")
print(f"✓ Config loaded")

# Create adapters
adapters = AdapterBundle()
print(f"✓ Adapters created")

# Create temp run directory
with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp) / "test-run"
    run_dir.mkdir()
    
    # Copy stage-01 outputs (goal.md is required)
    real_run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf")
    (run_dir / "stage-01").mkdir()
    (run_dir / "stage-02").mkdir()
    
    goal_src = real_run / "stage-01" / "goal.md"
    if goal_src.exists():
        (run_dir / "stage-01" / "goal.md").write_text(goal_src.read_text())
        print(f"✓ Copied goal.md from real run")
    else:
        print(f"✗ goal.md not found in {real_run/'stage-01'}")
        # Create a minimal goal.md
        (run_dir / "stage-01" / "goal.md").write_text("# Research Goal\n\nTopic: test\n")
        print(f"✓ Created minimal goal.md")
    
    # Stage 2 output not needed for Stage 3 input, but problem_tree.md is NOT needed
    
    # Create stage-03 directory manually to check if it's created by execute_stage
    stage3_dir = run_dir / "stage-03"
    
    print(f"\n=== About to call execute_stage ===")
    print(f"  Stage: {Stage.PROBLEM_DECOMPOSE} (value={int(Stage.PROBLEM_DECOMPOSE)})")
    print(f"  Run dir: {run_dir}")
    print(f"  Stage dir will be: {stage3_dir}")
    
    # Check contract
    contract = CONTRACTS[Stage.PROBLEM_DECOMPOSE]
    print(f"\nContract for Stage 3:")
    print(f"  Input files: {contract.input_files}")
    print(f"  Output files: {contract.output_files}")
    
    # Verify goal.md exists at expected path
    goal_path = run_dir / contract.input_files[0]
    print(f"\nChecking input file: {goal_path}")
    print(f"  Exists: {goal_path.exists()}")
    if goal_path.exists():
        print(f"  Content: {goal_path.read_text()[:100]}")
    
    # Now call execute_stage with full traceback
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
        print(f"  Stage dir contents: {list(stage3_dir.iterdir())}")
    except Exception as e:
        print(f"✗ EXCEPTION: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        print(f"\nStage dir after crash: {stage3_dir.exists()}")
        if stage3_dir.exists():
            print(f"  Contents: {list(stage3_dir.iterdir())}")
