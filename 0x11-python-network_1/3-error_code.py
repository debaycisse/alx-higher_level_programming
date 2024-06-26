#!/usr/bin/python3
"""This module taskes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
