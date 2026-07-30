
n=int(input("enter the number :"))
root=int(n**0.5)
count=0
for i in range(1,root+1):
    if root%i==0:
        count+=1
print("square root:",root)
if count==2:
    print("square root is prime")      
else:
    print("square root is not prime ")      