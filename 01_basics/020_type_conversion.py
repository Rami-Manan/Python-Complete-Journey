"""
Program 020: Type Conversion (Casting)
Description : Demonstrates converting values between int, float, and str.
Explanation : int(), float(), and str() are built-in constructors that
              attempt to convert a value to the requested type, raising
              a ValueError if the conversion is not possible.
"""

s = "42"
print(int(s), type(int(s)))
print(float(s), type(float(s)))

n = 99
print(str(n), type(str(n)))

# Float to int truncates the decimal part, it does not round
f = 9.87
print(int(f))
