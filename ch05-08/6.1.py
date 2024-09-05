def getPentagonalNumber(n):
    print(int(n*(3*n -1)// 2), end="")
    print ( ' ',end="")

for i in range (0,10):
    for j in range(1,11):
        getPentagonalNumber((i*10+j))
    print()