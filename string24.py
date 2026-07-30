s = input("Enter string: ")
max_char = ""
max_count = 0

for ch in s:
    count = s.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Character with highest frequency:", max_char)
print("Frequency:", max_count)