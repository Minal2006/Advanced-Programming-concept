file = open("file1.txt", "r")
longest_word = ""
for line in file:
    words = line.split()

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
file.close()
print("Longest word:", longest_word)
print("Length of longest word:", len(longest_word))