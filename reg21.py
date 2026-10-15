import re

s = "<p>Hello!!!   World.</p>"

s = re.sub(r'<[^>]*>', '', s)
s = re.sub(r'\s+', ' ', s)
s = re.sub(r'[^\w\s]', '', s)

print(s.strip())