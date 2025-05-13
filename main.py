import requests

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
    r = requests.get(url).json()
    return float(r.get("price", 0))

def get_market_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    r = requests.get(url).json()
    market_cap = r.get("market_data", {}).get("market_cap", {}).get("usd", "N/A")
    rank = r.get("market_cap_rank", "N/A")
    return market_cap, rank

def get_news(coin):
    return [f"Latest news headline about {coin}", "Another news line..."]

def generate_response(coin, price, cap, rank, news):
    response = f"""
💰 {coin.upper()} Summary:
- Current Price: ${price}
- Market Cap: ${cap}
- Market Rank: #{rank}
📰 Latest News:
"""
    for n in news:
        response += f"- {n}\n"
    return response

if __name__ == "__main__":
    coin = input("Enter cryptocurrency (e.g., solana): ").strip().lower()
    try:
        price = get_price(coin)
        cap, rank = get_market_data(coin)
        news = get_news(coin)
        print(generate_response(coin, price, cap, rank, news))
    except Exception as e:
        print("Error fetching data:", e)
