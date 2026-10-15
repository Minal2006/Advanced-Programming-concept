import re

s = "Invoice No: INV123 Date: 15-10-2026 Amount: Rs. 2500"

invoice = re.findall(r'INV\d+', s)
date = re.findall(r'\d{2}-\d{2}-\d{4}', s)
amount = re.findall(r'\d+', s.split("Amount: Rs.")[-1])

print("Invoice:", invoice)
print("Date:", date)
print("Amount:", amount)