"""
Program 034: Check Prime Number
Description : Checks whether a number is prime (only divisible by 1
              and itself).
Explanation : We only need to test divisors up to sqrt(n), because any
              factor larger than sqrt(n) would have a matching factor
              smaller than sqrt(n) already found.
"""

import math

n = int(input("Enter a number: "))

is_prime = n > 1  # numbers <= 1 are not prime by definition
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break  # a divisor was found, no need to keep checking

print(f"{n} is {'Prime' if is_prime else 'Not Prime'}")
