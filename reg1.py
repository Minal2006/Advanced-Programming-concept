import re

s = "My age is 20 and my marks are 94 and learn in 3 rd year "
print(re.findall(r'\d', s))