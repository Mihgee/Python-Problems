def reverse(lst):
    for i in range(len(lst)//2):
        temp = lst[i]
        lst[i]=lst[len(lst)-i-1]
        lst[(len(lst)-i-1)] = temp
    return lst

def main():
    lst=list(map(int,input("Enter the list elements seperated by comma").split(',')))
    print(reverse(lst))
main()