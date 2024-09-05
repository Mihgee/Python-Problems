vowels =  {'a','e','i','o','u'}

string  = input("Enter a string to count its vowel and consonants: ").lower()

vowel_count = 0
consonant_count = 0

for x in string:
    if x in vowels:
        vowel_count += 1

    elif x != ' ':
        consonant_count += 1
print("Vowels: " , vowel_count)
print("Consonant: " , consonant_count)
