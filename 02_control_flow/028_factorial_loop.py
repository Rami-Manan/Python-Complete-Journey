"""
Program 028: Factorial Using a Loop
Description : Calculates N! (N factorial) iteratively.
Explanation : Factorial is the product of all positive integers up to N.
              We start 'factorial' at 1 (the multiplicative identity) and
              multiply it by each number from 1 to N.
"""

n = int(input("Enter a non-negative integer: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i  # same as factorial = factorial * i

print(f"{n}! = {factorial}")
