# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# My solution
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    return number * 9

# My refactored solution
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# Alternatives
# Based on number leftover when dividing by two being boolean 1 (odd number)
# def simple_multiplication(number) :
#     return number * 9 if number % 2 else number * 8

# Less repetitive
# def simple_multiplication(number) :
#     return number * (8 if number % 2 == 0 else 9)

# Multiply based on 0 or 1 result for 2 division remainder
# def simple_multiplication(n) :
#     return n * (8 + n%2)