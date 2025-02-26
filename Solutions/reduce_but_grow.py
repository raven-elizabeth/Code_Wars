# Given a non-empty array of integers, return the result of multiplying the values together in order.
# Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


# My solution:
array = [2, 6, 4, 3, 1]

def grow(list):
    solution = 1
    for num in list:
        solution *= num
    return solution


# Alternatives:


# import math
# def grow(arr):
#     return math.prod(arr)


# from math import prod as grow