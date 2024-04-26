#!/usr/bin/python3
"""This module takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""

if __name__ == '__main__':
    # post_email hr@holbertonschool.com   https://httpbin.org/post
    import urllib.request
    import urllib.parse
    from sys import argv

    data = urllib.parse.urlencode({'email': argv[2]})
    _data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data=_data) as response:
        print("Your email is: {}"
              .format(eval(response.read().decode('utf-8'))["email"]))
