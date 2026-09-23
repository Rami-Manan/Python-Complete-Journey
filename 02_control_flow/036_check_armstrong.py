"""
Program 036: Check Armstrong Number
Description : An Armstrong number equals the sum of its own digits each
              raised to the power of the digit count (e.g., 153 = 1^3+5^3+3^3).
Explanation : Count the digits, then sum each digit raised to that power,
              and compare the result to the original number.
"""

n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)

total = sum(int(d) ** power for d in digits)

if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is NOT an Armstrong number")
