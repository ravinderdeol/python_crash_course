# import the necessary packages
from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

# class to simulate the roll of a dice
class Die:

    # a die has by default six sides unless it is overwritten when creating an instance
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    
    # function that returns a random value between one and the number of sides of the die
    def roll(self):
        return randint(1, self.num_sides)

# two instances of the die class are created with eight sides
die_1 = Die(8)
die_2 = Die(8)    

# for loop list comprehension that rolls each die ten thousand times and stores the results
results = [die_1.roll() + die_2.roll() for roll_num in range(10_000)]

# min value is set to the sum of the lowest possible values of the two dice
min_result = 2

#max value of the die calculated and stored in a variable
max_result = die_1.num_sides + die_2.num_sides

# list comprehension that counts the number of times each value appears in results
frequencies = [results.count(value) for value in range(min_result, max_result + 1)]

# store and create a bear for each of the possible values of the dice
x_values = list(range(min_result, max_result + 1))

# 'bar' class from plotly represents data that will be formatted as a bar chart
# 'bar' class needs a list of x values and a list of y values
# 'bar' class must be wrapped in square brackets because datasets often contain multiple elements
data = [Bar(x = x_values, y = frequencies)]

# axis can be configured in various ways with each option stored in a dictionary
# 'dtick' sets the spacing between ticks and tells ploty to label every tick
x_axis_config = {"title": "result", "dtick": 1}
y_axis_config = {"title": "frequency of result"}

# 'layout' class from plotly specifies the overall layout of the visualization
my_layout = Layout(title = "results of rolling two six-sided dice ten thousand times", xaxis = x_axis_config, yaxis = y_axis_config)

# 'offline' module from plotly is used to create the visualization and it needs a dictionary of data and a layout object
offline.plot({"data": data, "layout": my_layout}, filename = "d6_d6.html")

# notes
    # it is best to seperate the code that generates data from the code that visualizes the data
    # plotly can be used to create interactive visualization of data
    # always try your best to write code that models real world situations
    # plotly does not accept results from the range function so it must be converted to a list