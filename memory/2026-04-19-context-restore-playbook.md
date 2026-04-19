# 2026-04-19 — Playbook de restauração de contexto após troca de modelo

- Usuário pediu avaliação prática de um playbook para restaurar contexto de agente OpenClaw após troca de modelo.
- Diagnóstico principal: problema tende a ser composto por reindexação, retrieval, boot de contexto, memória recente e disciplina operacional do segundo cérebro (GitHub), não apenas pelo modelo.
- Ação executada: `openclaw memory index --force` concluído com sucesso.
- Evidência local: `openclaw status` mostrou memória vetorial pronta, 14 arquivos / 68 chunks, e a sessão atual em `openai/gpt-5.4`; havia também sessão antiga em `gpt-4o-mini`, o que reforça hipótese de troca de modelo afetando comportamento percebido.
- Observação de boot/contexto: `IDENTITY.md` e `USER.md` ainda estão vazios/template, então o boot identitário e de preferências está fraco neste workspace.
- Observação operacional: repositório git existe mas ainda sem commits; isso enfraquece o uso do GitHub como segunda fonte de verdade até que o fluxo de commit/push seja realmente adotado.
- Artefato criado: `PRD-restauracao-contexto-openclaw.md` com playbook/checklist replicável.
- Próximos passos recomendados: preencher identidade/usuário, consolidar fluxo de flush de memória, versionar e commitar playbook, e fazer warm-up deliberado após cada troca de modelo antes de tarefas críticas.
