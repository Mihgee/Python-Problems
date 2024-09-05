def main():
    numberString = input("Enter integers between 1 and 100:")
    count = [0 for i in range(1,101)]
    numsList = numberString.split(" ")
    nums = [int(x) for x in numsList]

    for num in nums:
        count[num-1] += 1

    for i in range(len(count)):
        if count[i] != 0:
            print(str(i+1)+ " occurs " + str(count[i]) + " times")

main()