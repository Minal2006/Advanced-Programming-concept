str = input("Enter a string: ")
ch = input("Enter the character to find: ")
count = 0
for i in str:
    if i == ch:
        count = count + 1

print("Number of occurrences:", count)