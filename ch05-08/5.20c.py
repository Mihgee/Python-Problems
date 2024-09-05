#pattern 3 ,  it said to do 5.20 in 4 seperate programs
N= 7
for i in range(1,N):
    for j in range(N,i - 1, -1):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k,end=" ")
    print()
print("\n")