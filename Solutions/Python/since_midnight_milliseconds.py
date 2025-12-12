# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

# My solution:
def past(h, m, s):
    hours = h * 60 * 60 * 1000
    minutes = m * 60 * 1000
    seconds = s * 1000
    return hours + minutes + seconds

# My condensed solution:
def past(h, m, s):
    return h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000


# Alternative:
# def past(h, m, s):
#     return (3600*h + 60*m + s) * 1000