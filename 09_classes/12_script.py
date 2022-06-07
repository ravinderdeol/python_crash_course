# import the a python standard library
from random import randint

class Die:

    # the class has one attribute with a default value
    def __init__(self, sides = 6):
        self.sides = sides
    
    # a method to print a random number from one to six
    def roll_die(self):
        print(randint(1, self.sides))

# using dot notation to call a method
Die().roll_die()
Die().roll_die()
Die().roll_die()
Die().roll_die()

# notes
    # include a space between imporrting python standard libraries and your own