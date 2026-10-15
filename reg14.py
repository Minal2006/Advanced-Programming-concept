import re

s = "Visit https://google.com and http://example.com"
print(re.findall(r'https?://[^\s]+', s))