user_age = int(input("please enter your age: "))

# this is known as a flag and is helpful for breaking out of a loop
active = True

# the while loop runs as long as 'active' is true
while active:

    if user_age < 3:
        print("admission: $0")
        active = False
    elif user_age < 12:
        print("admission: $10")
        active = False
    else:
        print("admission: $15")
        active = False
        

# notes
    # a while loop will not run if it has nothing to check hence create an empty variable or flag
    # 'break' statement will stop a loop from running
    # 'continue' statement will skip the rest of the code in the loop and start the loop over