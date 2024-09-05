def printChars(ch1, ch2, numberPerLine):
    count = 1
    for i in range(ord(ch1), ord(ch2)+1):
        print(chr(i), end="  ")
        if count % numberPerLine == 0:
            print()
        count += 1


printChars("1", "z", 10)