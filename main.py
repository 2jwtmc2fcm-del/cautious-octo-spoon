import requests

price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur").json()

print("Prezzo BTC:", price["bitcoin"]["eur"], "€")
