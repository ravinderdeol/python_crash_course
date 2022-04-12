# an example of a dictionary nested inside a dictionary
cities = {
        "paris": {
            "country": "france",
            "population": 2_165_423,
        },
    
        "london": {
            "country": "england",
            "population": 8_902_929,
        },
    }

# 'city' is the key
# 'description' is the value which holds the information about the city
for city, description in cities.items():
    
    # '{description[country]}' is how to get the value of the key inside a dictionary
    print(f"{city.title()} is in {description['country'].title()} and it has a population of {description['population']}")

# notes
    # do not nest too deeply else it will be hard to read