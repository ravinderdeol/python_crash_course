# function to count the number of words and instances of a word in a file
def count_words(filename):

    # code that could cause an exception goes in the try block
    try:
        with open(filename) as f:
            contents = f.read()

    # handles the 'file not found error' exception
    except FileNotFoundError:
        print(f"{filename} does not exist")
    
    # else block will run if no exceptions is raised
    else:

        # count the number of times a phrase appear in the text file
        word_one = contents.count("doublethink")
        word_two = contents.count("big brother")

        print(f"Occurrence Of Words In {filename}:\n- 'Doublethink': {word_one}~ Times\n- 'Big Brother': {word_two}~ Times")

# pass the filename to the function in lowercase
filename = "nineteen_eighty_four.txt".lower()

count_words(filename)

# notes
    # '.split()' splits the file into a list of words
    # 'len()' could be used after 'split' to get an approximate word count