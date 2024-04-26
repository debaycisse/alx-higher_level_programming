#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL, and displays
the value of the variable 'X-Request-Id in the response header'"""

if __name__ == '__main__':
    import requests
    from sys import argv

    resp = requests.get(argv[1])
    print(resp.headers['X-Request-Id'])
