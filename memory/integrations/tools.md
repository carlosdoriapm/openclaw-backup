# Integrações e Ferramentas

> Mapa de ferramentas, APIs e acessos configurados.

## APIs ativas

| Ferramenta | Uso | Notas |
|-----------|-----|-------|
| Firecrawl | Scraping de URLs (Spydoria, swing-trade) | Chave configurada internamente. Uso via scripts. |
| TradingView (via Firecrawl) | Scan de ações americanas | Script em `/root/.openclaw/workspace/skills/swing-trade-hunter/scripts/` |
| yfinance | Dados de mercado (RSI semanal/diário) | Usado pelo `swing-trade-hunter` para análises técnicas. |

## Scripts operacionais (Agente Interno: swing-trade-hunter)

- **Scan Completo**: `python3 /root/.openclaw/workspace/skills/swing-trade-hunter/scripts/tradingview_firecrawl.py` (com filtro RSI semanal ativo)
- **Análise de Ticker**: `python3 /root/.openclaw/workspace/skills/swing-trade-hunter/scripts/analyze_single_ticker.py "TICKER"`

## Infraestrutura

- Servidor com Cloudflare Tunnel ativo.
- Fail2ban ativo no SSH.
- UFW não instalado (pendente de configuração).
- SSH com `PermitRootLogin=yes` (risco identificado, pendente hardening — 2026-04-19).

---

*Última atualização: 2026-04-21*
