import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    parameters = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Kiểm tra nếu yêu cầu gặp lỗi
        data = response.json()
        price = data[crypto_id]["usd"]
        return price
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

crypto_id = "bitcoin"
price = get_crypto_price(crypto_id)
if price:
    print(f"The current price of {crypto_id.capitalize()} is ${price} USD.")
else:
    print("Failed to retrieve the price.")
