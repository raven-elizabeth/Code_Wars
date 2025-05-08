# Complete the solution so that the function will break up camel casing, using a space between words.

# My solution:
def solution(s):
    separate = [char for char in s]
    for index, char in enumerate(separate):
        if char == char.upper():
            separate[index] = " " + char
    return "".join(separate)


# Alternatives:
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

# import re
# def solution(s):
#     return re.sub('([A-Z])', r' \1', s)
