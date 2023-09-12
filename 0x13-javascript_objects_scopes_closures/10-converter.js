#!/usr/bin/node

exports.converter = function (base) {
  function changeBase (number) {
    return number.toString(base);
  }
  return changeBase;
};
