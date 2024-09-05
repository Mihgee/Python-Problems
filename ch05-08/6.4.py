def reverse(number):
    if number == 0:
        print("0")
    else:
        while number > 0:
            print(number%10,end="")
            number //= 10
        print()

n=int(input("enter an integer:"))
reverse(n)