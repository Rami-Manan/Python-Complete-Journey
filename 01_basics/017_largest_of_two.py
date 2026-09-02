"""
Program 017: Largest of Two Numbers
Description : Finds the larger of two numbers.
Explanation : A direct comparison with if/else. Python's built-in max()
              could do this in one line (see comment), but the explicit
              version shows the underlying logic.
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    largest = a
else:
    largest = b

print(f"The largest number is {largest}")
# Equivalent one-liner: largest = max(a, b)
