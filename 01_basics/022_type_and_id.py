"""
Program 022: type() and id() Demo
Description : Shows how to inspect a variable's type and memory identity.
Explanation : type() returns the class of an object. id() returns a
              unique integer identifying the object's location in memory
              for the lifetime of the object.
"""

value = "Python"

print(f"Value : {value}")
print(f"Type  : {type(value)}")
print(f"ID    : {id(value)}")
