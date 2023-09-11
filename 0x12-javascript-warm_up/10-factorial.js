#!/usr/bin/node
const process = require('process');
const argv = process.argv;

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

let arg = Number(argv[2]);
if (isNaN(arg)) {
  arg = 1;
}

console.log(factorial(arg));
