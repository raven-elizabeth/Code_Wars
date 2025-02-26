# Given an array of integers, return a new array with each value doubled.

# My solution:
def maps(a):
    new_array = []
    for num in a:
        new_array.append(num * 2)
    return new_array


# Alternative solution: List comprehension
# def maps(a):
#     return [2 * x for x in a]