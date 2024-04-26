#!/usr/bin/python3
"""This module takes in a ltter, and send a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) < 2:
        resp = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': ""}
        )
    else:
        resp = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': argv[1]}
        )
    try:
        data_json = resp.json()
        if len(data_json) > 0 and resp.status_code == 200:
            print('[{}] {}'.format(data_json['id'], data_json['name']))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')
