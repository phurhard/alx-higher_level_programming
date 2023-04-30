#!/usr/bin/bash
# This script takes a url, sends a get requests with a header attached
curl -s $1 -H "X-School-User-Id: 98"
