# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# My reasoning: Needs a mathematical formula
# Reference: 
# Multiply each number by 2 to the power of increasing num from 0, then add all these together (https://www.vcalc.com/wiki/binary-to-integer)
# Start from right to left (https://www.geeksforgeeks.org/binary-to-decimal/)

# My solution:
def binary_array_to_number(arr):
    int_value = 0
    arr.reverse() # Start from right to left
    for index, value in enumerate(arr): # Get to the power of value through corresponding index
        int_value += value * (2 ** index) # Mathematic formula to convert binary to decimal (integer in this case)
    return int_value


# Alternatives: I converted from binary myself, but these methods use int(binary_value, 2) to convert for you

# Join list items into a string using comprehension
# Convert string of binary to integer using int()'s optional parameter of the base format code of original (2 represents binary)
# def binary_array_to_number(arr):
#     return int(''.join(str(a) for a in arr), 2)


# Using map() instead of comprehension
# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)