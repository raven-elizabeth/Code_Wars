# Your friend Bob is working as a taxi driver. After working for a month he is frustrated in the city's traffic lights. 
# He asks you to write a program for a new type of traffic light. It is made so it turns green for the road with the most congestion.

# Task:
# Given 2 pairs of values each representing a road (the number of cars on it and its name), 
# construct an object whose turngreen method returns the name of the road with the most traffic at the moment of the method call, and clears that road from cars.
# After both roads are clear of traffic, or if the number of cars on both roads is the same from the beginning, return an empty value instead.

# My solution:
class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.queue1, self.st1 = st1
        self.queue2, self.st2 = st2
        
    def turngreen(self):
        if self.queue1 == self.queue2:
            return None
        elif self.queue1 > self.queue2:
            self.queue1 = 0
            return self.st1
        self.queue2 = 0
        return self.st2


