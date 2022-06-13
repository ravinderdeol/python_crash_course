# function to count the number of words and instances of a word in a file
def count_words(filename):

    # try-except-else block to hand any exceptions that may occur
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"{filename} does not exist")
    
    # the else block will run if the try block does not raise an exception
    else:

        # count the number of times a word appears from the list of words
        word_one = contents.count("doublethink")

        # count the number of times a phrase appear in the contents of the file
        word_two = contents.count("big brother")

        print(f"Occurance Of Words In {filename}:\n- 'Doublethink': {word_one}~ Times\n- 'Big Brother': {word_two}~ Times")

# pass the filename to the function in lowercase
filename = "nineteen_eighty_four.txt".lower()

count_words(filename)

# notes
    # '.split()' splits the file into a list of words
    # 'len()' could be used after 'split' to get an approximate word count