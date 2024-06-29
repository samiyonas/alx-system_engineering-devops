#!/usr/bin/python3
""" how many subscribers does a given subreddit have """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ a function to see the number of subs of a subreddit """
    response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            allow_redirects=False)

    try:
        response = response.json()
        print(response.get("data").get("subscribers"))
    except Exception:
        return 0
