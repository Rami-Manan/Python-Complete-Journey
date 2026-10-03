"""
Program 043: Fibonacci Series Using a Loop
Description : Prints the first N terms of the Fibonacci sequence
              (0, 1, 1, 2, 3, 5, 8, ...).
Explanation : Each term is the sum of the two terms before it. We keep
              two "sliding" variables (a, b) and shift them forward
              each iteration.
"""

n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # shift the window forward

print()
