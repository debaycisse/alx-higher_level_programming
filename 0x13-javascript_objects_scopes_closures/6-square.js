#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let squareFill = '';
      for (let i = 0; i < this.width; i++) {
        squareFill += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(squareFill);
      }
    }
  }
}
module.exports = Square;
