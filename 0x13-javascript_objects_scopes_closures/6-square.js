#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
