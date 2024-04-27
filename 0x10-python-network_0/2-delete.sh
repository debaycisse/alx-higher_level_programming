#!/bin/bash
# This script sends a DLETE request to the passed URL and displays the body of the response
curl -s -X DELETE "$1"
