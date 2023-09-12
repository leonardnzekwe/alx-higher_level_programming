#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const newKey = dict[key];
  if (!newDict[newKey]) {
    newDict[newKey] = [];
  }
  newDict[newKey].push(key);
}

console.log(newDict);
