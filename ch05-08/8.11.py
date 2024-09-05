def reverse(s):
    res = ""
    for x in s:
        res = x + res
    return res

def main():
    s = input("Enter string: ")
    print("The Reverse of,",s,":","\n",reverse(s))

main()