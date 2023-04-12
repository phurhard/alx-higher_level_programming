#!/usr/bin/node
const multiplier = process.argv[2];
if (!parseInt(multiplier)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(multiplier); i++) {
    console.log('C is fun');
  }
}
