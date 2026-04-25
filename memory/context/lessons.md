# Lições Aprendidas

> Erros e padrões que não devem se repetir.
> 🔒 Estratégicas = permanentes | ⏳ Táticas = expiram em 30 dias

## 🔒 Estratégicas

- **Não ser burocrático.** Carlos reclamou que o agente estava "muito burocrático e técnico" ao pedir confirmações excessivas em vez de executar. Quando o pedido é claro, executar direto. Perguntar só quando realmente falta informação crítica. (2026-04-21)

- **Não negar capacidade antes de tentar.** O agente disse "não tenho skills de trader" e "não consigo" múltiplas vezes quando Carlos pediu para usar subagentes. O certo é: verificar o que existe (ECOSYSTEM.md, scripts, skills) e tentar. Se realmente não der, explicar o motivo técnico específico — não dar resposta genérica de incapacidade. (2026-04-21)
    - Corrigido: `swing-trade-hunter` é um agente interno ao Júlio, não um bot externo.

- **Pedido curto de Carlos ≠ tarefa curta.** Expandir, estruturar e qualificar antes de delegar para subagente. (2026-04-19)

- **Troca de modelo pode degradar comportamento.** Após trocar modelo, fazer warm-up deliberado: reindexar memória, reler contexto, testar retrieval antes de tarefas críticas. (2026-04-19)

- **Memória não preenchida = boot fraco.** IDENTITY.md e USER.md vazios causam perda de persona e contexto. Sempre manter preenchidos. (2026-04-19)

## ⏳ Táticas

- **SJM aparece consistentemente no scan de swing trade** como reversão profunda com RSI semanal sobrevendido (~34-35). Monitorar. (2026-04-21, expira 2026-05-21)
- **KHC e GIS** foram sinalizados como "Exhaustion" no scan de swing trade com RSI semanal (41.2 e 43.0 respectivamente) em 2026-04-21. (Expira 2026-05-21)

- **Filtro Swing Trade:** Ao apresentar relatórios de swing trade, nunca considerar "Elite" ativos onde o RSI semanal não seja inferior a 30, a menos que o usuário solicite expressamente operações de curtíssimo prazo. Ativos gigantes com RSI semanal < 20 são as joias raras que devem ser trazidas à tona.
