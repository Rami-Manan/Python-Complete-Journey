"""
Program 053: Lambda Function Basics
Description : Demonstrates anonymous (lambda) functions.
Explanation : A lambda is a small, unnamed function defined in a single
              expression: 'lambda arguments: expression'. It's useful
              for short, throwaway functions.
"""

square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"Sum of 3 and 4: {add(3, 4)}")
