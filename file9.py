file = open("file1.txt", "r")
vowels = 0
consonants = 0
for line in file:
    for ch in line:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
file.close()
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)