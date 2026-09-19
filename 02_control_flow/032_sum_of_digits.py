"""
Program 032: Sum of Digits of a Number
Description : Adds up all the digits of an integer (e.g., 123 -> 1+2+3=6).
Explanation : Same digit-extraction technique as reversing a number:
              peel off the last digit with % 10, add it to a running
              total, then shrink the number with // 10.
"""

n = abs(int(input("Enter an integer: ")))

digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10

print(f"Sum of digits: {digit_sum}")
