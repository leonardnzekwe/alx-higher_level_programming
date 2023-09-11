#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let language;
let feeling;
if (argv[2]) {
  language = argv[2];
}
if (argv[3]) {
  feeling = argv[3];
}
console.log(`${language} is ${feeling}`);
