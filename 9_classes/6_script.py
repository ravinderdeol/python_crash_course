# capitalised name to represent a class
class User:

    # the init method has two trailing and leading underscores
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nAge: {self.age} \nLocation: {self.location} \nEmail: {self.email} \nLogin Attempts: {self.login_attempts}")

user_1 = User("John", "Doe", "25", "London, UK", "johndoe@xyz.co.uk")

# incrementing attribute values using a method
user_1.increment_login_attempts()
user_1.increment_login_attempts()

user_1.describe_user()

# modifying attribute values using a method
user_1.reset_login_attempts()

user_1.describe_user()

# notes
    # an example of modifying an incrementing attribute values using a method