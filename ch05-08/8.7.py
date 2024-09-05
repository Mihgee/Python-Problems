def getNumber(uppercaseLetter):
    if uppercaseLetter == 'a' or uppercaseLetter == 'b' or uppercaseLetter == 'c' or uppercaseLetter == 'A' or uppercaseLetter == 'B' or uppercaseLetter == 'C':
        return 2
    elif uppercaseLetter == 'd' or uppercaseLetter == 'e' or uppercaseLetter == 'f' or uppercaseLetter == 'D' or uppercaseLetter == 'E' or uppercaseLetter == 'F':
        return 3
    elif uppercaseLetter == 'g' or uppercaseLetter == 'h' or uppercaseLetter == 'i' or uppercaseLetter == 'G' or uppercaseLetter == 'H' or uppercaseLetter == 'I':
        return 4
    elif uppercaseLetter == 'j' or uppercaseLetter == 'k' or uppercaseLetter == 'l' or uppercaseLetter == 'J' or uppercaseLetter == 'K' or uppercaseLetter == 'L':
        return 5
    elif uppercaseLetter == 'm' or uppercaseLetter == 'n' or uppercaseLetter == 'o' or uppercaseLetter == 'M' or uppercaseLetter == 'N' or uppercaseLetter == 'O':
        return 6
    elif uppercaseLetter == 'p' or uppercaseLetter == 'q' or uppercaseLetter == 'r' or uppercaseLetter == 's' or uppercaseLetter == 'P' or uppercaseLetter == 'Q' or uppercaseLetter == 'R' or uppercaseLetter == 'S':
        return 7
    elif uppercaseLetter == 't' or uppercaseLetter == 'u' or uppercaseLetter == 'v' or uppercaseLetter == 'T' or uppercaseLetter == 'U' or uppercaseLetter == 'V':
        return 8
    elif uppercaseLetter == 'w' or uppercaseLetter == 'x' or uppercaseLetter == 'y' or uppercaseLetter == 'z' or uppercaseLetter == 'W' or uppercaseLetter == 'X' or uppercaseLetter == 'Y' or uppercaseLetter == 'Z':
        return 9
    else:
        return 0

s = input("Enter a phone number that contains letters:")

length = len(s)

for i in range(length):
    c = s[i]
    k = getNumber(c)
    if k == 0:
        print(c, end="")
    else:
        print(k, end="")

print('\n')