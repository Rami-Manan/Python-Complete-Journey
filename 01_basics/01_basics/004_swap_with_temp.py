"""
Program 004: Swap Two Variables (Using a Temporary Variable)
Description : Swaps the values of two variables using a helper variable.
Explanation : This is the classic swap algorithm used in most languages:
              store one value temporarily so it isn't lost when overwritten.
"""

a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Use a temporary variable to hold 'a' while we overwrite it
temp = a
a = b
b = temp

print(f"After swap:  a = {a}, b = {b}")
