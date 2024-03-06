#!/usr/bin/python3
"""0-subs Module that queries a Reddit API."""


import requests
import json


def number_of_subscribers(subreddit):
    """Queries the Reddit API and Reutrns the number of subscribers."""
    subred_params = {'exact': True,
                     'query': subreddit}
    check_url = 'https://www.reddit.com/api/search_reddit_names.json'
    subred_check = requests.get(check_url,
                                params=subred_params)
    subred_check_text = subred_check.content.text
    subred_obj = json.loads(subred_check_text)
    subred_check_name = subred_check_dict['names'][0]
    if (subred_check_name):
        subred_info_url = f'https://www.reddit.com/r/{subreddit}/about.json'
        subred_info = requests.get(subred_info_url)
        subred_text = subred_info.content.text
        subred_obj = json.loads(subred_text)
        subred_subs = subred_obj['data']['subscribers']
    else:
        subred_subs = 0

    return (subred_subs)
