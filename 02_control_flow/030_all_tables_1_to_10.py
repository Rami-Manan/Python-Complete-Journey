"""
Program 030: Print Multiplication Tables from 1 to 10
Description : Prints the multiplication tables for every number 1-10.
Explanation : A nested loop -- the outer loop picks the table number,
              the inner loop prints that table from 1x to 10x.
"""

for table in range(1, 11):
    print(f"--- Table of {table} ---")
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
    print()  # blank line between tables
