#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable, which is found
in the header of the response"""

if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
