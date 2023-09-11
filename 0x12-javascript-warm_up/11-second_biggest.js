#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const argLen = argv.length - 2;

if (argLen <= 1) {
  console.log(0);
} else {
  const args = [];

  for (let i = 0; i < argLen; i++) {
    const idx = i + 2;
    args.push(Number(argv[idx]));
  }

  function maxValue (max, currentValue) {
    return max > currentValue ? max : currentValue;
  }

  const maxNum = args.reduce(maxValue, args[0]);
  console.log(maxNum);
}
