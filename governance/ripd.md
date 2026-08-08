# RIPD — Relatório de Impacto à Proteção de Dados

> **Tipo de julgamento:** RIPD completo.
> **Por quê:** o sistema trata dados pessoais de titulares (usuários da plataforma).
> Art. 38 da LGPD exige RIPD quando há tratamento que possa gerar risco às liberdades
> civis e aos direitos fundamentais dos titulares.
>
> **Alvo:** danzeroum/mixlirous@658a6d3 (motor de remixagem de áudio guiado por IA).
> **Data:** 2026-08-07.

---

## 1. EXECUTIVE SUMMARY

O Mixlirous é um motor de remixagem algorítmica de áudio guiado por IA. Usuários enviam
gravações de áudio, descrevem a intenção em linguagem natural, e o sistema traduz em
parâmetros determinísticos de DSP, corta a faixa em blocos alinhados às batidas,
remonta e masteriza.

**Dados pessoais tratados:** e-mail, identificador de tenant, prompts de linguagem natural.
**Dados NÃO tratados:** o áudio de áudio NUNCA sai da máquina (modo local) e NUNCA é
enviado ao LLM — apenas o prompt textual e metadados.
**Risco principal:** prompt de usuário pode conter dado pessoal inadvertido enviado ao LLM
provedor (DeepSeek/OpenAI/Ollama).

---

## 2. INVENTÁRIO DE DADOS

| ID | Dado | Classificação | Finalidade | Base Legal | Componente |
|---|---|---|---|---|---|
| PD-001 | user_email | pessoal | Gestão de conta | execução de contrato | CMP-AUDIO-API |
| PD-002 | tenant_id | pessoal | Isolamento multitenant | execução de contrato | CMP-AUDIO-API |
| PD-003 | user_prompt | pessoal | Orquestração IA | legítimo interesse | CMP-AUDIO-AGENT |

**Armazenamento:**
- SQLite (laptop) ou PostgreSQL (VPS/multitenant)
- Áudio: disco local ou S3/MinIO via `object_store`
- Áudio NUNCA é enviado ao LLM (APENAS prompt textual e metadados)

---

## 3. BASES LEGAIS

| Dado | Base | Justificativa |
|---|---|---|
| user_email | execução de contrato | Necessário para autenticação e operação da conta |
| tenant_id | execução de contrato | Necessário para isolamento de dados entre organizações |
| user_prompt | legítimo interesse | Core do serviço — prompt é a entrada do usuário para o serviço solicitado |

**Atenção:** legímito interesse em prompts requer teste de equilíbrio (LGS). Prompt pode
conter dado pessoal inadvertido. Mitigação: sanitização de prompt (prompt_guard) e
aviso ao usuário sobre o que é enviado ao LLM.

---

## 4. MEDIDAS DE SEGURANÇA

| Medida | Onde | Estado |
|---|---|---|
| Autenticação JWT | `crates/audio_api/src/middleware/auth.rs` | implementado |
| Escopo de tenant | `crates/audio_api/src/middleware/tenant_scope.rs` | implementado |
| Sanitização de prompt | `crates/audio_agent/src/prompt_guard.rs` | planejado |
| OTel tracing | `crates/audio_api/src/middleware/otel.rs` | implementado |
| Escrita atômica de artefatos | `crates/audio_core/src/io/` | implementado |
| Hash SHA-256 de artefatos | Persistência de job | implementado |
| Container sandbox | `security/threat-model.yaml` | implementado |

---

## 5. RETENÇÃO E EXPURGO

| Dado | Política |
|---|---|
| user_email | Conta ativa + 30 dias após encerramento |
| tenant_id | Conta ativa + 30 dias após encerramento |
| user_prompt | Duração do job + 7 dias para debug |
| Áudio original | Até o usuário excluir ou encerrar a conta |
| Áudio processado (WAV) | Até o usuário excluir ou encerrar a conta |

---

## 6. DIREITOS DOS TITULARES

| Direito | Endpoint/Mecanismo | Estado |
|---|---|---|
| Acesso | `/api/v1/tenants/me` | implementado |
| Correção | pending_judgment | pendente |
| Exclusão | pending_judgment | pendente |
| Portabilidade | pending_judgment | pendente |
| Informação sobre compartilhamento | pending_judgment | pendente |
| Revogação de consentimento | pending_judgment | pendente |

**Observação:** os direitos de correção, exclusão e portabilidade estão como
`pending_judgment` pois dependem de implementação específica no backend.

---

## 7. RISCOS RESIDUAIS

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Prompt com dado pessoal enviado ao LLM | média | alto | Sanitização de prompt (prompt_guard), aviso ao usuário |
| Vazamento de áudio entre tenants | baixo | alto | Escopo de tenant isolado, testes de integração |
| Provedor LLM retém prompts | média | médio | Avaliação de provedor (LGPD), configuração de retention |
| Acesso não autorizado a jobs | baixo | médio | Auth JWT, escopo de tenant, rate limiting |

---

## 8. APROVAÇÃO

| Papel | Nome | Data | Veredito |
|---|---|---|--- |
| DPO | pending_judgment | — | pending_judgment |
| Responsável técnico | @danzeroum | 2026-08-07 | proposto |

---

## 9. ESCOPO NÃO AVALIADO

- Eficácia real das medidas de segurança em produção (não há ambiente de produção)
- Teste de equilíbrio (LGS) para legítimo interesse em prompts
- Adequação do provedor LLM (DeepSeek/OpenAI) à LGPD (transferência internacional de dados)
- Mecanismo de notificação de incidentes
