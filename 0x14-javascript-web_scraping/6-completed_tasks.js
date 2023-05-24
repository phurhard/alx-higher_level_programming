#!/usr/bin/node
const arg = process.argv.slice(2);
const url = arg[0];
const request = require('request');
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const Body = JSON.parse(body);
    console.log(Body);
    // for (todo in Body) {
    //	let
  }
});
