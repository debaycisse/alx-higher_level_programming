#!/bin/bash
# This script takes in a URL as an argument, sends a POST request to it, and displays the content of the body of the response of the request
curl -s -H 'Content-Type: application/json' -d '{email: test@gmail.com, subject: I will always be here for PLD}' -X POST "$1"
