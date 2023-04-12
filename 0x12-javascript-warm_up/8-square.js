#!/usr/bin/node
const multiplier = process.argv[2];
let square = '';
if (!parseInt(multiplier)) {
  console.log('Missing size');
} else {
  for (let i = 1; i < parseInt(multiplier); i++) {
    for (let j = 0; j < parseInt(multiplier); j++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
}
