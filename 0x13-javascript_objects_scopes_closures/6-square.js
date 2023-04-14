#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    let str = '';
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        if (i !== (this.height - 1)) {
          str += '\n';
        }
      }
      console.log(str);
    }
  }
};
