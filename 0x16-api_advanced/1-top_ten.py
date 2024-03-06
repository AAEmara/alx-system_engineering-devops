#!/usr/bin/python3
"""1-top-ten Module for querying the top 10 posts for a subreddit."""


import requests
import json


def top_ten(subreddit):
    """Queries the Reddit API and Prints the title of the first 10 hot
    posts listed for a given subreddit."""
    subred_params = {'exact': True,
                     'query': subreddit}
    check_url = 'https://www.reddit.com/api/search_reddit_names.json'
    subred_check = requests.get(check_url,
                                params=subred_params)
    subred_check_text = subred_check.text
    subred_obj = json.loads(subred_check_text)
    if (subred_obj['names'][0]):
        hot_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        subred_hot = requests.get(hot_url)
        hot_obj = json.loads(subred_hot.text)
        hot_list = hot_obj['data']['children']
        titles_list = list()
        i = 0
        for post in hot_list:
            print(post['data']['title'])
            i += 1
            if i == 10:
                return
    else:
        print(None)
