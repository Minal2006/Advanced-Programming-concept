
file = open("file1.txt", "r")
alphabets = 0
digits = 0
spaces = 0
special = 0
for line in file:
    for ch in line:
        if ch.isalpha():
            alphabets = alphabets + 1
        elif ch.isdigit():
            digits = digits + 1
        elif ch == " ":
            spaces = spaces + 1
        elif ch != "\n":
            special = special + 1
file.close()
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)