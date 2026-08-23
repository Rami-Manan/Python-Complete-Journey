"""
Program 006: Simple Calculator
Description : Performs +, -, *, / on two numbers based on user choice.
Explanation : Uses if/elif/else to branch on the operator string. Division
              is guarded against a zero denominator to avoid crashing.
"""

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2 if num2 != 0 else "Error: division by zero"
else:
    result = "Error: invalid operator"

print(f"Result: {result}")
