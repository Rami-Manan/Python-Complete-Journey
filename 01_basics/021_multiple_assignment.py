#!/usr/bin/env python2
import sys

def move_zeros_to_end(nums):
    """Move all zeros in list nums to the end in-place."""
    k = 0
    # First pass: move non-zero values forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    # Second pass: fill the rest with zeros
    for i in range(k, len(nums)):
        nums[i] = 0
    return nums

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    # If first value is test count, parse it. Otherwise treat all as one array.
    try:
        t = int(data[idx])
        idx += 1
    except:
        t = 1  # Single test if conversion fails
    for _ in range(t):
        if idx >= len(data):
            break
        n = int(data[idx]); idx += 1
        # Read n numbers (or use all remaining if n not provided)
        nums = []
        if n > 0 and idx < len(data):
            for i in range(min(n, len(data) - idx)):
                nums.append(int(data[idx + i]))
        else:
            # If no count given, take the rest as one test array
            nums = [int(x) for x in data[idx:]]
        idx += n

        # Apply the zero-moving algorithm
        move_zeros_to_end(nums)
        # Output the modified array (space-separated)
        print(" ".join(str(x) for x in nums))

if __name__ == "__main__":
    main()
