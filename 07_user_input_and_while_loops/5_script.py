# a dictionary to store the user inputs
responses = {}

# as long as this flag is set to 'true' the loop will continue
polling_active = True

while polling_active:
    name = input("\nenter your name: ")
    location = input("enter a country you want to visit: ")

    # 'responses[]' stores the name (key) and location (value) in the dictionary
    responses[name] = location

    repeat = input("\nenter 'yes' to let another person respond or 'no' to quit: ")

    if repeat == "no":

        # set the flag to 'false' to exit the loop
        polling_active = False

print("\n--- RESULTS ---")

for name, location in responses.items():
    print(f"{name.title()} wants to visit {location.title()}.")

# notes
    # the 'responses' dictionary is a global variable