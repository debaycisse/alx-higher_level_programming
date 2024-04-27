#!/bin/bash
# This script takes in a URL as an argument and sends a GET request to it, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
