#!/usr/bin/python3
"""A Module for querying Reddit API."""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all the hot articles recursively."""

    query_params = {"after": after, "count": count, "limit": 100}
    my_user_agent = {"User-Agent": "linux:0x16-advanced_api"}
    website = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(website,
                            params=query_params,
                            headers=my_user_agent,
                            allow_redirects=False)

    if response.status_code == 404:
        return (None)

    py_objs = response.json()
    children_objs = py_objs["data"]["children"]
    after = py_objs["data"]["after"]

    for child in children_objs:
        title = child["data"]["title"]
        hot_list.append(title)
        counter = count + 1

    if not after:
        return (hot_list)

    return (recurse(subreddit, hot_list, counter, after))
