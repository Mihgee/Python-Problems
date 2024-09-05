
def locateLargest(a):
    xLargestIndex, yLargestIndex = 0, 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a [i][j] > a[xLargestIndex][yLargestIndex]:
                xLargestIndex,yLargestIndex = i,j
    return xLargestIndex,yLargestIndex

def main():
    matrix= []
    numRows = int(input("Enter the number of rows in the list: "))
    for i in range(numRows):
        matrix.append([float(x.strip()) for x in input("enter a row: ").split()])
    x,y =locateLargest(matrix)
    print("The location of the largest element is at ({}, {})".format(x, y))

main()
