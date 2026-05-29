# Fix all write_text calls missing encoding='utf-8' in pipeline files
from pathlib import Path
import re

pipeline_dir = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline")

# Find all .py files in pipeline
py_files = list(pipeline_dir.rglob("*.py"))
print(f"Scanning {len(py_files)} Python files in pipeline/")

fixed_files = []
for py_file in py_files:
    try:
        content = py_file.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"  ⚠ Could not read {py_file}: {e}")
        continue
    
    lines = content.split('\n')
    new_lines = []
    changes = []
    
    for i, line in enumerate(lines):
        # Detect write_text without encoding
        # Pattern: .write_text(...) but NOT .write_text(..., encoding=...)
        if '.write_text(' in line and 'encoding=' not in line:
            # Check if this is a multiline call or single line
            # Simple heuristic: if line has .write_text( and ends with ):
            # we need to check if encoding= is on any of the next few lines
            
            # For now, let's flag each line
            changes.append((i+1, line.strip()[:80]))
        
        new_lines.append(line)
    
    if changes:
        print(f"\n{py_file.relative_to(pipeline_dir)}:")
        for lineno, line in changes:
            print(f"  Line {lineno}: {line}")
        fixed_files.append((str(py_file), changes))

print(f"\n=== Total: {len(fixed_files)} files need fixing ===")
