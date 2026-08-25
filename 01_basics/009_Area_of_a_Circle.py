"""
Program 009: Area of a Circle
Description : Calculates the area of a circle given its radius.
Explanation : Uses the formula Area = pi * r^2. The math module supplies
              a precise value of pi.
"""

import math

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print(f"Area of the circle: {area:.2f}")
