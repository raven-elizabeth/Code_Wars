# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# My solution:
# An even & odd number will always equal an odd number, else it will equal an even number
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 != 0


# Alternative:
# If the sum is an even number (and therefore they do not love each other) then the modulo will always equal 0 (False), else it will be equivalent to True
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2