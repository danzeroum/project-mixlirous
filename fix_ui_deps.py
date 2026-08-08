import yaml

with open('architecture/components.yaml', 'r', encoding='utf-8') as f:
    doc = yaml.safe_load(f)

# Fix CMP-UI depends_on
for comp in doc['components']:
    if comp['id'] == 'CMP-UI':
        comp['depends_on'] = ['CMP-AUDIO-API']

with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Fixed CMP-UI depends_on")
