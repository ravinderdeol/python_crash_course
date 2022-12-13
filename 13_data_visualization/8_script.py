from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests 
import json

# this url gets the top five hundred stories from hacker news
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# make the api call
r = requests.get(url)

# convert the response object to a python list
submission_ids = r.json()

# create an empty list to store the dictionaries
submission_dicts = []

# loop through the first thirty items in the list
for submission_id in submission_ids[:30]:

    # make separate api calls for each of the submissions
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    
    # make the api call
    r = requests.get(url)
    
    # convert the response object to a python list
    response_dict = r.json()

    # create a dictionary for each submission
    try:
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"],
            }
    except KeyError:
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
            "comments": 0,
            }

    # append each submission dictionary to the submission dictionaries list
    submission_dicts.append(submission_dict)

# sort the list of dictionaries by the number of comments
submission_dicts = sorted(submission_dicts, key = itemgetter("comments"), reverse = True)

# define the type of plot to create
# define data on the x and y axes
# define the hover template for each data point
data = [{
    "type": "bar",
    "x": [submission_dict["title"] for submission_dict in submission_dicts],
    "y": [submission_dict["comments"] for submission_dict in submission_dicts],
    "hovertemplate": "<b>%{x}</b> <br>%{y} Comments",
    "marker": {
        "color": "rgb(171, 209, 198)",
        "line": {"width": 1, "color": "rgb(0, 30, 29)"},
    },
    "opacity": 0.8,
}]

# build a dictionary with the layout specs to use instead of passing a 'layout' object to the 'plot' function
my_layout = {
    "title": "Most-Commented On Hacker News",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Title",
        "titlefont": {"size": 24},
    },
    "yaxis": {
        "title": "Comments",
        "titlefont": {"size": 24},
    },
}

# create a figure object
fig = {"data": data, "layout": my_layout}

# plot the data
offline.plot(fig, filename = "hacker_news.html")

# notes
    # documentation for the hacker news api is at https://github.com/HackerNews/API