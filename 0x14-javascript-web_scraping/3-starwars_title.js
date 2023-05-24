#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
