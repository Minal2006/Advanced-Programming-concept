import re
s = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', s)
print("Vowel count:", len(vowels))