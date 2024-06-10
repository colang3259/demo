import requests

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']

bitcoin_price = get_bitcoin_price()
print(f"Current Bitcoin price: ${bitcoin_price}")