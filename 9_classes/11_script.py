from admin import Admin

# create an insance of a class
user_1 = Admin("Jane", "Doe", "45", "New York, USA", "janedoe@xyz.com")

# using dot notation to call a method
user_1.describe_user()
user_1.privileges.show_privileges()

# user_1.greet_user()
user_1.greet_user()

# notes
    # write a docstring for each module that you create
    # each class in a module should be related somehow