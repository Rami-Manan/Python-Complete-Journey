"""
Program 048: Function with *args (Variable Positional Arguments)
Description : Defines a function that can sum any number of arguments.
Explanation : *args collects any number of positional arguments into a
              tuple inside the function, so the caller isn't limited to
              a fixed parameter count.
"""

def total_sum(*args):
    """Return the sum of any number of numeric arguments."""
    total = 0
    for num in args:
        total += num
    return total

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))
