#!/usr/bin/node
const fs = require('fs');
const arg = process.argv.slice(2);
const path = arg[0];
const string = arg[1];
fs.writeFile(path, string, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
