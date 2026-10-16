"""
Program 055: filter() with Lambda
Description : Filters a list to keep only the even numbers.
Explanation : filter(function, iterable) keeps only the elements for
              which 'function' returns True.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Evens   : {evens}")
