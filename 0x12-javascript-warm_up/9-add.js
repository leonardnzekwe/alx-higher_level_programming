#!/usr/bin/node
const process = require('process');
const argv = process.argv;

function add (a, b) {
  return a + b;
}

if (argv[2] && argv[3]) {
  const arg1 = Number(argv[2]);
  const arg2 = Number(argv[3]);
  if (!isNaN(arg1) && !isNaN(arg2)) {
    console.log(add(arg1, arg2));
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
