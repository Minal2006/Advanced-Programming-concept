import re

s = input("Enter email: ")

if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w{2,}', s):
    print("Valid email")
else:
    print("Invalid email")