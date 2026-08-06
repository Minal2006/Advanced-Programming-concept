print("enter the 10 numbers:")
num=[]
sum=0
for i in range(10):
    num.append(int(input()))
    sum=sum+num[i]
    avg=sum/10
print("sum:",sum)
print("average:",avg)