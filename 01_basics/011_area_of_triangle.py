"""
Program 011: Area of a Triangle (Heron's Formula)
Description : Calculates the area of a triangle from its three sides.
Explanation : Heron's formula: s = (a+b+c)/2 (semi-perimeter),
              Area = sqrt(s*(s-a)*(s-b)*(s-c)).
"""

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2                       # semi-perimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area of the triangle: {area:.2f}")
