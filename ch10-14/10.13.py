# eliminating duplicates from a list of N length   split() and create a new list .
# can numbers and letters be used interchangeably or do I need 2 separate functions?
def eliminateDuplicate(lst):
    newLst = lst

#is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())

    for i in range(len(newLst)):
        j = i + 1
        while j < len(newLst):
            if newLst[i] == newLst[j]:
                newLst.pop(j)
                j= j-1
            j= j + 1
    return newLst

s = input("Enter ten numbers: ")
lst= s.split()
print("The distinct numbers are: ", end='')
newLst= eliminateDuplicate(lst)
for i in range(len(newLst)):
    print(newLst[i], end=' ')
print()