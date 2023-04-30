#!/usr/bin/bash
# This scripts sends a request to the address n receives a response, although this script kept saying method not supported even as im using the PUT method that is supported
curl -Lis -X PUT  0.0.0.0:5000/catch_me -H "Content-Type: text/plain" -d "user_id=98"

