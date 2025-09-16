# Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number of times it appears). 
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# My solution:
import math
def comp(array1, array2):
    
    true = 0
    if array1 and array2:
        for i in array2:
            sqrt = math.sqrt(i)
            if sqrt in array1:
                true += 1
                array1.remove(sqrt)
            elif -sqrt in array1:
                true += 1
                array1.remove(-sqrt)
                
        return true == len(array2)
    
    elif array1 == array2:
        return True
    return False


# Alternatives:
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
    

def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []