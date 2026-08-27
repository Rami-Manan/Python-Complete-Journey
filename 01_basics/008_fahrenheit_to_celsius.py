"""
Program 008: Fahrenheit to Celsius
Description : Converts a temperature from Fahrenheit to Celsius.
Explanation : Uses the standard formula C = (F - 32) * 5/9.
"""

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is equal to {celsius}°C")
