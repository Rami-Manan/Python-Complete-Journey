"""
Program 050: Recursive Factorial
Description : Calculates N! using recursion instead of a loop.
Explanation : A recursive function calls itself with a smaller input
              until it reaches a 'base case' (here, n == 0) that stops
              the recursion.
"""

def factorial(n):
    """Return n! using recursion."""
    if n == 0:               # base case: 0! is defined as 1
        return 1
    return n * factorial(n - 1)  # recursive case

n = int(input("Enter a non-negative integer: "))
print(f"{n}! = {factorial(n)}")
