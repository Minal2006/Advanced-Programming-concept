s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

result = result + s[-1] + str(count)

if len(result) < len(s):
    print("Compressed string:", result)
else:
    print("Original string:", s)