import requests

SIMPLE_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"

def simple_single_price(coin_id, currency):
    request_url = SIMPLE_PRICE_URL.format(coin_id, currency)
    response = requests.get(request_url)
    coin_data = response.json()
    return coin_data[coin_id][currency]
