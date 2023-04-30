#!/bin/bash
# This scripts printns the status code of the request
curl -sI -o /dev/null -w "%{http_code}" $1
