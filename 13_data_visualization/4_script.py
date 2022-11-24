import csv
from datetime import datetime
import matplotlib.pyplot as plt

# assign the name of the file to a variable
filename = "sitka_weather_2018.csv"

# open the file and assign the resulting file object to the variable 'f'
with open(filename) as f:

    # variable to hold 'csv.reader' which creates a reader object when it is passed a file object
    reader = csv.reader(f)
    
    # 'next' function returns the next line when passed the reader object in this case the header
    header_row = next(reader)
    
    # empty list to hold the dates and high and low temperatures
    dates, highs, lows = [], [], []

    # loop through each row in the file after the header
    for row in reader:

        # convert the date information to a datetime object
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        # each loop pulls the data from the index specified and converts it to an integer
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn")
fig, ax = plt.subplots()

# pass the lists of data to the 'plot' function
# 'c' argument sets the color of the line
# 'alpha' argument sets the transparency of the line from zero to one
ax.plot(dates, highs, c = "red", alpha = 0.6)
ax.plot(dates, lows, c = "blue", alpha = 0.6)

# 'fill_between' takes the list of dates as x-values and the list of highs and lows as y-values
# 'facecolor' argument sets the color of the shaded area
ax.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.2)

# specify the title of the chart and the font size
ax.set_title("sitka daily high and low temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 16)

# draw the date labels diagonally to prevent them from overlapping
fig.autofmt_xdate()

# specify the label for the y axis and the font size
ax.set_ylabel("temperature (F)", fontsize = 16)

# specify the size of the tick labels
ax.tick_params(axis = "both", which = "major", labelsize = 16)

plt.show()

# notes
    # data for this is at https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv
    # csv files are easier for machines to read than humans 
    # 'enumerate' function returns the index and value of each item in a list and can be used to check the index of headers
    # ideally separate the code that generates data from the code that visualizes the data
    # 'csv' module parses lines in a csv file