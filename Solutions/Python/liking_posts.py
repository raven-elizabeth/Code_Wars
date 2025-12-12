# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. 

#     empty = "no one likes this"
#     one = "%s likes this"
#     two = "%s and %s like this"
#     three = "%s, %s and %s like this"
#     more = "%s, %s and %s others like this"


# My Solution:
def likes(names):
    likes = len(names)
    
    if likes == 0:
        return "no one likes this"
    elif likes == 1:
        return f"{names[0]} likes this"
    elif likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {likes - 2} others like this"
    

# My Alternative:
def likes(names):
    likes = len(names)
    first_name = names[0] if likes > 0 else ''
    second_name = names[1] if likes > 1 else ''
    third_name = names[2] if likes > 2 else ''
    message = {
        0: "no one likes this",
        1: f"{first_name} likes this",
        2: f"{first_name} and {second_name} like this",
        3: f"{first_name}, {second_name} and {third_name} like this",
        4: f"{first_name}, {second_name} and {likes - 2} others like this"
    }
    return message[likes if likes < 4 else 4]