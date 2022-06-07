# an example of a list nested inside a dictionary
favorite_places = {"hannah": ["paris", "london"],
    "joe": ["valletta"],
    "jane": ["manchester", "barcelona", "zurich"],
    }

# 'name' is the key and 'place' is the value
# 'sorted()' outputs the data in alphabetical order
for name, place in sorted(favorite_places.items()):

    # 'len()' checks the length of the list and depending on the result changes the output
    if len(place) > 1:
        print(f"\n{name.title()}'s favorite places are:")
    else:
        print(f"\n{name.title()}'s favorite place is:")

    # prints the list of favorite places for each person
    for place in place:
        print(f"\t{place.title()}")

# notes
    # the for loop goes through each item chronologically