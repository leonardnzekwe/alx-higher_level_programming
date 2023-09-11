#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const argLen = argv.length - 2;

if (argLen === 0 || argLen === 1) {
  console.log('0');
} else {
  let max = 0;
  for (let i = 0; i < argLen; i++) {
    const idx = i + 2;
    const arg = Number(argv[idx]);
    if (max < arg) {
      max = arg;
    }
  }
  console.log(max);
}
