import json
import yaml
from pathlib import Path

# Load inventory
with open('harness/state/code-inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

# Load current components
with open('architecture/components.yaml', 'r', encoding='utf-8') as f:
    doc = yaml.safe_load(f)

# Get test file paths from inventory
test_paths = set()
for mod in inv['modulos']:
    if mod['kind'] == 'test':
        test_paths.add(mod['path'])

# Fix each component: remove test files from source_paths
for comp in doc['components']:
    # Remove test paths from source_paths
    comp['source_paths'] = [p for p in comp.get('source_paths', []) if p not in test_paths]
    # Ensure tested_by has all test files for this component
    if comp['id'] == 'CMP-AUDIO-CORE':
        comp['tested_by'] = sorted(test_paths)

# Write back
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Fixed: removed test files from source_paths")
for comp in doc['components']:
    print(f"  {comp['id']}: {len(comp.get('source_paths', []))} src, {len(comp.get('tested_by', []))} test")
