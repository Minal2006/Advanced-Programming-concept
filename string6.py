str = input("Enter a string: ")
s = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in str:
    if ch == s:
        result = result + new
    else:
        result = result + ch

print("New string:", result)