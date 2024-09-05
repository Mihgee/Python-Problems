numbers = input("Enter a list of integers: ")

list1 = numbers.split()

dict_frequency = {}

for x in list1:
    if x in dict_frequency:
        dict_frequency[x] += 1
    else:
        dict_frequency[x] = 1

most_freq = sorted(list(dict_frequency.values()))[-1]

for k,v in dict_frequency.items():
    if v == most_freq:
        print(k,end=" ")