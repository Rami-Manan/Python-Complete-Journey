"""
Program 058: Nested Functions and Closures
Description : Demonstrates a closure -- an inner function that
              "remembers" a variable from its enclosing function.
Explanation : Even after outer_function() has finished running, the
              inner function retains access to 'count' because it
              formed a closure over it.
"""

def make_counter():
    """Return a function that increments and returns a private counter."""
    count = 0

    def counter():
        nonlocal count  # allows modifying the enclosing variable
        count += 1
        return count

    return counter

my_counter = make_counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3
