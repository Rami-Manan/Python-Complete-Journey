"""
Program 056: reduce() with Lambda
Description : Uses functools.reduce to compute the product of a list.
Explanation : reduce(function, iterable) repeatedly applies 'function'
              to pairs of elements, collapsing the whole iterable down
              to a single cumulative value.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)

print(f"Numbers: {numbers}")
print(f"Product: {product}")
