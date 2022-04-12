crypto_description = {"bitcoin": "digital gold",
    "ethereum": "programmable contracts and money",
    "ripple": "enterprise payment settlement network",
    }

# for loop which formats and prints items in the dictionary
for key, value in crypto_description.items():
    print(f"{key.title()}: {value.title()}")

# notes
    # use of a for loop to format refines the code