print("Enter a principle amount")
principle = float(input())
print("Enter years of Maturity")
maturity = float(input())
if principle >= 100000 and maturity == 5:
    ir = 0.06
else:
    if principle <= 50000 or principle >= 100000 and maturity == 10:
        ir = 0.05
    else:
        if principle >= 50000 or principle <= 100000 and maturity == 5:
            ir = 0.04
        else:
            ir = 0.02
print("Principle price: " + str(principle))
print("Maturity: " + str(maturity))
print("Interest Rate: " + str(ir))
print("Total price for 1 year: " + str(ir * principle + principle))
