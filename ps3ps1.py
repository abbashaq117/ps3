print("type the qty")
qty = float(input())
if qty >= 10000:
    price = 10.0
else:
    if qty >= 5000 or qty <= 10000:
        price = 20.0
    else:
        price = 30.0
total = price * 0.07
print(qty)
print(price)
print(total)
