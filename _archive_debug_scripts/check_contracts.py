"""Check if CONTRACTS has entry for Stage.PROBLEM_DECOMPOSE."""
import sys
sys.path.insert(0, r"D:\My_Project\AutoResearchClaw")

from researchclaw.pipeline.contracts import CONTRACTS
from researchclaw.pipeline.stages import Stage

print("=== All CONTRACTS keys ===")
for stage in sorted(CONTRACTS.keys()):
    contract = CONTRACTS[stage]
    print(f"  Stage.{stage.name:25s} -> input_files={contract.input_files}, output_files={contract.output_files}")

print(f"\n=== Check PROBLEM_DECOMPOSE ===")
stage = Stage.PROBLEM_DECOMPOSE
print(f"Stage value: {int(stage)}")
print(f"In CONTRACTS: {stage in CONTRACTS}")
if stage in CONTRACTS:
    c = CONTRACTS[stage]
    print(f"  Input files: {c.input_files}")
    print(f"  Output files: {c.output_files}")
else:
    print("  ERROR: Missing contract for Stage 3!")
