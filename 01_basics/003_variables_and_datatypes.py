"""
Program 003: Variables and Data Types
Description : Demonstrates Python's core built-in data types.
Explanation : Python is dynamically typed -- a variable's type is decided by
              the value assigned to it, and can change at runtime. type()
              returns the class of an object so we can inspect it.
"""

integer_var = 10          # int    -> whole numbers
float_var = 3.14          # float  -> decimal numbers
string_var = "Python"     # str    -> text
bool_var = True           # bool   -> True/False
list_var = [1, 2, 3]       # list   -> ordered, mutable collection
tuple_var = (1, 2, 3)      # tuple  -> ordered, immutable collection
dict_var = {"key": "val"}  # dict   -> key-value pairs
set_var = {1, 2, 3}        # set    -> unordered, unique elements

# Loop through each variable and print its value alongside its type
for value in (integer_var, float_var, string_var, bool_var,
              list_var, tuple_var, dict_var, set_var):
    print(f"Value: {value!r:<20} Type: {type(value).__name__}")
