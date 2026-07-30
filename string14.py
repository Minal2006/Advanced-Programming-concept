str = input("Enter a sentence: ")
words = str.split()
for word in words:
    print(word.capitalize(), end=" ")