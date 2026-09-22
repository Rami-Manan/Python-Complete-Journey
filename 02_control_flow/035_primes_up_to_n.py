"""
Program 035: Print Prime Numbers up to N
Description : Lists all prime numbers from 2 up to a given N.
Explanation : For each candidate number, test divisibility by every
              integer from 2 up to its square root; if none divide it
              evenly, it's prime.
"""

import math

n = int(input("Enter N: "))

print(f"Prime numbers up to {n}:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
