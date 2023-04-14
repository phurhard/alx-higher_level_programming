#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      if (i !== this.height) {
        str += '\n';
      }
    }
    console.log(str);
  }
};
