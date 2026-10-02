"""
Program 042: Number Pattern
Description : Prints a triangle of numbers where each row repeats its
              row number (e.g., row 3 -> "3 3 3").
Explanation : The outer loop is the row number; the inner loop prints
              that row number the same number of times as the row index.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
