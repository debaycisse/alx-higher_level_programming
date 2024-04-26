#!/usr/bin/python3
"""This module fetches data from a url, using the urllib module"""
if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: ', type(html))
        print('\t- content: ', html)
        print('\t- utf8 content: ', response.reason)
