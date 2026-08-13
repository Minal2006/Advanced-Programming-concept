numbers=(23,67,12,90,75,32)
large=numbers[0]
small=numbers[0]
for i in numbers:
    if i>large:
        large=i
    if i<small:
        small=i
print("large:",large)  
print("small:",small)        
