str = input("Enter string: ")

printed = ""

for ch in str:
    if ch not in printed:
        print(ch, "=", str.count(ch))
        printed = printed + ch