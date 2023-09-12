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

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
