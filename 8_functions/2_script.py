# 'describe_city' is a function with two parameters
def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}.")

# function call using positional arguments
describe_city('paris', 'france')

# notes
    # 'positional arguments' are when you pass the arguments in the order they are defined
    # 'keyword arguments' are when you pass the arguments associating them with the parameter names