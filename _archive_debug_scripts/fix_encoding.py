"""Fix all write_text calls missing encoding='utf-8' in pipeline files."""
from pathlib import Path
import re

pipeline_dir = Path(r"D:\My_Project\AutoResearchClaw\researchclaw\pipeline")
py_files = list(pipeline_dir.rglob("*.py"))

total_fixes = 0
fixed_files = []

for py_file in py_files:
    try:
        content = py_file.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        continue
    
    original = content
    
    # Pattern: find .write_text( followed eventually by ) but missing encoding=
    # We need to handle:
    # 1. Single line: (path).write_text(content)
    # 2. Multiline: (path).write_text(\n    content,\n)
    # 3. Multiline with other args: (path).write_text(content, some_arg)
    
    # Strategy: find each .write_text( and check if encoding= appears before the closing )
    # Simple regex replacement:
    # Replace .write_text( with .write_text(encoding='utf-8', 
    
    # But this is tricky for multiline. Let's try a simpler approach:
    # Find all occurrences and add encoding='utf-8' as first arg
    
    new_content = content
    changes = 0
    
    # Find all write_text( positions
    pattern = r'(\.write_text\()'
    
    for match in reversed(list(re.finditer(pattern, content))):
        pos = match.start()
        # Find the matching ) for this call
        # Start searching from pos + len('.write_text(')
        start_search = pos + len('.write_text(')
        depth = 1
        i = start_search
        while i < len(content) and depth > 0:
            if content[i] == '(':
                depth += 1
            elif content[i] == ')':
                depth -= 1
            i += 1
        
        # Now content[pos:i] is the full .write_text(...) call
        call = content[pos:i]
        
        # Check if encoding= is already in the call
        if 'encoding=' in call:
            continue
        
        # Build replacement: add encoding='utf-8' as first argument
        # .write_text(content) -> .write_text(encoding='utf-8', content)
        # .write_text(content, extra) -> .write_text(encoding='utf-8', content, extra)
        
        # Find the opening ( after .write_text
        first_paren = call.index('(')
        inner = call[first_paren+1:-1]  # content between ( and )
        
        if inner.strip():
            new_inner = f"encoding='utf-8', {inner}"
        else:
            new_inner = "encoding='utf-8'"
        
        new_call = '.write_text(' + new_inner + ')'
        new_content = new_content[:pos] + new_call + new_content[i:]
        changes += 1
    
    if changes > 0:
        py_file.write_text(new_content, encoding='utf-8')
        print(f"Fixed {py_file.name}: {changes} write_text calls")
        fixed_files.append((py_file.name, changes))
        total_fixes += changes

print(f"\n=== TOTAL: Fixed {total_fixes} write_text calls in {len(fixed_files)} files ===")
