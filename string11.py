str = input("Enter a sentence: ")
count = 1
for ch in str:
    if ch == " ":
        count = count + 1

print("Total words =", count)