# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# You can assume that all values are integers. Do not mutate the input array.

# My solution:
def invert(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num * -1)
    return new_lst


# Alternative solution:
# def invert(lst):
#     return [-x for x in lst]