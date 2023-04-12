#!/usr/bin/node
// Prints the second largest value of an argument
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const Arguments = argv.slice(2);
  Arguments.sort((a, b) => a - b);
  console.log(Arguments[Arguments.length - 2]);
}
