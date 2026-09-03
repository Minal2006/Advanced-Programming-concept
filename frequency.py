
def word_frequency(words):
    frequency = {}

    for word in words:
        word = word.lower()

        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency