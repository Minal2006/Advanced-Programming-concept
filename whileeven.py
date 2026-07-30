n=int(input("enter the numbers:"))
i=0
sum=0
while i<=n:
    if i%2==0:
         sum=sum+i
    i+=1    

print("sum of even numbers:",sum)    