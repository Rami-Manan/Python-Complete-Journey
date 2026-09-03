"""
Program 018: Largest of Three Numbers
Description : Finds the largest among three numbers.
Explanation : Nested if/elif comparisons cover every possible ordering
              of the three values.
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")
# Equivalent one-liner: largest = max(a, b, c)
