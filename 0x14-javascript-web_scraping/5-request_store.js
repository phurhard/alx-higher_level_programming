#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
const url = arg[0];
const file = arg[1];
request(url).pipe(fs.createWriteStream(file));
