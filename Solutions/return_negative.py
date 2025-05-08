# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# My solution:
def make_negative(number):
    return number if number <= 0 else -number


# Alternative:
# def make_negative(number):
#     return -abs(number)