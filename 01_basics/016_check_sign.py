"""
Program 016: Check Positive, Negative, or Zero
Description : Classifies a number as positive, negative, or zero.
Explanation : Simple comparison chain using if/elif/else.
"""

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
