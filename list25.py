list1 = [10, 20, 10, 30, 20, 40, 50, 30]
unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print("Original List:", list1)
print("List after removing duplicates:", unique)