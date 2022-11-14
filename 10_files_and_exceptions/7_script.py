# import json into the file
import json

# function to get the handle from the json file
def get_stored_handle():

    filename = "handle.json"

    # open the file in read mode
    try:
        with open(filename) as f:
            handle = json.load(f)
    
    # exception returns none in this function if no file is found
    except FileNotFoundError:
        return None
    
    # else statement returns the handle in this function if it found
    else:
        return handle

# function to create a handle if one is not found
def create_handle():

    handle = input("enter a handle name to reserve it: ")

    filename = "handle.json"

    with open(filename, "w") as f:
        # dump the input from the user into the json file
        json.dump(handle, f)
    
    # return the handle in this function after creating it
    return handle

# function to greet the user with their handle
def greet_user():

    # get the handle from the get_store_handle() function
    handle = get_stored_handle()

    # if the get_stored_handle() function returns a handle then this will trigger
    if handle:
        print(f"you have already reserved @{handle}")

    # if the get_stored_handle() function does not return a handle then this will trigger
    else:
        handle = create_handle()
        print(f"@{handle} - reserved")

greet_user()

# notes
    # functions should either return the value you are expecting or none