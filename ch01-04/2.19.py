invest= eval(input("Enter investment amount:"))
interest= eval(input("Enter interest rate:")) / (100*12)
years= eval(input("Enter number of years:")) * 12

future= invest * (1 +interest) ** years
print("Accumulated value is",future)