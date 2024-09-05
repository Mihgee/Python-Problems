import random

n1,n2 = random.randint(0,99), random.randint(0,99)
s = "what is " + str(n1) + " + " + str(n2) + " ?"
res= eval(input(s))

print((res == (n1+n2)))