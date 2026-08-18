"""Practice: defining and calling functions."""


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


print(greet("Learner"))
print("Sum:", add_numbers(10, 15))
