# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. 
# Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, 
# but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. 
# Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

# My solution:
def BracketMatcher(strParam):
  
  # Check brackets match
  left = 0
  for char in strParam:
    if char == "(": 
      left += 1 # Store unmatched left brackets
    
    elif char == ")":
      if left:
        left -= 1 # Matching brackets
      else:
        return 0 # If no preceding left bracket

  return 0 if left else 1 # Return 0 if there are any unmatched left brackets

# keep this function call here 
print(BracketMatcher(input()))