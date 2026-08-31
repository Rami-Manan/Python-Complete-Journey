"""
Program 015: Check Even or Odd
Description : Determines whether a number is even or odd.
Explanation : A number is even if it is exactly divisible by 2
              (remainder 0 when using the modulo operator %).
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
