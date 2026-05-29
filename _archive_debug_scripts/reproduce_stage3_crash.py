"""Reproduce Stage 3 crash to see the actual exception."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from pathlib import Path
from researchclaw.config import RCConfig
from researchclaw.llm import create_llm_client
from researchclaw.pipeline.stages import Stage
from researchclaw.pipeline.executor import execute_stage

# Load config
import yaml
with open(r"D:\My_Project\AutoResearchClaw\config.yaml", 'r', encoding='utf-8') as f:
    config_data = yaml.safe_load(f)

# Build RCConfig (simplified - use from_rc_config if available)
from researchclaw.config import RCConfig
config = RCConfig.from_yaml(r"D:\My_Project\AutoResearchClaw\config.yaml")

print(f"Config loaded: {config.project.name}")
print(f"Topic: {config.research.topic[:50]}")

# Create a dummy adapter bundle (minimal)
from researchclaw.adapters import AdapterBundle
adapters = AdapterBundle()  # May need proper init

# Create run directory (simulate)
run_id = "test-stage3-crash"
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp) / run_id
    run_dir.mkdir()
    # Copy prior artifacts from stage-01 and stage-02
    real_run = Path(r"D:\My_Project\AutoResearchClaw\artifacts\rc-20260413-061550-03dfbf")
    (run_dir / "stage-01").mkdir()
    (run_dir / "stage-02").mkdir()
    # Copy goal.md from stage-01 if exists
    goal_src = real_run / "stage-01" / "goal.md"
    if goal_src.exists():
        (run_dir / "stage-01" / "goal.md").write_text(goal_src.read_text())
    # Copy problem_tree.md from stage-02 if exists
    prob_src = real_run / "stage-02" / "problem_tree.md"
    if prob_src.exists():
        (run_dir / "stage-02" / "problem_tree.md").write_text(prob_src.read_text())

    stage_dir = run_dir / "stage-03"
    stage_dir.mkdir()

    print(f"\nAttempting Stage 3 execution...")
    print(f"Stage dir: {stage_dir}")

    try:
        result = execute_stage(
            Stage.PROBLEM_DECOMPOSE,
            run_dir=run_dir,
            run_id=run_id,
            config=config,
            adapters=adapters,
            auto_approve_gates=True,
        )
        print(f"✓ Stage succeeded: {result.status}")
        print(f"Artifacts: {result.artifacts}")
    except Exception as e:
        print(f"✗ CRASH: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
