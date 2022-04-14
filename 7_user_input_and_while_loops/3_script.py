# '+=' creates a multi-line string
greeting_message = "please enter a pizza topping: "
greeting_message += "\n(enter 'quit' when you are finished) \n"

while True:
    user_input = input(greeting_message)

    # 'break' exits the program when the condition is met
    if user_input == 'quit':
        break
    else:
        print(f"{user_input} - added")

# notes
    # there are alternative ways to create a multi-line string