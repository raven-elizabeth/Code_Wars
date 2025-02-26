# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. 
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# My solution (long-winded):
def DNA_strand(dna):
    complementary_dna = ""
    for i in dna:
        if i == "A":
            i = "T"
        elif i == "T":
            i = "A"
        elif i == "C":
            i = "G"
        else:
            i = "C"
        complementary_dna += i
    return complementary_dna

# Alternatives: Could have used a dictionary or .translate


# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))


# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])


# def DNA_strand(dna):
#     reference = { "A":"T",
#                 "T":"A",
#                 "C":"G",
#                 "G":"C"
#                 }
#     return "".join([reference[x] for x in dna])