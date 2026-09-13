"""
Program 026: Print Even Numbers from 1 to N
Description : Prints every even number between 1 and a user-given N.
Explanation : range(2, N+1, 2) starts at 2 (the first even number),
              stops after N, and steps by 2 each time -- so it only
              ever lands on even numbers.
"""

n = int(input("Enter N: "))

for num in range(2, n + 1, 2):
    print(num, end=" ")
print()
