laptop_price = int(input("Laptop price: "))
tax_percentage = int(input("Tax: "))
total_price = int((laptop_price * tax_percentage/100 + laptop_price)) 
print(f"{total_price}")