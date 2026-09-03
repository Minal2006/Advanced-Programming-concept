
file = open("file1.txt", "r")
word_count = {}
for line in file:
    words = line.split()

    for word in words:
        word = word.lower()

        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
file.close()
print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)