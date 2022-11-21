# import matplotlib using an alias
import matplotlib.pyplot as plt

# x value goes from one to ten
x_values = range(1, 11)

# y value cubes the x value
y_values = [x ** 3 for x in x_values]

# 'style.use' allows you to use one of the available matplotlib styles on your system
plt.style.use("seaborn")

# 'fig' represents the entire figure or collection of plots generated
# 'ax' represents a single plot in the figure and is used more often than 'fig'
# 'subplots' lets us generate more than one plot in the same figure
fig, ax = plt.subplots()

# 'plot' presents data in a meaningful way
# 'linewidth' controls the thickness of the line
ax.plot(y_values, x_values, linewidth = 4)

# 'scatter' makes matplotlib read one value from each list and plot it as a single point, i.e. (1,1), (2,8), etc
# colormap provides a sequences of colors in a gradient moving from example low value light color to high value dark color
# 'c' sets the color of the dots
# 'cmap' tells pyplot which colormap to use
# 's' controls the size of the dots
ax.scatter(y_values, x_values, c = y_values, cmap = plt.cm.Blues, s = 100)

# 'set_title' is for titling the chart
# 'fontsize' controls the size of the title
ax.set_title("Cube Numbers Up To 10", fontsize = 16)

# 'set_xlabel' is for labeling the x-axis and 'set_ylabel' is for labeling the y-axis
ax.set_xlabel("Value", fontsize = 10)
ax.set_ylabel("Cube of Value", fontsize = 10)

# 'tick_params' styles the tick marks on the axes
# 'axis' is for the axis to be styled
# 'labelsize' controls the size of the tick labels
ax.tick_params(axis = "both", labelsize = 10)

# set the x-axis to a range of '1111'
# set the y-axis to a range of '11'
ax.axis([0, 1111, 0, 11])

# 'show' displays the plot in the matplotlib viewer
plt.show()

# notes
    # when 'plot' is given a sequence of numbers it will assume the first datapoint corresponds to an x-coordinate of 0
    # mathplotlib is a mathematical plotting library and plotlty generates visuals that resize automatically
    # the 'pyplot' module contains many functions to help genrate visualizations
    # run '(alias).style.available' to see the available styles
    # all of the colormaps are on the mathplotlib website
    # 'alias.savefig("filename.png", bbox_inches = "tight")' is how to save a visualization
    # 'bbox_inches' trims extra whitespace from the plot