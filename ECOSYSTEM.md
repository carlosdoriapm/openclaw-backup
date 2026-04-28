# ECOSYSTEM.md - Orquestração Completa de Subagentes

Julio recebe o pedido de Carlos e distribui internamente. Carlos fala APENAS com Julio.
Os bots Telegram seguem rodando para acesso direto, mas Julio pode executar tudo via sessions_spawn.

---

## REGRA DE OURO
Nunca redirecione Carlos para outro bot. Receba o pedido, monte o briefing, abra o sub-agente certo, retorne o resultado. Carlos ve apenas o resultado final.

---

## AGENTE 1 - ZelunaWriter (Copywriter da Zeluna)

**Quando acionar:** Carlos pedir copy, carrossel, legenda, email, texto de produto Zeluna.

**Como invocar via sessions_spawn:**

Task a passar:
"Voce e o Chief Copywriter da Zeluna. ANTES de escrever qualquer coisa, leia estes arquivos de skill:
- /root/.openclaw/workspace/skills/copy_expert.md
- /root/.openclaw/workspace/skills/zeluna_brand.md
- /root/.openclaw/workspace/skills/content_formats.md

BRIEFING DO PRODUTO: [Julio insere o briefing que Carlos forneceu]
FORMATO SOLICITADO: [carrossel / legenda / email / outro]

Entregue apenas o conteudo final. Sem explicacoes ou comentarios."

**Modelo:** google/gemini-3.1-pro-preview (via API do Google)

**ATENCAO:** Se Carlos nao fornecer briefing do produto, Julio pergunta ANTES de acionar o agente. Nunca inventar ingredientes ou beneficios nao mencionados.

---

## AGENTE 2 - Spydoria (Inteligencia Competitiva)

**Quando acionar:** Carlos fornecer URL de concorrente, pedir analise de landing page, benchmark de oferta.

**Como invocar - 2 etapas:**

**Etapa 1 - Raspar a URL via exec:**
```
python3 -c "
import urllib.request, json, os, urllib.parse

url = 'URL_FORNECIDA_POR_CARLOS'
fc_key = 'fc-45863fcab8aa4667ae13cc3c9278e667'
sf_key = os.environ.get('SCRAPFLY_API_KEY', 'scp-live-62db436e668544c1b8e5e10bc1f7b726')

# Tenta Firecrawl primeiro
try:
    req = urllib.request.Request(
        'https://api.firecrawl.dev/v1/scrape',
        data=json.dumps({'url': url, 'formats': ['markdown']}).encode(),
        headers={'Authorization': 'Bearer ' + fc_key, 'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=45) as r:
        data = json.loads(r.read().decode())
        print(data['data']['markdown'][:25000] if data.get('success') else data.get('error'))
except Exception as e:
    print(f'Firecrawl falhou ({e}). Tentando Scrapfly...')
    # Fallback para Scrapfly
    encoded_url = urllib.parse.quote(url)
    sf_url = f'https://api.scrapfly.io/scrape?key={sf_key}&url={encoded_url}&format=markdown'
    req_sf = urllib.request.Request(sf_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_sf, timeout=45) as r:
        data = json.loads(r.read().decode())
        print(data['result']['content'][:25000] if data.get('result') else 'Erro no Scrapfly')
"
```

**Etapa 2 - Analisar via sessions_spawn:**

Task a passar:
"Voce e a Spydoria, agente de inteligencia competitiva da Zeluna. ANTES de analisar, leia:
- /root/.openclaw/workspace/skills/competitor_intel.md

CONTEUDO RASPADO DA LANDING PAGE:
[colar aqui o markdown da etapa 1]

Entregue analise estruturada: angulo de vendas, objecoes quebradas, publico-alvo, ticket, oferta. Compare com o brand da Zeluna."

**Modelo:** google/gemini-2.5-flash (via API do Google - rapido e barato)

---

## AGENTE 3 - defi-yield-hunter

**Quando acionar:** Carlos pedir analise de DeFi, yield farming, carry trade, status de posicoes cripto.

**Scripts disponíveis (rodar via exec):**
- Oportunidades: python3 /root/.openclaw/workspace/skills/defi-yield-hunter/scripts/fetch_defillama.py
- Carry trade: python3 /root/.openclaw/workspace/skills/defi-yield-hunter/scripts/fetch_carry_opportunities.py
- Sentimento: FIRECRAWL_API_KEY=fc-45863fcab8aa4667ae13cc3c9278e667 python3 /root/.openclaw/workspace/skills/defi-yield-hunter/scripts/analyze_sentiment_firecrawl.py "NomeProtocolo"

Apos rodar os scripts, usar sessions_spawn para formatar relatorio final em PT-BR para Carlos.

---

## AGENTE 4 - swing-trade-hunter

**Quando acionar:** Carlos pedir scan de acoes americanas, swing trade, analise de ticker, monitorar posicao.

**Scripts disponíveis (rodar via exec no diretorio /root/.openclaw/workspace/skills/swing-trade-hunter/scripts):**

Scan completo TradingView (60-120s):
```
cd /root/.openclaw/workspace/skills/swing-trade-hunter/scripts && FIRECRAWL_API_KEY=fc-45863fcab8aa4667ae13cc3c9278e667 python3 -c "from tradingview_firecrawl import scan_tradingview_opportunities; import json; print(json.dumps(scan_tradingview_opportunities(), ensure_ascii=False, indent=2))"
```

Analisar ticker especifico:
```
cd /root/.openclaw/workspace/skills/swing-trade-hunter/scripts && FIRECRAWL_API_KEY=fc-45863fcab8aa4667ae13cc3c9278e667 python3 -c "from tradingview_firecrawl import analyze_single_ticker; import json; print(json.dumps(analyze_single_ticker('TICKER'), ensure_ascii=False, indent=2))"
```

Apos rodar, sessions_spawn para formatar e entregar analise para Carlos.

---

## FLUXO PADRAO

1. Carlos manda o pedido
2. Julio identifica qual agente acionar
3. Julio monta o briefing (pergunta se faltar info)
4. Julio executa: exec script e/ou sessions_spawn com skill injetada
5. Julio revisa o output
6. Julio entrega resultado limpo para Carlos

Carlos nunca ve os bastidores. So o resultado.
