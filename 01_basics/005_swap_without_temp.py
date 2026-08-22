"""
Program 005: Swap Two Variables (Without a Temporary Variable)
Description : Swaps two variables using Python's tuple-unpacking feature.
Explanation : Python evaluates the right-hand side (a, b) fully into a
              temporary tuple BEFORE assigning to the left-hand side,
              so no extra variable is needed.
"""

a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Pythonic one-line swap using tuple unpacking
a, b = b, a

print(f"After swap:  a = {a}, b = {b}")
