import re

s = "Hello    World   Python"
s = re.sub(r' +', ' ', s)
print(s)