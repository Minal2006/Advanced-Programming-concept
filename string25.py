s = input("Enter string: ")
first = ""
second = ""

for ch in s:
    if first == "" or s.count(ch) > s.count(first):
        if ch != first:
            second = first
            first = ch
    elif ch != first and (second == "" or s.count(ch) > s.count(second)):
        second = ch

print("Second most frequent character:", second)