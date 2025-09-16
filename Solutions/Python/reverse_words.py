# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# My solution
def reverse_words(text):
    reversed_words = text[::-1].split(" ") # Reverse whole sentence, split sentence into list of words based on each single space
    return " ".join(reversed_words[::-1])  # Join list into sentence again, reversed again so word order is correct

# Alternative: Only reverse once
def reverse_words(str):
    return " ".join(s[::-1] for s in str.split(" ")) # Split sentence into word list and rejoin each word reversed

