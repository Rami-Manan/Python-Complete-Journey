"""
Program 040: Star Pattern - Pyramid
Description : Prints a centered pyramid of asterisks.
Explanation : Each row needs (rows - i) leading spaces to center it, and
              (2*i - 1) stars, which is the classic formula for an
              odd-numbered, symmetric pyramid row.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
