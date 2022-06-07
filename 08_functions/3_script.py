# 'new_user' is a function with two parameters with one having a default value
def new_user(email, username = "undefined"):
    print("here are your credentials:")
    print(f"\temail: {email}")
    print(f"\tusername: {username}")

# function call using keyword arguments
new_user(email = "test@gmail.com", username = "test_user")

# notes
    # if no 'username' was called it would default to 'undefined'
    # use default values after parameters which do not have them
    # use the style you find easiest and keep it consistent
    # keyword arguments free you from the worry of ordering arguments