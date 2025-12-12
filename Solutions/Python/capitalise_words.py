# When writing on Twitter, Jaden Smith is known for almost always capitalizing every word.
# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# My reasoning:
# .title() capitalises any letters that come after a non-letter, so letters after apostrophes are capitalised
# Not necessary for this problem, but I have converted to lowercase first for a blank slate

# My solution:
def to_jaden_case(string):
    list = [word.capitalize() for word in string.lower().split()] # Make a list of capitalised words by splitting string
    return " ".join(list) # Convert separate words in list into a string with .join()


# Alternatives:
# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())


# import string
# toJadenCase = string.capwords