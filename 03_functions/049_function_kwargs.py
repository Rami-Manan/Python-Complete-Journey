"""
Program 049: Function with **kwargs (Variable Keyword Arguments)
Description : Defines a function that accepts any number of named
              (keyword) arguments and prints them.
Explanation : **kwargs collects keyword arguments into a dictionary,
              letting the caller pass an arbitrary set of named values.
"""

def print_details(**kwargs):
    """Print each keyword argument as 'key: value'."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Manan", course="Computer Science", year=2)
