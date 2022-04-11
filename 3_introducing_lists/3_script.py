countries = ["vietnam", "argentina", "georgia", "china"]

# 'sorted()' lets you display a list alphabetically without changing the origianl list order
countries_alphabetically = sorted(countries)

# 'len()' returns the length of the list as an integer
countries_number = len(countries)

output = f"i will go to {countries_number} countries: {countries[0]}, {countries[1]}, {countries[2]}, {countries[3]}"

print(output)

# notes
    # 'countries.sort()' would sort the list alphabetically permanently
    # 'countries.sort(reverse = True)' would reverse sort the list alphabetically permanently
    # 'countries.reverse()' would reverse the order of the list permanently not alphabetically