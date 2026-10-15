import re

s = """# This is a comment
x = 10  # Another comment
print(x)"""

print(re.findall(r'#.*', s))