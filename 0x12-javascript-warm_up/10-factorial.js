#!/usr/bin/node
// Prints the factorial
const argv = process.argv;
const value = parseInt(argv[2]);
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else if (n < 0) {
    return ("Can't find the factorial of negative values");
  } else {
    return n * factorial(n - 1);
  }
}
const ans = factorial(value);
console.log(ans);
