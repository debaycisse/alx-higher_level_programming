#!/usr/bin/python3
"""This module takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/users/{}'.format(argv[1])
    github_req_header = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {}'.format(argv[2]),
        'X-GitHub-Api-Version': '2022-11-28'
    }
    resp = requests.get(url, headers=github_req_header)
    if resp.status_code == 200:
        print(resp.json().get('id'))
