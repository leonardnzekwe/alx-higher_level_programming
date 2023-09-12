#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let rectWidth = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          rectWidth += c;
        } else {
          rectWidth += 'X';
        }
      }
      console.log(rectWidth);
    }
  }
}

module.exports = Square;
