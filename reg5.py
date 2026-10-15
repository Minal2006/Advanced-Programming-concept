import re
s = "Hello World\tPython\nProgramming"
print(re.findall(r'[ \t\n]', s))