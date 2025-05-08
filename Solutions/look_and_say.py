# Write a function that given a starting value as a string, returns the appropriate sequence as a list. 
# The sequence should be what you see from looking at the value (e.g. 12 = 1112)
# The starting value can have any number of digits. 
# The termination condition is a defined by the maximum number of iterations, also supplied as an argument.

# My solution:
from itertools import groupby

def look_and_say(data='1', maxlen=5):
    sequence = []
    
    for i in range(maxlen):
        current = ""
        for key, value in groupby(data):
            current += f"{len(list(value))}{key}"
        sequence.append(current)
        data = sequence[-1]
        
    return sequence


# Alternative: recursion
# from itertools import groupby                                                   
# def look_and_say(data='1', maxlen=5):                                                    
#       read_string = [[k, len(list(g))] for k, g in groupby(data)]                 
#       output = ""                                                                 
#       for item in read_string:                                                    
#           output += str(item[1]) + item[0]
    
#       maxlen -= 1
#       if maxlen == 0:
#         return [output]
#       return [output] + look_and_say(output, maxlen)