#!/usr/bin/python3
"""
Task 0 module
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    a = 'User-Agent'
    b = 'My-User-Agent'
    info = requests.get(url, headers={a: b}, allow_redirects=False)
    if info.status_code >= 300:
        return 0
    return info.json().get("data").get("subscribers")
