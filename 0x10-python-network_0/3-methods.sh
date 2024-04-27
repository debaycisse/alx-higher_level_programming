#!/bin/bash
# This script taskes in a URL and displays all HTTP methods, implemented on the server or supported on the server
curl -s -X OPTIONS "$1"
