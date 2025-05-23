# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.
# Examples:
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28

# My solution:
def century(year):
    if year < 100:
        return 1
    elif year < 1000:
        return int(str(year)[0]) + 1
    
    return int(str(year)[:2]) if str(year)[-2:] == "00" else int(str(year)[:2]) + 1


# Alternatives:
# def century(year):
#     return year // 100 if year % 100 == 0 else (year // 100 + 1)

# def century(year):
#     return (year + 99) // 100

# import math
# def century(year):
#     return math.ceil(year / 100)