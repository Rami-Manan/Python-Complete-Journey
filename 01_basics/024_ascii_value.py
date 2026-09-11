"""
Program 024: ASCII Value of a Character
Description : Prints the ASCII/Unicode code point of a character, and
              vice versa.
Explanation : ord() converts a single character to its integer code
              point. chr() does the reverse, converting an integer
              back to its character.
"""

char = input("Enter a single character: ")
print(f"ASCII value of '{char}' is {ord(char)}")

code = int(input("Enter an ASCII code: "))
print(f"Character for code {code} is '{chr(code)}'")
