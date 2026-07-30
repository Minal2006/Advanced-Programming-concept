str = input("Enter a string: ")
r = ""
for ch in str:
    if ch != " ":
        r = r + ch

print("String without spaces:", r)