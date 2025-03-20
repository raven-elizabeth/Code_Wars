# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.


# My first solution:
def validate_with_isdigit(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    return False


# RegEx solution:
import re

def validate_with_regex(pin):
    four_digits = re.search("\d{4}", pin)
    six_digits = re.search("\d{6}", pin)
    
    if (len(pin) == 4 and four_digits) or (len(pin) == 6 and six_digits):
        return True
    return False


# Alternatives:
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()


# if re.fullmatch("\d{4}|\d{6}", pin):
#         return True
#     else:
#         return False