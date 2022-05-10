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
    
    def increment_number_served(self, number):
        self.number_served += number
    
    def describe_restaurant(self):
        print(f"{self.name} Has Served {self.number_served} Customers {self.cuisine} Food")

# this creates an instance of the class
new_restaurant = Restaurant("Pasta Hut", "Italian")

# modifying attribute values using a method then using dot notation to call a method
new_restaurant.set_number_served(10)
new_restaurant.describe_restaurant()

# incrementing attribute values using a method then using dot notation to call a method
new_restaurant.increment_number_served(5)
new_restaurant.describe_restaurant()

# notes
    # you can increment the value of an attribute through a method as in this example