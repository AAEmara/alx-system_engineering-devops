#!/usr/bin/python3
"""A Module to query the Reddit API."""

import requests


def number_of_subscribers(subreddit):
    """Querying for the number of subscribers for a specific subreddit."""
    website = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(website, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    py_objs = response.json()
    data_objs = py_objs["data"]
    subscribers_count = data_objs["subscribers"]
    return (subscribers_count)
