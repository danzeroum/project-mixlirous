import json
import yaml
from pathlib import Path

# Load inventory
with open('harness/state/code-inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

# Load current components
with open('architecture/components.yaml', 'r', encoding='utf-8') as f:
    doc = yaml.safe_load(f)

# Get all inventory paths
inv_paths = set()
for mod in inv['modulos']:
    inv_paths.add(mod['path'])

# Fix exemptions - add workspace/target/ prefix and verify they match
new_exemptions = []
for comp in doc['components']:
    pass  # exemptions are at the top level

# Current exemptions use paths without workspace/target/ prefix
# The inventory uses paths WITH workspace/target/ prefix
old_exemptions = doc.get('exemptions', [])

for ex in old_exemptions:
    old_path = ex['path']
    # Try adding workspace/target/ prefix
    new_path = f"workspace/target/{old_path}" if not old_path.startswith('workspace/target/') else old_path
    # Check if this path exists in inventory
    if new_path in inv_paths:
        new_exemptions.append({'path': new_path, 'justification': ex['justification']})
    else:
        # Try to find a matching path
        matches = [p for p in inv_paths if p.endswith(old_path)]
        for m in matches:
            new_exemptions.append({'path': m, 'justification': ex['justification']})

# Add exemptions for remaining non-code files that aren't covered
# Find all inventory files not covered by any component
covered = set()
for comp in doc['components']:
    for p in comp.get('source_paths', []):
        covered.add(p)
    for p in comp.get('tested_by', []):
        covered.add(p)

# Add exemptions for fixture/manifest files
for mod in inv['modulos']:
    path = mod['path']
    if path not in covered and not any(path.startswith(p) for p in covered if doc['components']):
        # Check if it's a non-code file that needs exemption
        if 'fixtures' in path or 'scripts' in path or path.endswith('.json') or path.endswith('.html'):
            # Already have exemptions for these directories
            pass

doc['exemptions'] = new_exemptions

# Write back
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print(f"Exemptions: {len(new_exemptions)}")
for ex in new_exemptions:
    print(f"  {ex['path']}")
