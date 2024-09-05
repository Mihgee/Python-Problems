name = input("Enter employee's name:")
hours = eval(input("Enter number of hours worked this week:"))
rate = eval(input("Enter hourly pay rate:"))
federal = eval(input("Enter a federal tax withholding rate(.2):"))
state = eval(input("Enter state tax withholding rate(0.09):"))
grosspay = hours * rate
fw= .2 * grosspay
sw= state * grosspay
total =fw + sw
net = grosspay - total

print()
print("Employee name:",name)
print("Hours worked:",hours)
print("Pay Rate: $",rate)
print("Gross Pay: $",grosspay)
print("Deductions:")
print("\tFederal Withholding " + "(" +format(federal,"2.1%")+ ") $" +format(fw,".2f"))
print("\tState Withholding " + "(" + format(state, ".1%") + "): $" + format(sw, ".2f"))
print("\tTotal Deduction: " + "$" + format(total, ".2f"))
print("Net Pay: $" + format(net, ".2f"))