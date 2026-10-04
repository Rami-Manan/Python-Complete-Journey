"""
Program 044: GCD (Greatest Common Divisor) Using a Loop
Description : Finds the GCD of two numbers by brute-force checking.
Explanation : We check every integer from the smaller of the two numbers
              down to 1, and the first one that divides both evenly is
              the GCD.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

smaller = min(a, b)
gcd = 1
for i in range(smaller, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

print(f"GCD of {a} and {b} is {gcd}")
