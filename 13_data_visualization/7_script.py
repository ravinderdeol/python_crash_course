import requests
from plotly.graph_objs import Bar
from plotly import offline

# store the url we want to access in a variable
url = "https://api.github.com/search/repositories?q=language:python&sort=stargazers_count&direction=desc"

# define the headers for the api call and specify the version of the api
headers = {"Accept": "application/vnd.github.v3+json"}

# make the api call using requests
r = requests.get(url, headers = headers)

# response object has a status code attribute that can tell us if a call was successful
print(f"Status code: {r.status_code}")

# json file is returned so we use the json method to convert the response to a dictionary
response_dict = r.json()

# 'items' key contains a list of dictionaries
repo_dicts = response_dict["items"]

# empty lists to store the data we want to visualize
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:

    # access and append necessary data to the specified lists
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br/>{description}"
    labels.append(label)

# define the type of plot to create
# define data on the x and y axes
# define the hover text for each data point
# define the color and style of the bars
data = [{
    "type": "bar",
    "x": repo_links,
    "y": stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
    },
    "opacity": 0.6,
}]

# build a dictionary with the layout specs to use instead of passing a 'layout' object to the 'plot' function
my_layout = {
    "title": "Most-Starred Python Projects on GitHub",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename = "python_repos.html")

# notes
    # read the api documentation or examine the code to find out the information available from an api
    # most apis are rate limited meaning there is a limit to the number of requests you can make in a given time period
    # type the following into a browser to see if you are approaching the github rate limit https://api.github.com/rate_limit
    # hovering the cursor over a bar to show the information it represents is called a tooltip
    # plotly lets you use html code within text elements
    # plotly has a helpful guide at https://plot.ly/python/user-guide/
    # plotly also has a python reference guide at https://plot.ly/python/reference/
    # the github api documentation is at https://developer.github.com/v3/