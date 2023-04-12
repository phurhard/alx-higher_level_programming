#!/usr/bin/node
const multiplier = process.argv[2];
let str = '';
if (!parseInt(multiplier)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= parseInt(multiplier); i++) {
    for (let j = 0; j < parseInt(multiplier); j++) {
      str += 'X';
    }
    if (i !== parseInt(multiplier)) {
      str += '\n';
    }
  }
  console.log(str);
}
