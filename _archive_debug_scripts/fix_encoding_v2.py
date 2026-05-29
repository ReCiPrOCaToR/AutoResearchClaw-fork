"""Fix write_text calls missing encoding='utf-8' - line by line approach."""
from pathlib import Path
import re

pipeline_dir = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline")
py_files = list(pipeline_dir.rglob("*.py"))

total_fixes = 0
for py_file in py_files:
    try:
        lines = py_file.read_text(encoding='utf-8', errors='ignore').split('\n')
    except Exception:
        continue
    
    new_lines = []
    changes = 0
    
    for line in lines:
        # Find .write_text( that doesn't already have encoding=
        if '.write_text(' in line and 'encoding=' not in line:
            # Check if this line has an unclosed paren (multiline call)
            # Simple heuristic: if line ends with ( without ), it's multiline start
            # But most calls are single line: .write_text(content)
            
            # Replace pattern: .write_text(X) -> .write_text(encoding='utf-8', X)
            # Handle: .write_text(content) 
            # Handle: .write_text(content, extra_arg)
            
            # Find the inner content
            match = re.search(r'\.write_text\((.*)\)', line)
            if match:
                inner = match.group(1)
                if inner.strip():
                    new_inner = f"encoding='utf-8', {inner}"
                else:
                    new_inner = "encoding='utf-8'"
                new_line = re.sub(r'\.write_text\(.*\)', '.write_text(' + new_inner + ')', line)
                if new_line != line:
                    line = new_line
                    changes += 1
        
        new_lines.append(line)
    
    if changes > 0:
        py_file.write_text('\n'.join(new_lines), encoding='utf-8')
        print(f"Fixed {py_file.name}: {changes} calls")
        total_fixes += changes

print(f"\n=== TOTAL: {total_fixes} write_text calls fixed ===")
