# '{}' defines a dictionary
company_0 = {"name": "tesla",
    "location": "austin",
    "revenue": 53_800_000_000,
    "employees": 99_290,
    }

# "name" is the key and it is used to access the associated value
company_name = company_0["name"].title()
company_location = company_0["location"].title()
company_revenue = company_0["revenue"]
company_employees = company_0["employees"]

message = f"{company_name} is located in {company_location}. It has {company_employees} employees and generates {company_revenue} in revenue."

print(message)

# notes
    # a dictionary is a collection of key-value pairs
    # dictionaries are dynamic so you can add or remove items from them
    # dictionaries retain the order in which they created and added to
    # when storing user submitted data start with an empty dictionary
    # 'del company_0["name"]' would permanently delete that key-value pair
    # 'company_0.get("ceo", "no ceo assigned")' that keyword is used to set a default value when a key is not found
    # with no second arguement in a get method the default value is 'none'