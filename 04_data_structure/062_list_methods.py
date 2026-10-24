"""
Program 062: List Methods Demo
Description : Demonstrates common built-in list methods.
Explanation : append() adds to the end, insert() adds at a position,
              remove() deletes the first matching value, pop() removes
              by index (and returns it), sort() orders in place.
"""

numbers = [5, 2, 8, 1]

numbers.append(9)          # add to the end
numbers.insert(1, 100)     # insert 100 at index 1
numbers.remove(2)          # remove the value 2
popped = numbers.pop()     # remove and return the last item
numbers.sort()             # sort in place, ascending

print(f"Final list: {numbers}")
print(f"Popped value: {popped}")
