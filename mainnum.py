

from number_util import is_prime, is_palindrome, is_armstrong, is_perfect

n = int(input("Enter a number: "))

if is_prime(n):
    print("The number is Prime.")
else:
    print("The number is not Prime.")

if is_palindrome(n):
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")

if is_armstrong(n):
    print("The number is Armstrong.")
else:
    print("The number is not Armstrong.")

if is_perfect(n):
    print("The number is Perfect.")
else:
    print("The number is not Perfect.")