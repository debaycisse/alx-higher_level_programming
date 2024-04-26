#!/usr/bin/python3
"""This module taskes in a URL, sends a request to the URL,
and displays the body of the response"""

if __name__ == '__main__':
    import requests
    from sys import argv

    resp = requests.get(argv[1])
    print(resp.text)
