"""
Program 014: BMI Calculator
Description : Calculates Body Mass Index from weight (kg) and height (m),
              and classifies it into a category.
Explanation : Formula: BMI = weight / (height ** 2)
"""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f} ({category})")
