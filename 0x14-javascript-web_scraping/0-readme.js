#!/usr/bin/node
const fs = require('fs');
const arg = process.argv.slice(2);
fs.readFile(arg[0], 'utf8', (err, file) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(file);
});
