usernames = ["admin", "bob", "joe", "steve", "susan"]

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"hi {username}, want to see a status report?")
        else:   
            print(f"hi {username}, it is good to see you again")
else:
    print("no users")

# notes
    # 'if usernames' would return true if the list was empty and the else statement would run