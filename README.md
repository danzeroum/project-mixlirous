# project-mixlirous

Gêmeo de governança de [danzeroum/mixlirous](https://github.com/danzeroum/mixlirous).

Este repositório **não é o mixlirous**. É o derivado que o governa: materializa o alvo em
`workspace/target/` (somente leitura, no SHA de `target.lock`), cartografa, avalia conformidade
e propõe mudanças — mas **nunca escreve no alvo**. Toda mudança no alvo nasce como achado aqui e
caminha para ele pelo fluxo natural do repositório adotante.

O ponto de partida:

> **O projeto declara configuração e autorização; o padrão fornece o motor e as verificações.**

## Papel

`project.yaml:project.kind: derived`. Este repositório é governado pela harness do molde
`danzeroum/project` (v1.0.0) e ancorado no alvo `danzeroum/mixlirous@658a6d3`.

## Estado

Nasce vermelho de propósito: coleções de metadados vazias aguardam `/ingerir`, o workspace
aguarda `/bootstrap`, e o atestado de proteção aguarda autoridade externa. O vermelho é o mapa
do trabalho, não um defeito.

## Comandos

| Comando | Quando |
|---|---|
| `/bootstrap` | Materializa `workspace/target/` no SHA ancorado e valida |
| `/ingerir` | Cartografa o alvo, preenche metadados, caminha do vermelho ao verde |
| `/sincronizar` | Reconcilia o derivado com o alvo quando o SHA muda |
| `/atualizar-carcaca` | Atualiza a casca do molde quando o derivado fica para trás |

## Regras

- NUNCA escreve no alvo. Só leitura, sempre.
- Toda mudança relevante vira change-proposal declarada ANTES de executar.
- Se um fiscal reprova, o vermelho é informação — não o contorne, resolva a causa.
