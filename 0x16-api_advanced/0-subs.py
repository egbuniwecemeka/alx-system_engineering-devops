#!/usr/bin/python3
""" Reddit API query that returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Queries Reddit API and returns total number of subscribers"""

    url = "https://www.reddit.com/r/{}/about-json".format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}
    request = requests.get(url, headers=headers, allow_redirects=False)
    data = request.json()
    if data == 200:
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
