#!/usr/bin/node
import { argv } from 'node:process';
if (!parseInt(+argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(+argv[2]));
}
