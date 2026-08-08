import json
import yaml
from pathlib import Path

# Load inventory
with open('harness/state/code-inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

# Load current components
with open('architecture/components.yaml', 'r', encoding='utf-8') as f:
    doc = yaml.safe_load(f)

# Map: component crate/dir prefix -> list of file paths
crate_to_files = {}
for mod in inv['modulos']:
    if mod['kind'] != 'code':
        continue
    path = mod['path']
    # Find which crate this belongs to
    for prefix in ['workspace/target/crates/audio_core/',
                   'workspace/target/crates/audio_agent/',
                   'workspace/target/crates/audio_api/',
                   'workspace/target/ui/']:
        if path.startswith(prefix):
            crate_to_files.setdefault(prefix, []).append(path)
            break

# Map component -> crate prefix
comp_prefix_map = {
    'CMP-AUDIO-CORE': 'workspace/target/crates/audio_core/',
    'CMP-AUDIO-AGENT': 'workspace/target/crates/audio_agent/',
    'CMP-AUDIO-API': 'workspace/target/crates/audio_api/',
    'CMP-UI': 'workspace/target/ui/',
    'CMP-AUDIO-REPO': 'workspace/target/crates/audio_api/src/adapters/',
    'CMP-LLM-PROVIDER': 'workspace/target/crates/audio_agent/src/llm/',
}

# Update source_paths for each component
for comp in doc['components']:
    cid = comp['id']
    if cid in comp_prefix_map:
        prefix = comp_prefix_map[cid]
        files = crate_to_files.get(prefix, [])
        if files:
            comp['source_paths'] = sorted(set(files))

# Write back
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Updated source_paths from inventory")
for comp in doc['components']:
    print(f"  {comp['id']}: {len(comp.get('source_paths', []))} paths")
