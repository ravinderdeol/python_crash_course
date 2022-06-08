filename = "guest_book.txt"

# creates or opens a file in append mode
with open(filename, "a") as file_object:

    while True:

        # continue to prompt the user for an input until they enter 'q'
        name = input("enter a name (or enter 'q' to stop): ").lower()

        if name == "q":
            break

        # print a greeting to the guest and write each name to a text file on a new line
        else:
            print(f"Welcome, {name.title()}!")
            file_object.write(name + "\n")

# notes
    # if no mode is specified python defaults to read mode
    # any numerical data must be converted to a string before it can be written to a file