#!/bin/bash
# This script makes a post request with a json file as contents
curl -sL -X POST $1 -H "Content-Type: application/json" -d "@$2"
