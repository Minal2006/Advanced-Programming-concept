str = input("Enter sentence: ").split()
word = input("search word: ")
count = 0
for w in str:
    if w == word:
        count = count + 1

print("Number of occurrences:", count)