str = input("Enter a string: ")
rev = ""
for ch in str:
    rev = ch + rev

if str == rev:
    print("Palindrome")
else:
    print("Not Palindrome")