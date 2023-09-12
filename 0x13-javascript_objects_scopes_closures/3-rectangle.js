#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w < 1 || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectWidth = '';
      for (let j = 0; j < this.width; j++) {
        rectWidth += 'X';
      }
      console.log(rectWidth);
    }
  }
}

module.exports = Rectangle;
