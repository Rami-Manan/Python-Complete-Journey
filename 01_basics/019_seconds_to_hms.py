"""
Program 019: Convert Seconds to HH:MM:SS
Description : Converts a duration given in seconds into hours, minutes,
              and seconds.
Explanation : Integer division (//) gives whole hours/minutes, and the
              modulo operator (%) gives the remainder to carry forward.
"""

total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
