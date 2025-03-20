#Emotional Sort: Create a function that will return an array of emotions sorted. It has two parameters.
# The first parameter called will expect an array of emotions where an emotion will be one of the following: :D -> Super Happy, :) -> Happy, :| -> Normal, :( -> Sad, T_T -> Super Sad
# The second parameter will expect a boolean. If true then order of emotions will be descending, if false then will be ascending (from Super Sad to Super Happy)
# The array could be empty, in that case return the same empty array

# My reasoning:

# Given list of symbols representing emotions
# Given true/false
# If true, return emotions list from happiest to most sad
# If false, return reverse of this
# Return empty if array is empty: nothing will happen to arr naturally as it has no corresponding keys in the dictionary

# Steps:
# Have my own dictionary of all emotions from happiest to saddest
# With input array, order list according to matching values in dictionary
# If false, reverse the list

# My solution:
def sort_emotions(arr, order):
    emotion_values = {":D": 1, ":)": 2, ":|": 3, ":(": 4, "T_T": 5} 
    
    # sort() (and sorted()) has optional key parameter for functions to decide ordering (use lambda for throwaway functions)
    arr.sort(key=lambda value: emotion_values[value]) # Sorts arr emotions by values in emotion_values dictionary
    
    if not order: # Reverse order if order is False
        arr.reverse()
    
    return arr

# This took some time, but once I found out about the key= parameter, I had exactly what I was looking for


# Alternative: Similar to mine, but more concise - without lambda and deciding reverse in new sorted() array
# def sort_emotions(arr, order):
#     return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)

# I considered using list indexing, but found it easier to make a dictionary - this method though, of assigning the list as the key, makes sense
# I did not know you could use .index as just a reference for index() (to be used by sorted() when determining the order of the items)
# reverse=not order is clever! I knew reverse= is a parameter but didn't think of just assigning it to the opposite of the order given so it would match

# Perhaps in order to 'return same empty array' it is worth using sort() on arr and then returning arr:
# def sort_emotions(arr, order):
#     arr.sort(key=[":D", ":)", ":|", ":(", "T_T"].index, reverse= not order)
#     return arr