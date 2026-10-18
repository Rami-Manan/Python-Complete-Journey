"""
Program 057: Function as an Argument (Higher-Order Function)
Description : Passes a function as an argument to another function.
Explanation : In Python, functions are first-class objects -- they can
              be stored in variables, passed as arguments, and returned
              from other functions.
"""

def apply_operation(a, b, operation):
    """Apply the given 'operation' function to a and b."""
    return operation(a, b)

def multiply(x, y):
    return x * y

result = apply_operation(4, 5, multiply)
print(f"Result: {result}")

# Works with a lambda too
result2 = apply_operation(4, 5, lambda x, y: x + y)
print(f"Result2: {result2}")
