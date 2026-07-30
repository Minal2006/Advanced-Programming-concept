str = input("Enter string: ")
result = ""
for ch in str:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)