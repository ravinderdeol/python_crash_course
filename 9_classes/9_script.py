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

class Privileges:

    # method stores the list of privileges
    def __init__(self, privileges = ["Can Add Post", "Can Delete Post", "Can Ban User"]):
        self.privileges = privileges
    
    # new method to display the list of privileges
    def show_privileges(self):
        print(f"Privileges: {self.privileges}")

class Admin(User):
    
        # inherits attributes from the parent class using the 'super' function
        def __init__(self, first_name, last_name, age, location, email):

            # initialise the attributes of the parent class
            super().__init__(first_name, last_name, age, location, email)
            self.privileges = Privileges()

# create an insance of a class
user_1 = User("John", "Doe", "25", "London, UK", "johndoe@xyz.co.uk")
user_2 = Admin("Jane", "Doe", "45", "New York, USA", "janedoe@xyz.com")

# using dot notation to call a method
user_1.describe_user()

user_2.describe_user()
user_2.privileges.show_privileges()

user_1.greet_user()
user_2.greet_user()

# notes
    # you will start thinking more abstractly about modelling data with classes as your code grows