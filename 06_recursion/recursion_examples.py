"""Practice: recursion with factorial."""


def factorial(number):
    """Return factorial using recursion."""
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


value = 5
print(f"Factorial of {value} is", factorial(value))
