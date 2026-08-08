import json
import yaml
from pathlib import Path

# Load inventory
with open('harness/state/code-inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

# Get test file paths from inventory
test_paths = set()
for mod in inv['modulos']:
    if mod['kind'] == 'test':
        test_paths.add(mod['path'])

# Get code file paths (excluding test files)
code_files = {}
for mod in inv['modulos']:
    if mod['kind'] == 'code':
        path = mod['path']
        if path in test_paths:
            continue  # skip test files
        # Find which component this belongs to
        if 'crates/audio_core/' in path:
            code_files.setdefault('CMP-AUDIO-CORE', []).append(path)
        elif 'crates/audio_agent/' in path:
            code_files.setdefault('CMP-AUDIO-AGENT', []).append(path)
        elif 'crates/audio_api/' in path:
            code_files.setdefault('CMP-AUDIO-API', []).append(path)
        elif 'ui/' in path:
            code_files.setdefault('CMP-UI', []).append(path)

# Build components
doc = {
    'schema_version': '1.0',
    'metadata_version': '1.0',
    'source_of_truth': False,
    'generated_from': 'ingerir ING-03-CARTOGRAFIA',
    'components': [
        {
            'id': 'CMP-AUDIO-CORE',
            'kind': 'domain-module',
            'capability': 'CAP-DSP-ENGINE',
            'status': 'implemented',
            'source_paths': sorted(set(code_files.get('CMP-AUDIO-CORE', []))),
            'depends_on': [],
            'exposes': [
                'audio_core::domain::PipelineConfig',
                'audio_core::dsp::analysis::Analyzer',
                'audio_core::dsp::mastering::MasteringChain',
                'audio_core::ports::AudioAnalyzer',
                'audio_core::ports::AudioMixer',
                'audio_core::ports::AudioRepo',
                'audio_core::ports::Storage',
                'claim_next_job()',
                'update_status()',
                'put_object()',
                'get_object()',
            ],
            'tested_by': sorted(test_paths),
            'owner': 'engineering',
            'derived_from': {
                'repo': 'danzeroum/mixlirous',
                'sha': '658a6d34407232e70b512d71732cfdb62868140c',
                'path': 'docs/02-ARQUITETURA.md',
                'section': 'audio_core-dominio-dsp',
            },
        },
        {
            'id': 'CMP-AUDIO-AGENT',
            'kind': 'service',
            'capability': 'CAP-AGENT-ORCHESTRATION',
            'status': 'implemented',
            'source_paths': sorted(set(code_files.get('CMP-AUDIO-AGENT', []))),
            'depends_on': ['CMP-AUDIO-CORE'],
            'exposes': [
                'AudioToolDef',
                'ValidationLayer',
                'react_kernel::ReActLoop',
                'LlmProvider',
                'complete()',
                'stream()',
            ],
            'tested_by': [],
            'owner': 'engineering',
            'derived_from': {
                'repo': 'danzeroum/mixlirous',
                'sha': '658a6d34407232e70b512d71732cfdb62868140c',
                'path': 'docs/02-ARQUITETURA.md',
                'section': 'audio_agent-orquestracao-cognitiva',
            },
        },
        {
            'id': 'CMP-AUDIO-API',
            'kind': 'service',
            'capability': 'CAP-HTTP-TRANSPORT',
            'status': 'implemented',
            'source_paths': sorted(set(code_files.get('CMP-AUDIO-API', []))),
            'depends_on': ['CMP-AUDIO-CORE', 'CMP-AUDIO-AGENT'],
            'exposes': [
                'POST /api/v1/jobs',
                'GET /api/v1/jobs/:id',
                'GET /api/v1/jobs/:id/events',
                'GET /api/v1/tools',
                'GET /api/v1/tracks',
                'GET /api/v1/prompts',
                'GET /api/v1/tenants',
                'GET /api/v1/system',
                'agent.thought',
                'agent.error',
                'agent.proposal',
                'job.progress',
                'job.completed',
            ],
            'tested_by': [],
            'owner': 'engineering',
            'derived_from': {
                'repo': 'danzeroum/mixlirous',
                'sha': '658a6d34407232e70b512d71732cfdb62868140c',
                'path': 'docs/02-ARQUITETURA.md',
                'section': 'audio_api-transporte',
            },
        },
        {
            'id': 'CMP-UI',
            'kind': 'ui-surface',
            'capability': 'CAP-UI-PRESENTATION',
            'status': 'implemented',
            'source_paths': sorted(set(code_files.get('CMP-UI', []))),
            'depends_on': [],
            'exposes': [
                'RemixCanvas',
                'ProposalOverlay',
                'ParamStream',
            ],
            'tested_by': [],
            'owner': 'design',
            'derived_from': {
                'repo': 'danzeroum/mixlirous',
                'sha': '658a6d34407232e70b512d71732cfdb62868140c',
                'path': 'docs/02-ARQUITETURA.md',
                'section': 'ui-apresentacao',
            },
        },
    ],
    'exemptions': [
        {
            'path': p,
            'justification': 'Teste acústico/integração do motor DSP. Coberto por tested_by do componente mas check_orphan_code exige isenção explícita para arquivos de teste.',
        }
        for p in sorted(test_paths)
    ],
}

# Write with proper YAML formatting
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Rewritten components.yaml")
for comp in doc['components']:
    print(f"  {comp['id']}: {len(comp['source_paths'])} src, {len(comp['tested_by'])} test")
