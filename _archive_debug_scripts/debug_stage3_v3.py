"""Fixed: reproduce Stage 3 crash using proper config loading."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from pathlib import Path
from researchclaw.config import RCConfig
from researchclaw.adapters import AdapterBundle
from researchclaw.pipeline.stages import Stage
from researchclaw.pipeline.executor import execute_stage, CONTRACTS
import tempfile

# Load config the RIGHT way (as used in cli.py)
print("Loading config with RCConfig.load()...")
config = RCConfig.load(r"D:\My_Project\AutoResearchClaw\config.yaml", check_paths=False)
print(f"✓ Config loaded")
print(f"  Project: {config.project.name}")
print(f"  Topic: {config.research.topic[:50]}")

# Create adapters
adapters = AdapterBundle()
print(f"✓ Adapters created, hitl={adapters.hitl}")

# Create temp run directory with stage-01 output
with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp) / "test-run"
    run_dir.mkdir()
    
    # Copy real stage-01 outputs
    real_run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf")
    (run_dir / "stage-01").mkdir()
    (run_dir / "stage-02").mkdir()
    
    goal_src = real_run / "stage-01" / "goal.md"
    if goal_src.exists():
        (run_dir / "stage-01" / "goal.md").write_text(goal_src.read_text())
        print(f"✓ Copied goal.md")
    else:
        print(f"✗ goal.md missing in {real_run/'stage-01'}")
        # List what's actually there
        print(f"  Actual contents: {list((real_run/'stage-01').iterdir())}")
        sys.exit(1)
    
    # Check input file for Stage 3
    contract = CONTRACTS[Stage.PROBLEM_DECOMPOSE]
    goal_input = run_dir / contract.input_files[0]
    print(f"\nInput file {contract.input_files[0]}: exists={goal_input.exists()}")
    
    # Call execute_stage
    print(f"\n=== Calling execute_stage for Stage {Stage.PROBLEM_DECOMPOSE} ===")
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
            print(f"  Stage dir files: {[f.name for f in stage3_dir.iterdir()]}")
    except Exception as e:
        print(f"✗ EXCEPTION: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        stage3_dir = run_dir / "stage-03"
        print(f"\nStage dir exists: {stage3_dir.exists()}")
        if stage3_dir.exists():
            print(f"  Contents: {[f.name for f in stage3_dir.iterdir()]}")
