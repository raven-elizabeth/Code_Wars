# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# My solution:
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Ternary operator example:
def ternary_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(even_or_odd(7))
print(ternary_even_or_odd(7))