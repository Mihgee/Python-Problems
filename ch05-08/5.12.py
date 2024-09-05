count = 1
for y in range(100,1001):
    if y % 5 == 0 and y % 6 == 0:
        if count == 10:
            print()
            count = 0

        print(y, end=" ")
        count += 1