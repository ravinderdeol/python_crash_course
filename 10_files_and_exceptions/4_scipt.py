print("enter two numbers and i will multiply them (enter 'q' to quit)")

# continually prompt the user for input until they quit the program
while True:
    first_number = input("\nfirst number: ")
    if first_number == 'q':
        break

    second_number = input("second number: ")
    if second_number == 'q':
        break

    # only code that could cause an exception goes in the try block
    try:
        answer = int(first_number) * int(second_number)

    # the except block tells python what to do if an exception occurs
    except ValueError:
        print("please enter a number not text")
    
    # the else block holds code that depends on the success of the try block
    else:
        print(answer)

# notes
    # use 'pass' to not do anything other than continue if an exception occurs