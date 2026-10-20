"""
Program 059: Function Returning Multiple Values
Description : Returns several values from one function call.
Explanation : Python lets a function 'return a, b, c', which is really
              returning a single tuple (a, b, c) that the caller can
              unpack into separate variables.
"""

def get_min_max(numbers):
    """Return (minimum, maximum) of the given list."""
    return min(numbers), max(numbers)

low, high = get_min_max([4, 2, 9, 1, 7])
print(f"Minimum: {low}, Maximum: {high}")
