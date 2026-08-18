"""Practice: basic problem-solving programs."""


def is_even(number):
    """Return True if number is even, else False."""
    return number % 2 == 0


def sum_of_first_n_numbers(n):
    """Return sum from 1 to n."""
    return n * (n + 1) // 2


number = 8
print(f"Is {number} even?", is_even(number))

n = 10
print(f"Sum of first {n} numbers:", sum_of_first_n_numbers(n))
