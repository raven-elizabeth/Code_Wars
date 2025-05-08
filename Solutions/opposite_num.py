# Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

# My solution:
def opposite(number):
    return -abs(number) if number > 0 else abs(number)


# Alternative:
# def opposite(number):
#     return -number