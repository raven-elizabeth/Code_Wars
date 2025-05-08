# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as a list.

# My solution:
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]