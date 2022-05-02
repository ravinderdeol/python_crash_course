# capitalised names are reserved for classes
class Restaurant:

    # 'self' is required as the first argument in every method definition
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name} ({self.cuisine})")

# this creates an instance of the class
new_restaurant = Restaurant("Pasta Hut", "Italian")

# use the dot notation to call methods
new_restaurant.describe_restaurant()

# use the dot notation to access attributes
print(f"Restaurant Name: {new_restaurant.name} ({new_restaurant.cuisine})")

# notes
    # OOP helps to represent world things and situations and create objects based on classes
    # making an object from a class is called instantiation
    # no paranthesis are required after the class name
    # the function of a course is called a method
    # everything about functions is true about classes apart from the way they are called
    # think of classes as a set of instructions for how to make an instance
    # you can create multiple instances from a class