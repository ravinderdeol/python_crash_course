from operator import itemgetter
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

# loop through the list and print the data
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# notes
    # documentation for the hacker news api is at https://github.com/HackerNews/API