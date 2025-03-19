# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

# My notes:
# All sides must be greater than 0 - sorting the list verifies this as adding 0 will never get to larger than the max value
# Sum of two shorter sides must be greater than third side (googled for this and watched a video: https://youtu.be/PlTvrLLTAAE?si=BJ_WYsF1CUZ4K0Lz)

# My solution:
def is_triangle(a, b, c):
    values = [a, b, c]
    values.sort()
    
    if values[0] + values[1] > values[2]:
        return True
    return False


# My alternative:
def is_triangle(a, b, c):
    values = [a, b, c]
    values.sort()
    return values[0] + values[1] > values[2]