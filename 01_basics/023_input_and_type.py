"""
Program 023: Take User Input and Print Its Type
Description : Reads raw input from the user and shows that input()
              always returns a string.
Explanation : Even if the user types a number, input() hands it back
              as str; you must explicitly convert it if you need a
              number for arithmetic.
"""

value = input("Enter anything: ")
print(f"You entered: {value}")
print(f"Type of input: {type(value)}")  # Always <class 'str'>
