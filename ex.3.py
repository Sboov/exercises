currency = "PLN"
bitcoin_value = 279092.10  
bitcoin_increase_in_percentage = 20  

total_increase_value = bitcoin_value * (bitcoin_increase_in_percentage / 100)

total_bitcoin_value = bitcoin_value + total_increase_value

print("You bought BTC with Value:", bitcoin_value, currency)
print("BTC increased about 20% (", total_increase_value, currency, ")")
print("Now you got:", total_bitcoin_value, currency)