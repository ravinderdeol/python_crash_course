# capitalised names are reserved for classes
class Restaurant:

    # 'self' is required as the first argument in every method definition
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name} ({self.cuisine})")

class IceCreamStand(Restaurant):

    # inherits attributes from the parent class using the 'super' function
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)

        # new attribute to store the flavours available
        self.flavours = ["Chocolate", "Strawberry", "Vanilla"]

    # new method to display the list of flavours
    def display_flavours(self):
        print(f"Flavours Available: {self.flavours}")

# create an insance of a class
my_ice_cream = IceCreamStand("Ice Cream Hut", "American")

# using dot notation to call a method
my_ice_cream.describe_restaurant()
my_ice_cream.display_flavours()

# notes
    # use inheritance if the class you are creating is a specialised version of another class
    # when a child class inherits from a parent class it takes on all its attributes and methods
    # to override a method from the parent class in a child class use the same name
    # you will start thinking more abstractly about modelling data with classes as your code grows