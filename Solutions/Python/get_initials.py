# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# # The output should be two capital letters with a dot separating them.
# It should look like this: Sam Harris => S.H, patrick feeney => P.F

# My solution:
def abbrev_name(name):
    first_initial = name[0].upper()
    counter = -1
    for char in name:
        counter += 1
        if char == " ":
            last_initial = name[counter + 1].upper()
    return f"{first_initial}.{last_initial}"  


# Alternative:
# def abbrevName(name):
#     first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]


# Note to self: Look into join() and split()!