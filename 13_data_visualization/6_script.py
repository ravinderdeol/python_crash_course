import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# open and load the json file
# store the set of data in the variable 'all_eq_data'
filename = "eq_30_day_m1.json"
with open (filename) as f:
    all_eq_data = json.load(f)

# create a more readable version of the json file
# 'indent' tells 'dump' to format the data using indentation matching the data structure to make it more readable
readable_file = "readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent = 4)

# save the title of the data set to a variable
dataset_title = all_eq_data["metadata"]["title"]

# save all of the data associated with the key 'features'
all_eq_dicts = all_eq_data["features"]

# create a list of the magnitude, longitude, latitude, and description of the earthquakes
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:

    # magnitude of each earthquake is stored under the key 'properties' then 'mag'
    mags.append(eq_dict["properties"]["mag"])

    # longitude and latitude of each earthquake is stored under the key 'geometry' then 'coordinates'
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

    # description for each earthquake is stored under the key 'properties' then 'title'
    hover_texts.append(eq_dict["properties"]["title"])

# define a dictionary called 'data' and create the 'scattergeo' object inside it
# the key 'marker' is used to define the size of the markers
# we use a list comprehension and multiply each magnitude to create larger markers
# the key 'text' is used to define the text that appears when you hover over a marker
# 'color' tells plotly what values it should use to determine where each marker falls on the color scale
# 'colorscale' tells plotly which color scale to use
# 'reversescale' tells plotly to reverse the color scale as we want bright for small mags and dark for large
# 'colorbar' settings allow us to control the appearance of the color scale shown and we write a title
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [6 * mag for mag in mags],
        "color": mags,
        "colorscale": "agsunset",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
        },
    }]

my_layout = Layout(title = f"{dataset_title}")

# create a dictionary called 'fig' that contains the data and layout
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename = "global_earthquakes.html")

# notes
    # data for this is at https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/mapping_global_data_sets/data/eq_data_30_day_m1.json
    # plotly color scales can be found at https://plotly.com/python/builtin-colorscales/
    # the json data format helps us to store large amounts of data in a way that is easy to work with
    # always check whether the convention you are working with with using latitude or longitude first
    # the 'scattergeo' object is created inside a list because you can plot multiple data sets in the same figure
    # 'data = [Scattergeo(lon = lons, lat = lats)]' is a simple way to define data for a chart but not the best for customisation
    # a dictionary is used as the value associated with 'marker' because you can specify multiple options for the markers