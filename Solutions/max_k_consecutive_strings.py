# You are given an array(list) strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# My solution:
def longest_consec(strarr, k):
    consecutives = []
    prev = []
    
    if not strarr or k <= 0 or k > len(strarr):
        return ""
    
    for idx, word in enumerate(strarr):
        prev.append(word)
        if len(prev) == k:
            consecutives.append("".join(prev))
            prev.pop(0)
            
    return max(consecutives, key=len)


# Alternatives:
# def longest_consec(strarr, k):
#     result = ""
    
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s
            
#     return result