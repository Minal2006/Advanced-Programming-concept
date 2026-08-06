lst=[22,16,18,27,23]
large=lst[0]
second=lst[1]
for i in lst:
    if large<i:
        second=large
        large=i
    elif second<i and second!=large:
        second=i
print(second)