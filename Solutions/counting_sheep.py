# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# My solution:
def count_sheep(n):
    counting = ""
    if n > 0:
        for i in range(n):
            counting = counting + str(i+1) + " sheep..."
    return counting


# Alternative:
# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))