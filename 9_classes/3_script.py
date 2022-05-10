# capitalised names are reserved for classes
class Restaurant:

    # 'self' is required as the first argument in every method definition
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

        # default value set for an attribute
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.name} Has Served {self.number_served} Customers {self.cuisine} Food")

# this creates an instance of the class
new_restaurant = Restaurant("Pasta Hut", "Italian")

# modifying the attribute value directly
new_restaurant.number_served = 10

# use the dot notation to call methods
new_restaurant.describe_restaurant()

# notes
    # when an instance is created attributes can be defined without being passed as parameters
    # you can change the value of an attribute directly through an instance as in this example