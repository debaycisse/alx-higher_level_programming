#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangleFill = '';
    for (let i = 0; i < this.width; i++) {
      rectangleFill += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rectangleFill);
    }
  }
}
module.exports = Rectangle;
