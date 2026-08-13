numbers = (10, 25, 14, 33, 42, 51, 68, 77, 80, 91, 12, 23, 36, 45, 50)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)