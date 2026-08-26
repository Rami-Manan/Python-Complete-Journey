"""
Program 010: Area and Perimeter of a Rectangle
Description : Calculates the area and perimeter of a rectangle.
Explanation : Area = length * width, Perimeter = 2 * (length + width).
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
