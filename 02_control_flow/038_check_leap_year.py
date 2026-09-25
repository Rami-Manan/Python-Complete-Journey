"""
Program 038: Check Leap Year
Description : Determines whether a given year is a leap year.
Explanation : A year is a leap year if it's divisible by 4, EXCEPT
              century years (divisible by 100), UNLESS they are also
              divisible by 400 (e.g., 2000 is a leap year, 1900 is not).
"""

year = int(input("Enter a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(f"{year} is {'a Leap Year' if is_leap else 'NOT a Leap Year'}")
