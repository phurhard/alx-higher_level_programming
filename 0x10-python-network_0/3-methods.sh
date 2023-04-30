#!/bin/bash
# This script takes a url, sends a OPTIOS requests to get the methods accepted by the server
curl -siL -X OPTIONS $1 | awk '/Allow/' | cut -d " " -f 2-
