def count(s, ch):
    result = 0
    for x in s:
        if(ch == x):
            result += 1
    return result

s = input("Enter string: ")
ch = input("Enter character: ")[0]
print("The number of times,",ch,",appears in the string is: ",count(s, ch))