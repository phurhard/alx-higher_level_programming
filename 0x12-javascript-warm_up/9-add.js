#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  console.log(a + b);
}
const a = +argv[2];
const b = +argv[3];
add(a, b);
