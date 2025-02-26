# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# My solution:
def double_char(s):
    new_str = ""
    for i in s:
        new_str = new_str + i + i
    return new_str
        

# Alternatives:
# def double_char(s):
#     res = ''
#     for i in s:
#         res += i*2
#     return res


# def double_char(s):
#     return ''.join(c * 2 for c in s)