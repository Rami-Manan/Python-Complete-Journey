"""
Program 052: Recursive Sum of a List
Description : Sums all elements in a list using recursion.
Explanation : The base case is an empty list (sum is 0). The recursive
              case adds the first element to the sum of the rest of
              the list.
"""

def recursive_sum(lst):
    """Return the sum of all numbers in lst using recursion."""
    if not lst:              # base case: empty list
        return 0
    return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"Sum: {recursive_sum(numbers)}")
