import urllib.request
import json

def get_current_data():
    url = "https://yields.llama.fi/pools"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode('utf-8'))
    pools = data.get("data", [])
    
    results = []
    
    # Pools we are looking for:
    # 1. Aave V3 on Base (ETH supply, USDC borrow)
    # 2. Yo Protocol on Base (USDC)
    # 3. Altura Trade on Hyperliquid (USDTO)
    
    for pool in pools:
        project = pool.get('project', '').lower()
        chain = pool.get('chain', '').lower()
        symbol = pool.get('symbol', '').lower()
        
        if 'aave-v3' in project and 'base' in chain:
            results.append(pool)
        if 'yo' in project and 'base' in chain:
            results.append(pool)
        if 'altura' in project and 'hyperliquid' in chain:
            results.append(pool)
            
    return results

data = get_current_data()
for p in data:
    print(f"Project: {p['project']} | Chain: {p['chain']} | Symbol: {p['symbol']} | APY: {p['apy']}")
