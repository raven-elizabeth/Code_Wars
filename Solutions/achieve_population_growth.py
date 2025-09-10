# In a small town the population is p0 = 1000 at the beginning of a year. 
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?


# More generally given parameters:
# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.
# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

# Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.
# There are no fractions of people. At the end of each year, the population count is an integer: 252.8 people round down to 252 persons.

# My solution:
import math
def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        counter += 1
        p0 = math.floor(p0 + (p0 * (percent/100)) + aug)
    return counter


# Alternatives:

# int() will ignore anything past the decimal point for positive numbers
# aug will always be an int so do not need to include it in rounding a potential decimal
# multiplying by 1.percent is the same as adding the current population again
def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        p0 = int(p0 * (1 + percent/100)) + aug
        counter += 1
    return counter

# Recursive
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years