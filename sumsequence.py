n=int(input("enter the value:"))
sum=1.0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(1/fact)
print("sum of sequence:",sum)