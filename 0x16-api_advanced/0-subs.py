#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit is
given, the function should return 0"""
import requests


def number_of_subscribers(subreddit):
    """"queries the Reddit API"""
    agent_user = {'User-agent': 'Marisol2201'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    get_req = requests.get(url, headers=agent_user)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        return (0)
    else:
        return(get_subs["data"]["subscribers"])
