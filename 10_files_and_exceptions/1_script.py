# assign the filename to a variable
filename = "pi.txt"

with open(filename) as file_object:

    # 'readlines()' takes each line in a file and stores it in a list
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    
    # 'strip()' removes whitespace from the start and end of a string
    pi_string += line.strip()

print(pi_string)

# notes
    # files outside of the current directory should be assigned with an absolute path
    # you can nest a for loop inside an open function to examine each line of a file
    # when python reads from a text file it interprets everything as a string