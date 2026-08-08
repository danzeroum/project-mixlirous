import json
import yaml
from pathlib import Path

# Load inventory
with open('harness/state/code-inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

# Load current components
with open('architecture/components.yaml', 'r', encoding='utf-8') as f:
    doc = yaml.safe_load(f)

# Find test files
test_files = []
for mod in inv['modulos']:
    if mod['kind'] == 'test':
        test_files.append(mod['path'])

print(f"Found {len(test_files)} test files")

# Add test files to CMP-AUDIO-CORE's tested_by
for comp in doc['components']:
    if comp['id'] == 'CMP-AUDIO-CORE':
        comp['tested_by'] = sorted(set(test_files))
        break

# Write back
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Updated tested_by")
