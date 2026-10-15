import re

s = "My PIN codes are 416001 and 411001"
print(re.findall(r'\b[1-9]\d{5}\b', s))