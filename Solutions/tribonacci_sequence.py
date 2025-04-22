# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
# You need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and 
# be ready for anything else which is not clearly specified ;)


# My Solution:
def tribonacci(signature, n):
    
    if n <= len(signature): # If n is less than or equal to signature length
        return signature[:n]
    
    while len(signature) < n:
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature

# Alternatives:
# def tribonacci(signature,n):
#     while len(signature) < n:
#         signature.append(sum(signature[-3:]))
    
#     return signature[:n] # Returns empty array if n == 0


# def tribonacci(signature, n):
#     for i in range(n - 3): # Include initial signature of 3 in n
#         signature.append(sum(signature[-3:])) # Add the sum of the last three numbers
#     return signature[:n] # Return signature up to n (empty array if n == 0)