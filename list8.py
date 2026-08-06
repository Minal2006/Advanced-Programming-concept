num=[2,4,5,6,7,8,9,1,2,54,3,2,1,90,6]
count=0
count1=0
for i in num:
    if i%2==0:
        count+=1
    if i%2!=0:
        count1+=1
print("even number:",count)
print("odd number:",count1)