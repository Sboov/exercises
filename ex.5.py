money = float(input("How much money do u have?"))
crypto_prices = {"BTC": 200, "ETH":50, "LTC":20}

for crypto, price in crypto_prices.items():
    amount = money / price
    print(f"For {money} USD u can buy {amount} of {crypto}")


