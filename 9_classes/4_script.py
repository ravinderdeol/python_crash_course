# capitalised names are reserved for classes
class Restaurant:

    # 'self' is required as the first argument in every method definition
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

        # default value set for an attribute
        self.number_served = 0
    
    # method to modify the attributes value
    def set_number_served(self, served):
        self.number_served = served
    
    def describe_restaurant(self):
        print(f"{self.name} Has Served {self.number_served} Customers {self.cuisine} Food")

# this creates an instance of the class
new_restaurant = Restaurant("Pasta Hut", "Italian")

# modifying the attribute value using the method
new_restaurant.set_number_served(10)

# use the dot notation to call methods
new_restaurant.describe_restaurant()

# notes
    # you can change the value of an attribute through a method as in this example
    # an if/else statement could be used in 'set number served' to avoid negative number changes