# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9

# My solution:
def square_sum(numbers):
    result = 0
    for num in numbers:
        result += num * num
    return result

# Alternatives:
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

# def square_sum(numbers):
#     return sum(x * x for x in numbers) 