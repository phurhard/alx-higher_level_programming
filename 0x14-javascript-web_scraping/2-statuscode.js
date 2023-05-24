#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = arg[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
