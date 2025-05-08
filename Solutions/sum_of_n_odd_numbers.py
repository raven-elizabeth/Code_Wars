# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# My solution:
# Find the pattern from input --> output
def row_sum_odd_numbers(n):
    # 1 --> 1
    # 2 --> 8
    # 3 --> 27
    # 4 --> 64
    # 5 --> 125
    # Pattern: n**3
    return n ** 3