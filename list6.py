num=[34,78,90,32,10]
large=num[0]
small=num[0]
for i in num:
    if large<i:
        large=i
    if small>i:
        small=i
print("large:",large)
print("small:",small)