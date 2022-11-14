# import json into the file
import json

# store the name of the file to a variable
filename = "handle.json"

# open the 'filename' in read mode with json.load() if it exists
try:
    with open(filename) as f:
        handle = json.load(f)

# handles the 'file not found error' exception
except FileNotFoundError:
    handle = input("enter a handle name to reserve it: ")

    with open(filename, "w") as f:
        
        # dumps the input from the user into a json file
        json.dump(handle, f)
        print(f"@{handle} - reserved")

# notes
    # 'json.load()' loads the data from a json file
    # 'json.dump()' dumps the data into a json file