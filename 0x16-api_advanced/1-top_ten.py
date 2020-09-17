#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    agent_user = {'User-agent': 'Marisol2201'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    get_req = requests.get(url, headers=agent_user)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        print(None)
    else:
        dict_p = get_subs["data"]["children"]
        for i in range(len(dict_p)):
            print(dict_p[i]["data"]["title"])
