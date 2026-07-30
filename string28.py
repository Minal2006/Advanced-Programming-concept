para = input("Enter paragraph: ")

words = para.split()
printed = []

for word in words:
    if word not in printed:
        print(word, "=", words.count(word))
        printed.append(word)