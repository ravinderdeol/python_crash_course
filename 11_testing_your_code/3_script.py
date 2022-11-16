# import the unittest module
import unittest

class Employee:

    # function that stores the arguments as attributes
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    # function that raises the salary by a default amount but also accepts custom amounts
    def give_raise(self, raise_amount = 5000):
        self.annual_salary += raise_amount
    
    # function that prints the prints the details of the employee formatted
    def describe_employee(self):
        return f"{self.first_name.title()} {self.last_name.title()} - ${self.annual_salary:,}"

# descriptive class name that then inherits from 'unittest.testcase'
class EmployeeTestCase(unittest.TestCase):

    # the set up method from unit test allows us to create an instance once and reuse it in all of the test methods
    def setUp(self):
        self.employee = Employee("john", "smith", 10000)
    
    # function to test the default raise amount set within the class
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 15000)
    
    # function to test the custom raise amount which is passed as an argument
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 20000)
    
    # function to test the formatting of the employee details using the values in set up
    def test_describe_employee(self):
        self.assertEqual(self.employee.describe_employee(), "John Smith - $10,000")

if __name__ == "__main__":
    unittest.main()

# notes
    # the user input and function and test should be in separate files
    # you can only use the methods below in a class that inherits from 'unittest.testcase'
    # 'assertequal(a, b)' verifies that 'a' == 'b'
    # 'assertnotequal(a, b)' verifies that 'a' != 'b'
    # 'asserttrue(x)' verifies that 'x' is true
    # 'assertfalse(x)' verifies that 'x' is false
    # 'assertin(item, list)' verifies that 'item' is in 'list'
    # 'assertnotin(item, list)' verifies that 'item' is not in 'list'