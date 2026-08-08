<!-- GENERATED: não editar; rodar ci/alignment_report.py -->
<!-- O --check do CI contradiz qualquer edição manual: edita-se a FONTE, não o derivado. -->
# Alinhamento entre departamentos

Matriz derivada do metadado declarado. Ela responde a pergunta que os demais fiscais não
fazem: **o que ficou de fora?**

## Cobertura de risco por capacidade

| Capacidade | risk_level | Riscos que a cobrem |
|---|---|---|
| `CAP-AGENT-ORCHESTRATION` | high | `RISK-SEC-001` |
| `CAP-DSP-ENGINE` | low | — |
| `CAP-HTTP-TRANSPORT` | medium | — |
| `CAP-LLM-PROVIDER` | high | `RISK-SEC-001` |
| `CAP-PERSISTENCE` | medium | — |
| `CAP-UI-PRESENTATION` | low | — |

## Componentes

| Componente | Status | Capacidade | Implementa | Coberto por risco |
|---|---|---|---|---|
| `CMP-AUDIO-AGENT` | implemented | `CAP-AGENT-ORCHESTRATION` | REQ-001 | não |
| `CMP-AUDIO-API` | implemented | `CAP-HTTP-TRANSPORT` | REQ-005, REQ-006 | não |
| `CMP-AUDIO-CORE` | implemented | `CAP-DSP-ENGINE` | REQ-002, REQ-003, REQ-004 | não |
| `CMP-UI` | implemented | `CAP-UI-PRESENTATION` | REQ-007 | não |

## Riscos por área

| Área | Total | Abertos |
|---|---|---|
| access | 3 | 0 |
| data | 2 | 0 |
| dependencies | 1 | 0 |
| governance | 16 | 3 |
| webqa | 1 | 0 |

## Pendências de alinhamento

Nenhuma. Todo ativo relevante está coberto ou tem isenção declarada.
