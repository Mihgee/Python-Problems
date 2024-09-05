# 1.9 2.5 3.7 2 1 6 3 4 5 2
import math

def mean(x):
    total = 0
    for num in x:
        total += num
    return total / len(x)


def deviation(x):
    mn = mean(x)
    z = [(y - mn) ** 2 for y in x]
    sm = sum(z)
    dev = math.sqrt(sm / (len(z) - 1))
    return dev

def main():
    lst = input("Enter Numbers: ").split()
    lst = [float(x) for x in lst]
    print("The mean is", mean(lst))
    print("The standard Deviation is",deviation(lst))
main()