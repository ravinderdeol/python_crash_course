# 'none' is used in the functio as a placeholder value
def make_book(title, author, year, pages = None):
    
    book = {"title": title, "author": author, "year": year}

    # 'pages' will get added to the dictionary if it contains a value
    if pages:
        book["pages"] = pages

    return book

# as long as this flag is set to 'true' the loop will continue
submission_active = True

while submission_active:
    book_title = input("\nenter the book title: ")
    book_author = input("enter the book author: ")
    book_year = input("enter the book publication year: ")
    book_pages = input("enter the book total pages: ")

    repeat = input("\nenter 'yes' to make another book or 'no' to quit: ")

    if repeat == "no":

        # set the flag to 'false' to exit the loop
        submission_active = False
    
    # build the dictionary item with user inputs
    book = make_book(book_title, book_author, book_year, book_pages)
    print(f"\n{book}")

# notes
    # functions do not have to display output directly
    # functions can process data and return a value or set of them
    # 'return' allows you to move much of your programs work into functions
    # 'none' evaluates to 'false' in conditional tests
    # python structures can be used inside functions