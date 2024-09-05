def prefix(s1, s2):
    i=0
    j=0
    temp=''
    lcp=''

    while i < len(s1) and j < len(s2):

        if (s1[i] == s2[j]):
            temp=temp+s1[i]
            i+=1
            j+=1
        else:
            if len(s1) <len(s2):
                i=0
                j+=1
            else:
                j=0
                i+=1
            temp=''
        if len(lcp)<len(temp):
            lcp=temp
    return lcp
def main():
    string1=input('Enter a string: ')

    string2=input('Enter another string: ')

    print('Longest common prefix= '+prefix(string1,string2))

main()