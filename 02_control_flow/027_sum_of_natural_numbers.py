"""
Program 027: Sum of First N Natural Numbers
Description : Calculates 1 + 2 + 3 + ... + N using a loop.
Explanation : A running total ('total') is updated on every iteration.
              The mathematical shortcut N*(N+1)/2 is shown for comparison.
"""

n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1):
    total += i  # same as total = total + i

print(f"Sum of first {n} natural numbers: {total}")
print(f"Verified with formula: {n * (n + 1) // 2}")
