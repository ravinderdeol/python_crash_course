voter_age = {"ryan": 19,
    "joe": 20,
    "susan": 25,
    "hannah": 16,
    }

# 'sorted()' alphabetically organizes the keys
for name, age in sorted(voter_age.items()):

    if age >= 18:
        print(f"{name.title()} (Eligible)")
    else:
        print(f"{name.title()} (Ineligible)")

# notes
    # wrapping in '.set().' would remove duplicates when printing
    # sets have no key-value pair hence do not mistake them for dictionaries