"""
Program 041: Star Pattern - Inverted Triangle
Description : Prints a right-angled triangle upside down.
Explanation : The loop counts DOWN from 'rows' to 1, printing one fewer
              star on each subsequent row.
"""

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print("*" * i)
