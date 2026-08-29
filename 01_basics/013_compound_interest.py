"""
Program 013: Compound Interest Calculator
Description : Calculates compound interest given principal, rate, time
              and compounding frequency per year.
Explanation : Formula: A = P * (1 + R/(100*N)) ^ (N*T), CI = A - P
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))
n = int(input("Enter compounding frequency per year (e.g., 1, 4, 12): "))

amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {amount:.2f}")
