import yaml

data_inventory = {
    'schema_version': '1.0',
    'metadata_version': '1.0',
    'source_of_truth': False,
    'generated_from': 'ingerir ING-06-GOVERNANCA',
    'controller': {
        'role': 'controller',
        'name': 'danzeroum',
        'dpo_contact': 'pending_judgment',
    },
    'purposes': [
        {
            'id': 'PURP-001',
            'name': 'Processamento de remixagem de áudio',
            'description': 'Recorte, remontagem e masterização de áudio enviado pelo usuário.',
        },
        {
            'id': 'PURP-002',
            'name': 'Orquestração de agente IA',
            'description': 'Tradução de intenção em linguagem natural para parâmetros de DSP via LLM.',
        },
        {
            'id': 'PURP-003',
            'name': 'Gestão de conta e tenant',
            'description': 'Autenticação, autorização e isolamento multitenant.',
        },
    ],
    'fields': [
        {
            'id': 'PD-001',
            'name': 'user_email',
            'classification': 'pessoal',
            'purpose': 'PURP-003',
            'legal_basis': 'execucao_contrato',
            'owning_component': 'CMP-AUDIO-API',
            'locations': ['crates/audio_api/src/middleware/auth.rs'],
            'retention': {
                'policy': 'Conta ativa + 30 dias após encerramento',
            },
        },
        {
            'id': 'PD-002',
            'name': 'tenant_id',
            'classification': 'pessoal',
            'purpose': 'PURP-003',
            'legal_basis': 'execucao_contrato',
            'owning_component': 'CMP-AUDIO-API',
            'locations': ['crates/audio_api/src/middleware/tenant_scope.rs'],
            'retention': {
                'policy': 'Conta ativa + 30 dias após encerramento',
            },
        },
        {
            'id': 'PD-003',
            'name': 'user_prompt',
            'classification': 'pessoal',
            'purpose': 'PURP-002',
            'legal_basis': 'legitimo_interesse',
            'owning_component': 'CMP-AUDIO-AGENT',
            'locations': ['crates/audio_agent/src/prompt_loader.rs'],
            'retention': {
                'policy': 'Duração do job + 7 dias para debug',
            },
        },
    ],
    'subject_rights': {
        'access': '/api/v1/tenants/me',
        'correction': 'pending_judgment',
        'deletion': 'pending_judgment',
        'portability': 'pending_judgment',
    },
    'scan': {
        'last_run': '2026-08-07T00:00:00Z',
        'adapter': 'generico',
        'exclusions': [],
    },
}

with open('governance/data-inventory.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data_inventory, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Created data-inventory.yaml")
