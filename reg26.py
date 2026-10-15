import re

s = """Research paper published in 2024.
DOI: 10.1234/abcd.5678
Email: author@example.com
URL: https://example.com/paper"""

doi = re.findall(r'10\.\d{4,9}/[^\s]+', s)
year = re.findall(r'\b(?:19|20)\d{2}\b', s)
email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', s)
url = re.findall(r'https?://[^\s]+', s)

print("DOI:", doi)
print("Year:", year)
print("Email:", email)
print("URL:", url)