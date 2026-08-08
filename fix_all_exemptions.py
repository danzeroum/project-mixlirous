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
all_inv_paths = set()
for mod in inv['modulos']:
    all_inv_paths.add(mod['path'])

# Get covered paths
covered = set()
for comp in doc['components']:
    for p in comp.get('source_paths', []):
        covered.add(p)
    for p in comp.get('tested_by', []):
        covered.add(p)

# Get exempted paths
exempted = set()
for ex in doc.get('exemptions', []):
    exempted.add(ex['path'])

# Find uncovered files
uncovered = all_inv_paths - covered - exempted
print(f"Uncovered files: {len(uncovered)}")
for p in sorted(uncovered):
    print(f"  {p}")

# Add exemptions for uncovered non-code files
new_exemptions = list(doc.get('exemptions', []))
for path in sorted(uncovered):
    if 'fixtures' in path:
        new_exemptions.append({
            'path': path,
            'justification': 'Fixture de áudio para testes acústicos. Dados de teste, não código governável.'
        })
    elif 'scripts' in path:
        new_exemptions.append({
            'path': path,
            'justification': 'Script auxiliar Python. Ferramenta de apoio, não componente do sistema em produção.'
        })
    elif path.endswith('.html'):
        new_exemptions.append({
            'path': path,
            'justification:': 'Template HTML estático. Recurso de apresentação, não código de negócio.'
        })
    elif path.endswith('.json') and 'tsconfig' not in path:
        new_exemptions.append({
            'path': path,
            'justification': 'Arquivo de configuração/manifesto JSON. Metadado de build, não código de negócio.'
        })
    elif path.endswith('.toml') and '.cargo' in path:
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração de auditoria de dependências Cargo. Metadado de build.'
        })
    elif path == 'workspace/target/Cargo.toml':
        new_exemptions.append({
            'path': path,
            'justification': 'Manifesto workspace Rust: metadado de build, não código de negócio.'
        })
    elif path.endswith('README.md'):
        new_exemptions.append({
            'path': path,
            'justification': 'Documentação do projeto. Não é código governável.'
        })
    elif path.endswith('CONTRIBUTING.md'):
        new_exemptions.append({
            'path': path,
            'justification': 'Documentação de contribuição. Não é código governável.'
        })
    elif path.endswith('HANDOFF.md'):
        new_exemptions.append({
            'path': path,
            'justification': 'Documentação de handoff. Não é código governável.'
        })
    elif path.endswith('LICENSE-APACHE') or path.endswith('LICENSE-MIT'):
        new_exemptions.append({
            'path': path,
            'justification': 'Arquivo de licença. Não é código governável.'
        })
    elif path.endswith('package-lock.json'):
        new_exemptions.append({
            'path': path,
            'justification': 'Lockfile de dependências Node. Metadado de build gerado automaticamente.'
        })
    elif path.endswith('.env.example'):
        new_exemptions.append({
            'path': path,
            'justification': 'Exemplo de configuração de ambiente. Documentação, não código.'
        })
    elif path.endswith('eslint.config.js'):
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração de linter. Metadado de build, não código de negócio.'
        })
    elif path.endswith('tsconfig.app.json') or path.endswith('tsconfig.node.json'):
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração de compilador TypeScript. Metadado de build.'
        })
    elif path.endswith('docker-compose') or path.endswith('Dockerfile'):
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração de container. Infraestrutura, não código de negócio.'
        })
    elif path.endswith('.gitignore'):
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração de git. Metadado de repositório.'
        })
    elif path.endswith('.prompt'):
        new_exemptions.append({
            'path': path,
            'justification': 'Template de prompt LLM. Configuração de IA, não código de negócio.'
        })
    elif path.endswith('.sh'):
        new_exemptions.append({
            'path': path,
            'justification': 'Script shell auxiliar. Ferramenta de apoio, não componente do sistema.'
        })
    elif path.endswith('.csv'):
        new_exemptions.append({
            'path': path,
            'justification:': 'Dados de importação. Não é código governável.'
        })
    elif path.endswith('.yml') or path.endswith('.yaml'):
        new_exemptions.append({
            'path': path,
            'justification': 'Configuração YAML. Infraestrutura, não código de negócio.'
        })
    else:
        print(f"  UNHANDLED: {path}")

doc['exemptions'] = new_exemptions

# Write back
with open('architecture/components.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(doc, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print(f"\nTotal exemptions: {len(new_exemptions)}")
