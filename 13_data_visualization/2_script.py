from random import choice
import matplotlib.pyplot as plt

# class to generate random walks
class RandomWalk:
    
    # initialize the attributes of a walk
    # default number of points is 50000
    def __init__(self, num_points = 50_000):
        self.num_points = num_points

        # walks start at zero on both the x and y axis
        # both the x and y values are stored in a list
        self.x_values = [0]
        self.y_values = [0]
        
    # function to calculate the points in the walk
    def fill_walk(self):
        
        # loop continues to run until the length of the walk is equal to the number of points
        while len(self.x_values) < self.num_points:

            # use the 'choice' method to select a random direction which will either return one for right or minus one for left
            x_direction = choice([1, -1])

            # use the 'choice' method to select a random distance between zero and eight
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            
            # multiply direction by distance to determine the length of each step
            # positive values moves right and negative value moves left while a value of zero moves vertically
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            
            # positive value moves up and negative value moves down while a value of zero moves horizontally
            y_step = y_direction * y_distance
            
            # code continues to run until the walk moves
            if x_step == 0 and y_step == 0:
                continue
            
            # the next value is calculated by adding the last value in the list to the step
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # new values are appended to the list
            self.x_values.append(x)
            self.y_values.append(y)

# continue making new walks while the program is active
while True:
    
    # create a random walk and store it in a variable and call the method to fill the walk
    rw = RandomWalk()
    rw.fill_walk()

    # plot the points in the walk using the classic style
    plt.style.use("classic")
    
    # 'figsize' argument is a tuple that tells mathplotlib the dimensions of the plotting window in inches
    fig, ax = plt.subplots(figsize = (16, 9))
    
    # 'range' is used to generate a list of numbers equal to those in the walk
    point_numbers = range(rw.num_points)
    
    # feed the x and y values of the walk to the 'scatter' method
    # 's' argument sets the size of the dots
    # 'edgecolors' removes the outline around the dots
    # 'cmap' argument is the name of the colormap we want to use
    # 'c' argument is the list of values we want to use for the color map
    # lighter colors represent earlier points and darker colors represent later points
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = "none", s = 1)
    
    # empasize the first and last points of the walk
    ax.scatter(0, 0, c = "green", edgecolors = "none", s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = "red", edgecolors = "none", s = 100)

    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # show the plot
    plt.show()

    # ask the user if they want to make another walk
    keep_running = input("make another walk? (y/n): ")
    if keep_running == "n":
        break

# notes
    # ideally split the code into two files with one file containing the class and the other containing the code to plot the walk
    # mathplotlib assumes screen resolutions are 100 pixels per inch
    # use the 'dpi' argument to change the resolution of the plot and add it as a second argument in 'plt.subplots()'