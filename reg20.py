import re

s = "Files: abc.py, photo.jpg, notes.txt"
print(re.findall(r'\.([A-Za-z0-9]+)\b', s))