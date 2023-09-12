#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    const item = list[i];
    if (searchElement === item) {
      count++;
    } else if (searchElement === item) {
      count++;
    }
  }
  return count;
};
