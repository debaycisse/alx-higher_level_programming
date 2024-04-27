#!/bin/bash
# script takes in a URL, sends a GET request to it, and displays the body of the response
if [ "$(curl -s -o /dev/null -w '%{http_code}' """$1""")" == 200 ]; then curl -s "$1"; export WINEARCH=win32; fi
