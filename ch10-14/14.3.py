def word_countr(str):
    counts= dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_countr(input("Enter a list of words or a sentence( without punctuation ): ")))