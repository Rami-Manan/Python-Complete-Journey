"""
Program 039: Star Pattern - Right Triangle
Description : Prints a right-angled triangle made of asterisks.
Explanation : The outer loop controls the row number; the inner loop
              prints that many stars on the current row.
              Row 1 -> 1 star, Row 2 -> 2 stars, etc.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)
