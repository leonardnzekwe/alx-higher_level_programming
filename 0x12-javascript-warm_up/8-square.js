#!/usr/bin/node
const process = require('process');
const argv = process.argv;

try {
  const x = Number(argv[2]);
  if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
      const shape = 'X'.repeat(x);
      console.log(shape);
    }
  } else {
    throw new Error('Error');
  }
} catch (err) {
  console.log('Missing size');
}
