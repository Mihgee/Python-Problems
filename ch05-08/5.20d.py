#Pattern 4 ,  it said to do 5.20 in 4 seperate programs
n = 6

for i in range(0,n+1):
    num = 1
    for j in range(i, n):
        print(num, end=" ")
        num = num + 1
    print()