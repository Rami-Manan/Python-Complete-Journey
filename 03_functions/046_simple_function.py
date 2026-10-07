"""
Program 046: Simple Function with Return Value
Description : Defines a function that adds two numbers and returns the result.
Explanation : 'def' declares a function. The 'return' statement sends a
              value back to the caller; without it, a function implicitly
              returns None.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(5, 3)
print(f"Sum: {result}")
