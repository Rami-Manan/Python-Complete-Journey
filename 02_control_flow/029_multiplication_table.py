"""
Program 029: Multiplication Table of a Number
Description : Prints the multiplication table (1x to 10x) of a given number.
Explanation : A simple for loop multiplies the number by each value
              from 1 to 10 and prints the result.
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
