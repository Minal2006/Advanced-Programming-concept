n = int(input("Enter how many numbers: "))

i = 1
largest = 0

while i <= n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number is:", largest)