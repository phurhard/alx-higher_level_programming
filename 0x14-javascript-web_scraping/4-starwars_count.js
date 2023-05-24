#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = arg[0];
const charId = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    const result = body.count;
    let count = 0;
    for (let chr in body['results']['characters']) {
        if (chr == charId) {
	  count = count + 1;
	  console.log(chr);
	  return
	}
    }
    console.log(count);
  }
});
