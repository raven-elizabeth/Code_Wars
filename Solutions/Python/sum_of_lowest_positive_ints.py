# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.


# My pseudocode:

# Return lowest positive numbers
# Minimum 4 positive int
# No floats or non-positive inputs

# Steps:
# Order list
# Return sum of first and second index (0 + 1)

# My solution:
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]