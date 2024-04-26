#!/usr/bin/python3
"""This module fetches the resource
(https://alx-intranet.hbtn.io/status) through the requests python package"""

if __name__ == '__main__':
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print(
        "Body response:\n\t- type: {}\n\t- content: {}".format(
            type(res.text),
            res.text
        )
    )
