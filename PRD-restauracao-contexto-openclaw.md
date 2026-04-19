# PRD — Playbook de Restauração de Contexto após Troca de Modelo no OpenClaw

## 1. Objetivo
Criar um processo simples, replicável e confiável para restaurar contexto, memória operacional e continuidade de agentes OpenClaw após troca de modelo.

## 2. Problema
Após trocar de modelo, alguns agentes passam a operar pior mesmo mantendo a mesma base de memória. Os sintomas mais comuns são:
- perda de continuidade
- piora na recuperação de contexto
- menor aderência a decisões e preferências já salvas
- respostas mais desalinhadas
- regressão em tarefas complexas

## 3. Hipótese central
O problema não é apenas o novo modelo. Existe um desalinhamento entre:
- o índice atual de memória
- o padrão de retrieval do novo modelo
- a memória recente da sessão
- o boot de contexto
- o fluxo de uso do GitHub como segundo cérebro

## 4. Tese operacional
Duas ações ajudam muito logo após a troca de modelo:

### 4.1 Reindexação forçada
Executar:
`openclaw memory index --force`

### 4.2 Warm-up do agente
Após a reindexação:
- conversar alguns minutos com o agente
- reapresentar projetos, decisões, tarefas e preferências atuais
- só depois iniciar tarefas críticas

## 5. Por que a reindexação forçada ajuda
Mesmo sem trocar explicitamente o embedding model, a reindexação ajuda porque:
- reprocessa todos os arquivos de memória
- recria embeddings do zero
- reorganiza o espaço vetorial
- recalibra relações de proximidade semântica
- melhora coerência entre busca e o novo padrão de uso do modelo

Em termos práticos:
O índice anterior pode não estar “errado”, mas pode estar mal calibrado para a forma como o novo modelo formula consultas, interpreta relevância e consome contexto.

## 6. Por que o warm-up ajuda
O warm-up ajuda porque cria um centro de gravidade novo de contexto recente.

Durante esse processo:
- o usuário injeta contexto real e atualizado
- o sistema grava memória recente
- o retrieval passa a priorizar esse contexto fresco
- o agente reduz dependência do histórico antigo mal recuperado

Em termos práticos:
- sem warm-up: modelo novo + memória antiga = mais desalinhamento
- com warm-up: modelo novo + memória recente = melhora rápida de aderência

## 7. Escopo
### Incluído
- reindexação forçada
- warm-up estruturado
- auditoria de boot
- auditoria de retrieval
- auditoria do uso do GitHub como fonte de verdade
- auditoria de flush antes da compactação
- recomendações replicáveis para outros usuários

### Não incluído
- fine-tuning do modelo
- mudanças no provider fora do OpenClaw
- alterações externas sem acesso disponível

## 8. Fluxo recomendado
### Etapa 1 — Reindexação
Rodar:
`openclaw memory index --force`

### Etapa 2 — Warm-up
Nos primeiros minutos após a troca:
- reapresentar contexto atual
- reforçar decisões importantes
- citar tarefas, projetos e preferências vivas
- evitar começar direto em tarefa crítica

### Etapa 3 — Revisão de boot
Garantir que o agente leia corretamente seus arquivos-base de identidade e contexto no início da sessão.

### Etapa 4 — Revisão do GitHub
Garantir fluxo:
- pull
- leitura do contexto relevante
- execução
- validação
- registro
- push

### Etapa 5 — Revisão de compactação
Garantir flush antes da compactação, salvando:
- decisões
- lições aprendidas
- projetos
- pendências
- nota diária
- índice, quando necessário

## 9. Entregáveis
- diagnóstico técnico claro
- explicação prática do papel da reindexação
- explicação prática do papel do warm-up
- checklist objetivo de correção
- quick wins imediatos
- recomendações replicáveis para outros agentes

## 10. Critérios de aceite
O playbook será considerado bem-sucedido se:
- o agente recuperar melhor o contexto após troca de modelo
- houver melhora perceptível na aderência a preferências e decisões já salvas
- o retrieval passar a encontrar memória relevante com mais consistência
- o usuário conseguir repetir o processo em outros agentes com resultado semelhante

## 11. Quick wins imediatos
- rodar `openclaw memory index --force` após troca de modelo
- fazer warm-up antes de tarefa crítica
- revisar boot dos arquivos-base
- reforçar o uso do GitHub como fonte de verdade
- reforçar flush antes da compactação

## 12. Riscos se não fizer
- agente continuar desalinhado mesmo com memória existente
- repetição de erros já resolvidos
- perda de confiança do usuário
- mais retrabalho
- pior replicabilidade em setups de alunos ou outros agentes

## 13. Instrução final para o agente executor
Use este playbook para diagnosticar, explicar e corrigir o problema de restauração de contexto após troca de modelo.
Sempre que possível, implemente os ajustes práticos, não apenas explique.

## 14. Checklist operacional curto
- [ ] Rodar `openclaw memory index --force`
- [ ] Abrir nova sessão após troca de modelo
- [ ] Fazer warm-up de 5–10 minutos com contexto vivo
- [ ] Confirmar leitura dos arquivos-base no boot
- [ ] Confirmar fluxo GitHub: pull → leitura → execução → validação → registro → push
- [ ] Confirmar flush de memória antes de compactação
- [ ] Só então iniciar tarefa crítica
