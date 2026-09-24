"""
Program 037: Print Armstrong Numbers up to N
Description : Lists every Armstrong number from 1 up to a given N.
Explanation : Applies the Armstrong check (digit sum raised to digit
              count) to every number in the range and prints matches.
"""

n = int(input("Enter N: "))

print(f"Armstrong numbers up to {n}:")
for num in range(1, n + 1):
    digits = str(num)
    power = len(digits)
    if sum(int(d) ** power for d in digits) == num:
        print(num, end=" ")
print()
