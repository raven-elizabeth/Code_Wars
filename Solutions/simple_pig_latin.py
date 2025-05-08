# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# My solution:
import string
def pig_it(text):
    text = text.split()
    
    for index, word in enumerate(text):
        for char in word:
            if char not in string.punctuation:
                text[index] = text[index].replace(char, "", 1)
                text[index] += f"{char}ay"
                break
    return " ".join(text)


# Alternative: RegEx
import re
def pig_it(text):
    # Replaces text by splitting the first letter and the following (* = zero or more) letters of each word, 
    # then at the end of the word (\2), adds the first letter (\1) and "ay"
    return " ".join([re.sub(r"([a-z])([a-z]*)", r"\2\1ay", text, 1, flags=re.I) for text in text.split()])

# Alternative: isalnum()
# Punctuation will be separated by a space so will count as its own word
# def pig_it(text):
#     return ' '.join([word[1:] + word[0] + 'ay' if word.isalnum() else word for word in text.split()])
