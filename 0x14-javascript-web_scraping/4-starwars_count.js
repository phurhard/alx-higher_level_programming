#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = arg[0];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    let count = 0;
    const result = body.results;
    let obj;
    for (obj in result) {
      const character = result[obj].characters;
      for (const line in character) {
        if (character[line] === charId) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
