# Build a function that returns an array of integers from n to 1 where n>0.

# My solution:
def reverse_seq(n):
    return [i for i in range(1, n + 1)][::-1]


# Alternative:
# def reverse_seq(n):
#     return range(n, 0, -1)