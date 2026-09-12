"""
Program 025: Roots of a Quadratic Equation
Description : Solves ax^2 + bx + c = 0 for its roots.
Explanation : Uses the quadratic formula x = (-b +- sqrt(b^2 - 4ac)) / 2a.
              The discriminant (b^2 - 4ac) determines whether the roots
              are real & distinct, real & equal, or complex.
"""

import cmath  # supports complex square roots for negative discriminants

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c
root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
