# Write a function that takes an array of numbers (integers for the tests) and a target number. 
# It should find two different items in the array that, when added together, give the target value. 
# The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
#                                 target will always be the sum of two different items from that array).

# My solution
def two_sum(numbers, target):
    for first_idx, i in enumerate(numbers):
        for second_idx, j in enumerate(numbers):
            if first_idx != second_idx and i + j == target:
                return first_idx, second_idx
            

# Alternatives
# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if (numbers[i] + numbers[j]) == target:
#                 return i, j
            
# def two_sum(numbers, target):
#     for idx1, i in enumerate(numbers[:-1]):
#         for idx2, j in enumerate(numbers[idx1+1:]):
#             if i + j == target:
#                 # Add first index + 1 to account for new starting point for second enumeration
#                 return idx1, idx2 + idx1 + 1