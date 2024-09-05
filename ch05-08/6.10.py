def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False

    return True

count = 0
for i in range(1,10001):
    if isPrime(i):
        count += 1

print("The nuber of primes less than 10,000 is ",count)