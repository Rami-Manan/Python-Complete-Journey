"""
Program 054: map() with Lambda
Description : Applies a lambda function to every item in a list.
Explanation : map(function, iterable) returns an iterator that applies
              'function' to each element of 'iterable'. list() converts
              that iterator into a concrete list.
"""

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print(f"Original: {numbers}")
print(f"Squared : {squared}")
