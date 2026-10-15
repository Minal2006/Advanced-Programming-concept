import re

s = "Enjoying #Python and #Coding today"
print(re.findall(r'#\w+', s))