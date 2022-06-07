current_users = ["dave@xyz.com", "jim@xyz.com", "sally@xyz.com", "ross@xyz.com", "jane@xyz.com"]

new_users = ["adrian@xyz.com", "Dave@xyz.com", "martin@xyz.com", "JIM@xyz.com", "james@xyz.com"]

for user in new_users:

    # '.lower()' to make the comparison case insensitive
    if user.lower() in current_users:
        print(f"{user} (unavailable")
    else:
        print(f"{user} (available)")

# notes
    # 'lower()' not used would render the program case sensitive