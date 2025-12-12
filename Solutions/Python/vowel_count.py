# Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# My solution:
def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in vowels:
        count += sentence.count(char)
    return count


# Alternative:
# def getCount(s):
#     return sum(char in 'aeiou' for char in s)