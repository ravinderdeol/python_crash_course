# imports the 'make_sandwich' module and the 'make' function
from make_sandwich import make

make("chicken", "avocado", "onion", "mayonnaise")

# notes
    # 'import module_name' imports an entire module and dot notation would be used to access specific functions
    # 'from module_name import function_name' imports a specific function and dot notation would not be needed
    # 'from module_name import *' imports every function from a module and no dot notation is needed
    # 'from module_name import function_name as new_name' imports a function and renames it
    # 'from module_name' import as new_name' imports a module and renames it
    # 'from module_name import function_name, function_name, function_name' imports multiple functions
    # it is best to only import specific functions or the entire module and use dot notation
    # modules and functions have be descriptive, undersored, and lowercase
    # every function should have a comment explaining what it does
    # when specfiying a default value leave no space beside the equal sign
    # modules make your code easier to read and maintain
