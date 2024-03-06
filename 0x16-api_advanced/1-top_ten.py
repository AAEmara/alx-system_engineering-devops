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
    subred_check_text = subred_check.content.text
    subred_obj = json.loads(subred_check_text)
    subred_check_name = subred_check_dict['names'][0]
    if (subred_check_name):
        hot_url = f'https://www.reddit.com/r/{subreddit}/hot'
        subred_hot = requests.get(hot_url)
        hot_obj = json.loads(subred_hot.content.text)
        hot_list = hot_obj['data']['children']
        titles_list = list()
        for post in hot_list:
            titles_list.append(post['data']['title'])
        print(titles_list)
    else:
        print(None)
