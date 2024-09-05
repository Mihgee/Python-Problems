from random import randint

def printMatrix(n):

    for x in range(n):

        for y in range(n):

            print(randint(0,1)," ", end="")

        print("\n",end="")

n = int(input('Enter n:'))

printMatrix(n)