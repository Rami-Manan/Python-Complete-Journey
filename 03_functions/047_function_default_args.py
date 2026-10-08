"""
Program 047: Function with Default Arguments
Description : Defines a greeting function where the greeting word has a
              default value if the caller doesn't supply one.
Explanation : Parameters with '=value' in the definition become optional;
              if the caller omits them, the default is used instead.
"""

def greet(name, greeting="Hello"):
    """Greet 'name' using 'greeting' (default: 'Hello')."""
    return f"{greeting}, {name}!"

print(greet("Manan"))                 # uses default greeting
print(greet("Manan", "Welcome"))      # overrides the default
