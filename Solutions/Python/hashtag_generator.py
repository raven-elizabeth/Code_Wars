# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

# My solution:
def generate_hashtag(s):
    s = s.split()
    result = "#" + "".join(word.title() for word in s)
    if len(result) > 140 or len(result) == 1:
        return False
    return result


# My refactored solution:
def generate_hashtag(s):
    s = s.title().split()
    result = "#" + "".join(s)
    return False if len(result) > 140 or len(result) == 1 else result


# My alternative refactored solution:
def generate_hashtag(s):
    s = "#" + s.title().replace(" ", "")
    return False if len(s) > 140 or len(s) == 1 else s