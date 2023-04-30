#!/usr/bin/bash
# This script takes a url, sennds a requests and displays
# the size of the body of the response
curl -Is $1 | awk '/Content-Length/{print $2}'
