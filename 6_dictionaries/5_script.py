# an example of a dictionary nested inside a list
companies = [{"name": "tesla", "revenue": 53_800_000_000, "employees": 99_290},
    {"name": "rivian", "revenue": 55_000_000, "employees": 11_500}]

for company in companies:
    print(f"{company['name'].title()} generates {company['revenue']} with {company['employees']} employees")

# notes
    # you can nest lists of items inside dictionaries
    # you can nest dictionaries inside dictionaries but it can get complicated
    # do not nest too deeply
    # nest whenever you want multiple values associated with a key