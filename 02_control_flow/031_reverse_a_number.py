"""
Program 031: Reverse a Number
Description : Reverses the digits of an integer (e.g., 1234 -> 4321).
Explanation : Repeatedly extract the last digit with n % 10, append it
              to the reversed result, then remove that digit from n
              using integer division (n // 10).
"""

n = int(input("Enter an integer: "))
original = n
n = abs(n)  # handle negative numbers by working with the magnitude

reversed_num = 0
while n > 0:
    last_digit = n % 10
    reversed_num = reversed_num * 10 + last_digit
    n //= 10

if original < 0:
    reversed_num = -reversed_num

print(f"Reversed number: {reversed_num}")
