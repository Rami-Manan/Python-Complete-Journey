"""
Program 045: LCM (Least Common Multiple) Using a Loop
Description : Finds the LCM of two numbers.
Explanation : The LCM is always a multiple of the larger number, so we
              test successive multiples of the larger number until we
              find one that's also divisible by the smaller number.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

larger = max(a, b)
multiple = larger
while True:
    if multiple % a == 0 and multiple % b == 0:
        lcm = multiple
        break
    multiple += larger

print(f"LCM of {a} and {b} is {lcm}")
