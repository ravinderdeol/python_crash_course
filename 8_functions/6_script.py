# '*fillings' collects an arbitrary number of arguments from the calling statement
def make_sandwich(*fillings):

    print("Making A Sandwich With:")
    
    for filling in fillings:
        print(f"- {filling.title()}")

make_sandwich("chicken", "avocado", "onion", "mayonnaise")

# notes
    # '*fillings' create an empty tuple and pack in the values
    # if 'make_sandwich' has multiple arguments then '*fillings' should be the last
    # you will often see '*args' to collect arbitrary positional arguments