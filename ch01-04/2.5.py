gratuity= eval(input("What is the desired gratuity percent?"))
subtotal= eval(input("What is the subtotal of your bill?"))
ngrat= gratuity/100
total= (ngrat * subtotal)+subtotal
print(total)
