"""
Program 051: Recursive Fibonacci
Description : Calculates the Nth Fibonacci number using recursion.
Explanation : fib(n) = fib(n-1) + fib(n-2), with base cases fib(0)=0
              and fib(1)=1. Note: this naive version is exponential
              time -- fine for small n, but slow for large n.
"""

def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed) using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {fibonacci(n)}")
