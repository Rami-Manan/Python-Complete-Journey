"""
Program 002: Add Two Numbers
Description : Takes two numbers from the user and prints their sum.
Explanation : input() always returns a string, so we convert it to float
              using float() before doing arithmetic. Using float (instead of
              int) lets the program also accept decimal numbers.
"""

# Read two numbers from the user, converting text input to float
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add them together
total = num1 + num2

# Display the result using an f-string
print(f"The sum of {num1} and {num2} is {total}")
