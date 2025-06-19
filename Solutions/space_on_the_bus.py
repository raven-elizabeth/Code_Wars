# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
# With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! 
# He wants you to write a simple program telling him if he will be able to fit all the passengers.
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

# My solution
def enough(cap, on, wait):
    total = on + wait
    return 0 if total <= cap else total - cap


# Alternative: Using max()
# def enough(cap, on, wait):
#     return max(0, on + wait - cap)