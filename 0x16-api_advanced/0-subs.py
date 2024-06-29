#!/usr/bin/python3
""" how many subscribers does a given subreddit have """
import requests


def number_of_subscribers(subreddit):
    """ a function to see the number of subs of a subreddit """
    headers = {"User-Agent": 'firefox'}
    response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers=headers,
            allow_redirects=False)

    if response.status_code != 200:
        return 0
    response = response.json()
    return (response.get("data").get("subscribers"))
