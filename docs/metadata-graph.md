<!-- GENERATED: não editar; rodar ci/generate_graph.py -->
# Mapa de relacionamento dos metadados

> Artefato DERIVADO dos metadados reais, não fonte de verdade. Editar aqui é trabalho
> perdido: o `--check` do CI contradiz a edição na hora mais cara.

Legenda: azul-escuro = projeto · azul = capacidade (`CAP-`) · ciano = componente (`CMP-`) ·
roxo = interface (`IFC-`) · verde = regra (`RULE-`) · rosa = superfície de UI (`UI-`) ·
amarelo = ADR · vermelho = risco (`RISK-`).

```mermaid
graph TD
  PROJ_danzeroum_project_mixlirous["danzeroum-project-mixlirous"]
  TEST_workspace_target_crates_audio_core_tests_aliasing_rs{{"aliasing.rs"}}
  TEST_workspace_target_crates_audio_core_tests_crossfade_properties_rs{{"crossfade_properties.rs"}}
  TEST_workspace_target_crates_audio_core_tests_dc_offset_proptest_regressions{{"dc_offset.proptest-regressions"}}
  TEST_workspace_target_crates_audio_core_tests_dc_offset_rs{{"dc_offset.rs"}}
  TEST_workspace_target_crates_audio_core_tests_fixtures_manifest_rs{{"fixtures_manifest.rs"}}
  TEST_workspace_target_crates_audio_core_tests_generators_rs{{"generators.rs"}}
  TEST_workspace_target_crates_audio_core_tests_homogeneity_rs{{"homogeneity.rs"}}
  TEST_workspace_target_crates_audio_core_tests_idempotence_rs{{"idempotence.rs"}}
  TEST_workspace_target_crates_audio_core_tests_latency_rs{{"latency.rs"}}
  TEST_workspace_target_crates_audio_core_tests_neutral_bypass_rs{{"neutral_bypass.rs"}}
  TEST_workspace_target_crates_audio_core_tests_thd_rs{{"thd.rs"}}
  CAP_AGENT_ORCHESTRATION["CAP-AGENT-ORCHESTRATION<br/>Orquestração cognitiva do agente de IA (ReAct)"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_AGENT_ORCHESTRATION
  CAP_DSP_ENGINE["CAP-DSP-ENGINE<br/>Motor de DSP para remixagem de áudio"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_DSP_ENGINE
  CAP_HTTP_TRANSPORT["CAP-HTTP-TRANSPORT<br/>Transporte HTTP e SSE da API"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_HTTP_TRANSPORT
  CAP_LLM_PROVIDER["CAP-LLM-PROVIDER<br/>Abstração de provedor LLM (OpenAI/Ollama/DeepSeek)"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_LLM_PROVIDER
  CAP_PERSISTENCE["CAP-PERSISTENCE<br/>Persistência dual (SQLite/PostgreSQL)"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_PERSISTENCE
  CAP_UI_PRESENTATION["CAP-UI-PRESENTATION<br/>Interface de usuário (canvas, overlay, streaming)"]
  PROJ_danzeroum_project_mixlirous -->|capacidade| CAP_UI_PRESENTATION
  CMP_AUDIO_AGENT["CMP-AUDIO-AGENT<br/>Cargo.toml"]
  CMP_AUDIO_AGENT -->|realiza| CAP_AGENT_ORCHESTRATION
  CMP_AUDIO_AGENT -->|depende| CMP_AUDIO_CORE
  CMP_AUDIO_API["CMP-AUDIO-API<br/>Cargo.toml"]
  CMP_AUDIO_API -->|realiza| CAP_HTTP_TRANSPORT
  CMP_AUDIO_API -->|depende| CMP_AUDIO_AGENT
  CMP_AUDIO_API -->|depende| CMP_AUDIO_CORE
  CMP_AUDIO_CORE["CMP-AUDIO-CORE<br/>Cargo.toml"]
  CMP_AUDIO_CORE -->|realiza| CAP_DSP_ENGINE
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_aliasing_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_crossfade_properties_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_dc_offset_proptest_regressions
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_dc_offset_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_fixtures_manifest_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_generators_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_homogeneity_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_idempotence_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_latency_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_neutral_bypass_rs
  CMP_AUDIO_CORE -.->|testa| TEST_workspace_target_crates_audio_core_tests_thd_rs
  CMP_UI["CMP-UI<br/>eslint.config.js"]
  CMP_UI -->|realiza| CAP_UI_PRESENTATION
  CMP_UI -->|depende| CMP_AUDIO_API
  IFC_API_HTTP(["IFC-API-HTTP<br/>API HTTP REST"])
  CMP_AUDIO_API -.->|provê| IFC_API_HTTP
  IFC_API_HTTP -.->|consome| CMP_UI
  IFC_API_SSE(["IFC-API-SSE<br/>Stream de eventos SSE"])
  CMP_AUDIO_API -.->|provê| IFC_API_SSE
  IFC_API_SSE -.->|consome| CMP_UI
  IFC_AUDIO_ANALYZER(["IFC-AUDIO-ANALYZER<br/>Porta de análise de áudio"])
  CMP_AUDIO_CORE -.->|provê| IFC_AUDIO_ANALYZER
  IFC_AUDIO_ANALYZER -.->|consome| CMP_AUDIO_AGENT
  IFC_AUDIO_MIXER(["IFC-AUDIO-MIXER<br/>Porta de mixagem e masterização"])
  CMP_AUDIO_CORE -.->|provê| IFC_AUDIO_MIXER
  IFC_AUDIO_MIXER -.->|consome| CMP_AUDIO_AGENT
  IFC_AUDIO_REPO(["IFC-AUDIO-REPO<br/>Porta de persistência de áudio"])
  CMP_AUDIO_CORE -.->|provê| IFC_AUDIO_REPO
  IFC_AUDIO_REPO -.->|consome| CMP_AUDIO_API
  IFC_LLM_PROVIDER(["IFC-LLM-PROVIDER<br/>Porta de provedor LLM"])
  CMP_AUDIO_AGENT -.->|provê| IFC_LLM_PROVIDER
  IFC_LLM_PROVIDER -.->|consome| CMP_AUDIO_API
  IFC_STORAGE(["IFC-STORAGE<br/>Porta de armazenamento de objetos"])
  CMP_AUDIO_CORE -.->|provê| IFC_STORAGE
  IFC_STORAGE -.->|consome| CMP_AUDIO_API
  MET_ACTIVATION[["MET-ACTIVATION"]]
  MET_AOV[["MET-AOV"]]
  MET_DISCOVERY[["MET-DISCOVERY"]]
  REQ_001["REQ-001<br/>in_progress"]
  REQ_001 -->|requisito| CAP_AGENT_ORCHESTRATION
  REQ_002["REQ-002<br/>done"]
  REQ_002 -->|requisito| CAP_DSP_ENGINE
  REQ_003["REQ-003<br/>done"]
  REQ_003 -->|requisito| CAP_DSP_ENGINE
  REQ_004["REQ-004<br/>done"]
  REQ_004 -->|requisito| CAP_DSP_ENGINE
  REQ_005["REQ-005<br/>done"]
  REQ_005 -->|requisito| CAP_HTTP_TRANSPORT
  REQ_006["REQ-006<br/>done"]
  REQ_006 -->|requisito| CAP_HTTP_TRANSPORT
  REQ_007["REQ-007<br/>done"]
  REQ_007 -->|requisito| CAP_UI_PRESENTATION
  REQ_008["REQ-008<br/>planned"]
  REQ_008 -->|requisito| CAP_LLM_PROVIDER
  RISK_ALIGN_001["RISK-ALIGN-001"]
  RISK_APPROVAL_001["RISK-APPROVAL-001"]
  RISK_CHANGE_001["RISK-CHANGE-001"]
  RISK_CHANGE_002["RISK-CHANGE-002"]
  RISK_CONF_001["RISK-CONF-001"]
  RISK_CONF_002["RISK-CONF-002"]
  RISK_DECISION_001["RISK-DECISION-001"]
  RISK_DEP_001["RISK-DEP-001"]
  RISK_DERIV_001["RISK-DERIV-001"]
  RISK_DERIV_002["RISK-DERIV-002"]
  RISK_EXT_001["RISK-EXT-001"]
  RISK_INCUBA_001["RISK-INCUBA-001"]
  RISK_INGEST_001["RISK-INGEST-001"]
  RISK_INGEST_002["RISK-INGEST-002"]
  RISK_META_001["RISK-META-001"]
  RISK_META_002["RISK-META-002"]
  RISK_MOLD_001["RISK-MOLD-001"]
  RISK_ORIENT_001["RISK-ORIENT-001"]
  RISK_PRIV_001["RISK-PRIV-001"]
  RISK_PRIV_002["RISK-PRIV-002"]
  RISK_SEC_001["RISK-SEC-001"]
  RISK_STAGE_001["RISK-STAGE-001"]
  RISK_WEBQA_001["RISK-WEBQA-001"]
  ADR_001["ADR-001"]
  ADR_001 -->|mitiga| RISK_WEBQA_001
  ADR_002["ADR-002"]
  ADR_002 -->|mitiga| RISK_META_001
  ADR_003["ADR-003"]
  ADR_003 -->|mitiga| RISK_DEP_001
  ADR_004["ADR-004"]
  ADR_004 -->|mitiga| RISK_CHANGE_001
  ADR_005["ADR-005"]
  ADR_006["ADR-006"]
  ADR_006 -->|mitiga| RISK_CONF_001
  ADR_006 -->|mitiga| RISK_STAGE_001
  ADR_007["ADR-007"]
  ADR_007 -->|mitiga| RISK_PRIV_001
  ADR_007 -->|mitiga| RISK_PRIV_002
  ADR_008["ADR-008"]
  ADR_008 -->|mitiga| RISK_DERIV_001
  ADR_008 -->|mitiga| RISK_DERIV_002
  ADR_009["ADR-009"]
  ADR_009 -->|mitiga| RISK_DERIV_002
  ADR_009 -->|mitiga| RISK_INGEST_001
  ADR_010["ADR-010"]
  ADR_010 -->|mitiga| RISK_INGEST_001
  ADR_010 -->|mitiga| RISK_INGEST_002
  ADR_011["ADR-011"]
  ADR_011 -->|mitiga| RISK_ALIGN_001
  ADR_012["ADR-012"]
  ADR_012 -->|mitiga| RISK_CONF_002
  ADR_012 -->|mitiga| RISK_DERIV_001
  ADR_013["ADR-013"]
  ADR_013 -->|mitiga| RISK_DEP_001
  ADR_013 -->|mitiga| RISK_SEC_001
  ADR_014["ADR-014"]
  ADR_014 -->|mitiga| RISK_META_001
  ADR_014 -->|mitiga| RISK_ORIENT_001
  ADR_015["ADR-015"]
  ADR_015 -->|mitiga| RISK_DERIV_001
  ADR_015 -->|mitiga| RISK_MOLD_001
  ADR_016["ADR-016"]
  ADR_016 -->|mitiga| RISK_CHANGE_001
  ADR_016 -->|mitiga| RISK_META_001
  ADR_017["ADR-017"]
  ADR_017 -->|mitiga| RISK_CONF_001
  ADR_017 -->|mitiga| RISK_DECISION_001
  ADR_018["ADR-018"]
  ADR_018 -->|mitiga| RISK_DEP_001
  ADR_018 -->|mitiga| RISK_SEC_001
  ADR_019["ADR-019"]
  ADR_019 -->|mitiga| RISK_CONF_001
  ADR_019 -->|mitiga| RISK_META_001
  ADR_020["ADR-020"]
  ADR_020 -->|mitiga| RISK_EXT_001
  ADR_020 -->|mitiga| RISK_META_002
  ADR_021["ADR-021"]
  ADR_021 -->|mitiga| RISK_META_001
  ADR_021 -->|mitiga| RISK_PRIV_001
  ADR_022["ADR-022"]
  ADR_022 -->|mitiga| RISK_META_001
  ADR_022 -->|mitiga| RISK_ORIENT_001
  ADR_023["ADR-023"]
  ADR_023 -->|mitiga| RISK_DEP_001
  ADR_023 -->|mitiga| RISK_META_001
  ADR_024["ADR-024"]
  ADR_024 -->|mitiga| RISK_CONF_001
  ADR_024 -->|mitiga| RISK_DEP_001
  ADR_025["ADR-025"]
  ADR_025 -->|mitiga| RISK_CONF_001
  ADR_025 -->|mitiga| RISK_EXT_001
  ADR_025 -->|mitiga| RISK_MOLD_001
  ADR_026["ADR-026"]
  ADR_026 -->|mitiga| RISK_CONF_001
  ADR_026 -->|mitiga| RISK_DERIV_002
  ADR_026 -->|mitiga| RISK_MOLD_001
  ADR_027["ADR-027"]
  ADR_027 -->|mitiga| RISK_CHANGE_001
  ADR_027 -->|mitiga| RISK_CHANGE_002
  ADR_028["ADR-028"]
  ADR_028 -->|mitiga| RISK_EXT_001
  ADR_028 -->|mitiga| RISK_META_002
  ADR_029["ADR-029"]
  ADR_029 -->|mitiga| RISK_EXT_001
  ADR_029 -->|mitiga| RISK_META_002
  ADR_030["ADR-030"]
  ADR_030 -->|mitiga| RISK_CONF_001
  ADR_030 -->|mitiga| RISK_SEC_001
  ADR_030 -->|mitiga| RISK_WEBQA_001
  ADR_031["ADR-031"]
  ADR_031 -->|mitiga| RISK_META_001
  ADR_031 -->|mitiga| RISK_ORIENT_001
  classDef project fill:#1f2937,stroke:#111827,color:#fff;
  class PROJ_danzeroum_project_mixlirous project;
  classDef cap fill:#2563eb,stroke:#1e40af,color:#fff;
  class CAP_AGENT_ORCHESTRATION,CAP_DSP_ENGINE,CAP_HTTP_TRANSPORT,CAP_LLM_PROVIDER,CAP_PERSISTENCE,CAP_UI_PRESENTATION cap;
  classDef cmp fill:#0891b2,stroke:#0e7490,color:#fff;
  class CMP_AUDIO_AGENT,CMP_AUDIO_API,CMP_AUDIO_CORE,CMP_UI cmp;
  classDef ifc fill:#7c3aed,stroke:#5b21b6,color:#fff;
  class IFC_API_HTTP,IFC_API_SSE,IFC_AUDIO_ANALYZER,IFC_AUDIO_MIXER,IFC_AUDIO_REPO,IFC_LLM_PROVIDER,IFC_STORAGE ifc;
  classDef rule fill:#16a34a,stroke:#15803d,color:#fff;
  classDef ui fill:#db2777,stroke:#9d174d,color:#fff;
  classDef req fill:#0d9488,stroke:#0f766e,color:#fff;
  class REQ_001,REQ_002,REQ_003,REQ_004,REQ_005,REQ_006,REQ_007,REQ_008 req;
  classDef met fill:#ea580c,stroke:#c2410c,color:#fff;
  class MET_ACTIVATION,MET_AOV,MET_DISCOVERY met;
  classDef test fill:#57534e,stroke:#44403c,color:#fff;
  class TEST_workspace_target_crates_audio_core_tests_aliasing_rs,TEST_workspace_target_crates_audio_core_tests_crossfade_properties_rs,TEST_workspace_target_crates_audio_core_tests_dc_offset_proptest_regressions,TEST_workspace_target_crates_audio_core_tests_dc_offset_rs,TEST_workspace_target_crates_audio_core_tests_fixtures_manifest_rs,TEST_workspace_target_crates_audio_core_tests_generators_rs,TEST_workspace_target_crates_audio_core_tests_homogeneity_rs,TEST_workspace_target_crates_audio_core_tests_idempotence_rs,TEST_workspace_target_crates_audio_core_tests_latency_rs,TEST_workspace_target_crates_audio_core_tests_neutral_bypass_rs,TEST_workspace_target_crates_audio_core_tests_thd_rs test;
  classDef adr fill:#ca8a04,stroke:#a16207,color:#fff;
  class ADR_001,ADR_002,ADR_003,ADR_004,ADR_005,ADR_006,ADR_007,ADR_008,ADR_009,ADR_010,ADR_011,ADR_012,ADR_013,ADR_014,ADR_015,ADR_016,ADR_017,ADR_018,ADR_019,ADR_020,ADR_021,ADR_022,ADR_023,ADR_024,ADR_025,ADR_026,ADR_027,ADR_028,ADR_029,ADR_030,ADR_031 adr;
  classDef risk fill:#dc2626,stroke:#991b1b,color:#fff;
  class RISK_ALIGN_001,RISK_APPROVAL_001,RISK_CHANGE_001,RISK_CHANGE_002,RISK_CONF_001,RISK_CONF_002,RISK_DECISION_001,RISK_DEP_001,RISK_DERIV_001,RISK_DERIV_002,RISK_EXT_001,RISK_INCUBA_001,RISK_INGEST_001,RISK_INGEST_002,RISK_META_001,RISK_META_002,RISK_MOLD_001,RISK_ORIENT_001,RISK_PRIV_001,RISK_PRIV_002,RISK_SEC_001,RISK_STAGE_001,RISK_WEBQA_001 risk;
```
