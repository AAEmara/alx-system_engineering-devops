#!/usr/bin/python3
"""A Module that Queries the Reddit API"""

import requests


def top_ten(subreddit):
    """Queries Reddit's API and prints the titles of the first 10 hot posts."""
    top_10 = {"limit": 9}
    website = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(website, params=top_10, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        exit()
    py_objs = response.json()
    data_objs = py_objs["data"]
    children_objs = data_objs["children"]
    for obj in children_objs:
        print(obj["data"]["title"])
