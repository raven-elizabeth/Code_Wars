# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

# My solution:
from collections import Counter
def count(s):
    return Counter(s)


# Alternative:
def count(string):
    return {char: string.count(char) for char in string}