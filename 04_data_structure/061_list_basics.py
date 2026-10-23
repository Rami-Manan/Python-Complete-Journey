"""
Program 061: List Basics (Create, Access, Slice)
Description : Demonstrates creating a list and accessing/slicing it.
Explanation : Lists are ordered, mutable collections. Indexing starts
              at 0; negative indices count from the end. Slicing
              list[start:stop] extracts a sub-list (stop is excluded).
"""

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"Full list: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"First three: {fruits[0:3]}")
print(f"Every other item: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")
