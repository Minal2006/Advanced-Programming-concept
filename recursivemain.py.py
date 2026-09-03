# main.py

from module_recursive import factorial, fibonacci, sum_digits, binary

n = int(input("Enter a number: "))

# Factorial
print("\nFactorial:", factorial(n))

# Fibonacci Series
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(fibonacci(i), end=" ")

# Sum of digits
print("\nSum of digits:", sum_digits(n))

# Binary conversion
if n == 0:
    print("Binary:", 0)
else:
    print("Binary:", binary(n))