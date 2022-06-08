filename = "guest.txt"

name = input("please enter your name: ").lower()

# creates or opens a file in append mode
with open(filename, "a") as file_object:

    # write to the text file with each entry on a new line
    file_object.write(name + "\n")

# notes
    # "r" opens a file in read mode
    # "w" opens a file in write mode
    # "a" opens a file in append mode
    # "r+" opens a file in read and write mode
    # opening a file in write mode will overwrite the contents of the file
    # open a file in append mode to add to the end of the file