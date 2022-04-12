crypto_description = {"bitcoin": "digital gold",
    "ethereum": "programmable contracts and money",
    "ripple": "enterprise payment settlement network",
    "basic attention": "decentralized ad network",
    }

# for loop using '.items()' loops through the key-value pairs in the dictionary
# 'key' and 'value' variable can be replaced with any other variable name
for key, value in crypto_description.items():
    print(f"{key.title()}: {value.title()}")

# notes
    # use of a for loop to format refines the code