n = int(input("Enter how many numbers: "))

i = 1
smallest = 0

while i <= n:
    num = int(input("Enter number: "))
    if num < smallest:
       smallest = num
    i = i + 1

print("smallest number is:", smallest)