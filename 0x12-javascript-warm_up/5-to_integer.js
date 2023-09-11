#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (argv[2]) {
  const number = Number(argv[2]);
  if (!isNaN(number)) {
    console.log(`My number: ${number}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
