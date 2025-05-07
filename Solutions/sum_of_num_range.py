# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!

# My solution:
def get_sum(a,b):
    if a > b:
        a, b = b, a
    all_nums = [i for i in range(a, b + 1)]
    return sum(all_nums) if a != b else a

# My refactored solution:
def get_sum(a,b):
    if a > b:
        a, b = b, a
    return sum(i for i in range(a, b + 1)) if a != b else a


# Alternative: Do not need to check if a != b, although question does specify to return a or b
# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))