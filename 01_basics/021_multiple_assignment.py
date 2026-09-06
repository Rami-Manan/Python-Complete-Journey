"""
Program 021: Multiple Assignment
Description : Shows how to assign several variables in a single line.
Explanation : Python allows assigning the same value to multiple names,
              or different values to multiple names, in one statement.
"""

# Same value assigned to three variables
x = y = z = 0
print(x, y, z)

# Different values assigned in one line (tuple unpacking)
a, b, c = 1, 2, 3
print(a, b, c)
