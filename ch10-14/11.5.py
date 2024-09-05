def addMatrix(a, b):

    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(0, len(a)):

        for j in range(0, len(a[i])):
            c[i][j] = a[i][j] + b[i][j]

    return c


print('Enter 3x3 matrix')

x = list(map(float, input('Enter matrix 1 : ').split(' ')))

y = list(map(float, input('Enter matrix 2 : ').split(' ')))

index = 0

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):

    for j in range(0, 3):
        a[i][j] = x[index]

        index += 1

index = 0

for i in range(0, 3):

    for j in range(0, 3):
        b[i][j] = y[index]

        index += 1

c = addMatrix(a, b)

for i in range(0, 3):
    print(a[0][i], end=' ')

print('   ', end='')

for i in range(0, 3):
    print(b[0][i], end=' ')

print(' ', end='')

for i in range(0, 3):
    print(c[0][i], end=' ')

print()

for i in range(0, 3):
    print(a[1][i], end=' ')

print(' + ', end='')

for i in range(0, 3):
    print(b[1][i], end=' ')

print(' = ', end='')

for i in range(0, 3):
    print(c[1][i], end=' ')

print()

for i in range(0, 3):
    print(a[2][i], end=' ')

print('   ', end='')

for i in range(0, 3):
    print(b[2][i], end=' ')

print(' ', end='')

for i in range(0, 3):
    print(c[2][i], end=' ')