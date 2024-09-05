def gcd(numbers):
    if len(numbers) > 1:
        minimum = numbers[0]
        for i in range(1,len(numbers)):
            if minimum > numbers[i]:
                minimum = numbers[i]
        result = 1
        for i in range(minimum+1,1,-1):
            allDivisible = True
            for x in numbers:
                if x%i !=0:
                    allDivisible = False
                    break
            if allDivisible:
                result = i
                break
        return result
    else:
        return 1

lst=[int(x) for x in input("Enter a list of numbers: ").split()]
print(" GCD:",gcd(lst))