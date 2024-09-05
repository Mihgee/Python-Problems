def format(number, width):
    res = str(number)
    while len(res) < width:
        res = "0" + res
    return res

def main():
    x=int(input("enter a number:"))
    y=int(input("enter the specified width:"))
    print(format(x, y))


main()