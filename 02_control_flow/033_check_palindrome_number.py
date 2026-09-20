"""
Program 033: Check Palindrome Number
Description : Checks whether a number reads the same forwards and
              backwards (e.g., 121, 1331).
Explanation : Reverse the number and compare it to the original --
              if they match, it's a palindrome.
"""

n = int(input("Enter an integer: "))
original = n

reversed_num = 0
temp = abs(n)
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10

if original == reversed_num:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is NOT a Palindrome")
