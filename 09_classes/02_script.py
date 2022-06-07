# capitalised name to represent a class
class User:

    # the init method has two trailing and leading underscores
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
    
    def describe_user(self):
        print(f"\nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nAge: {self.age} \nLocation: {self.location} \nEmail: {self.email}")
    
    def greet_user(self):
        print(f"\nHi, {self.first_name} ({self.email})")

user_1 = User("John", "Doe", "25", "London, UK", "johndoe@xyz.co.uk")
user_2 = User("Jane", "Doe", "45", "New York, USA", "janedoe@xyz.com")

user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()

# notes
    # you can create multiple instances from a class
    # the init method is run automatically when you create an instance of a class