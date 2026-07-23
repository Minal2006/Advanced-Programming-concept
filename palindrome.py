num=int(input("enter the number:"))
rev=0
digit=0
while num>0:
    digit=num%10
    num=num//10

    rev=rev*10+digit
if rev==num:
    print('number is palindrome')
else:
    print("number is not palindrome")