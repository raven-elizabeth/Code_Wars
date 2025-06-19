# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.

# My solution
def find_uniq(arr):
    # Sort array
    # Check if first item is equal to second
    # If so, return arr[-1], else return arr[0]
    
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]


# Alternatives
# Using set()
# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b

# Using collections
# from collections import Counter
# def find_uniq(a):
#     # Return least common by reversing
#     return Counter(a).most_common()[-1][0]

# Find lowest count of item via min()
# def find_uniq(arr):
#         return min(set(arr),key=arr.count)