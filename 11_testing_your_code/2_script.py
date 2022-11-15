# import the unittest module
import unittest

# function capitalizes the first letter of each word
def get_formatted_location(city, country, population = ""):

    # an if and else statement to check if the population argument is empty
    # using ':,' adds commas to the population number
    if population:
        return f"{city}, {country} - {population:,} population".title()
    else:
        return f"{city}, {country}".title()

# descriptive class name that then inherits from 'unittest.testcase'
class NamesTestCase(unittest.TestCase):

    # function to test the code in the 'get_formatted_location' function if the 'else' block triggers
    def test_city_country(self):
        
        # calling the function we want to test with arguments defined
        formatted_location = get_formatted_location("london", "england")

        # this method verifies that the result we get matches the result we expected
        self.assertEqual(formatted_location, "London, England")

    # function to test the code in the 'get_formatted_location' function if the 'if' block triggers
    def test_city_country_population(self):

        # calling the function we want to test with arguments defined
        formatted_location = get_formatted_location("london", "england", 1000000)

        # this method verifies that the result we get matches the result we expected
        self.assertEqual(formatted_location, "London, England - 1,000,000 Population")

# the special variable 'name' is set when the program is executed
# if the file is being run as the main program then the value of 'name' is set to 'main'
if __name__ == "__main__":

    # this runs the test case we defined
    # if a testing framework imports this file the value of 'name' will not be 'main' and this block would not be executed
    unittest.main()

# notes
    # the user input and function and test should be in separate files
    # the test would fail if the output of the function does not equal what is defined in 'self.assertEqual'
    # writing test for the most critical part of the code is often good enough
    # use the word 'test' in the name of a class that is testing functions
    # and use the word 'test' in the name of a function that is testing specific parts of the code